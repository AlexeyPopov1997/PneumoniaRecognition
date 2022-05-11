import cv2
import pydicom
import numpy as np
import matplotlib.pyplot as plt

from src.mrcnn import utils

from src.detector.model import Model


class Detector:
    """ Main detector class

    """

    ORIG_SIZE = 1024

    @staticmethod
    def analyze_image(image_path: str) -> None:
        """ Main detector class

        Args: 
            image_path (str): image path

        Returns: None

        """

        image_id = image_path
        ds = pydicom.read_file(image_id)
        image = ds.pixel_array
        resize_factor = Detector.ORIG_SIZE / Model.config.IMAGE_SHAPE[0]

        if len(image.shape) != 3 or image.shape[2] != 3:
            image = np.stack((image,) * 3, -1)

        resized_image, window, scale, padding, crop = utils.resize_image(image, min_dim=Model.config.IMAGE_MIN_DIM,
                                                                         min_scale=Model.config.IMAGE_MIN_SCALE,
                                                                         max_dim=Model.config.IMAGE_MAX_DIM,
                                                                         mode=Model.config.IMAGE_RESIZE_MODE)

        model = Model.get_model()
        results = model.detect([resized_image])
        r = results[0]

        inx = 0
        for bbox in r['rois']:
            x1 = int(bbox[1] * resize_factor)
            y1 = int(bbox[0] * resize_factor)
            x2 = int(bbox[3] * resize_factor)
            y2 = int(bbox[2] * resize_factor)
            cv2.rectangle(image, (x1, y1), (x2, y2), (220, 20, 60), 3, 1)

            cv2.putText(image, 'pneumonia: ' + str(round(r['scores'][inx], 3)), (x1, y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (220, 20, 60), 2)
            inx = inx + 1

        plt.imsave('.temp/temp1.png', image)
