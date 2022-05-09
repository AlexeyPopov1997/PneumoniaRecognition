import cv2
import pydicom
import numpy as np
import matplotlib.pyplot as plt

from src.mrcnn import utils
from src.mrcnn.config import Config
from src.mrcnn import model as model_lib


class Images:
    ORIG_SIZE = 1024

    @staticmethod
    def analyze_image(image_path):
        image_id = image_path
        ds = pydicom.read_file(image_id)
        image = ds.pixel_array
        resize_factor = Images.ORIG_SIZE / Model.config.IMAGE_SHAPE[0]

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

        plt.imsave('.temp_files/temp1.png', image)


class DetectorConfig(Config):
    NAME = 'pneumonia'
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    BACKBONE = 'resnet50'
    NUM_CLASSES = 2
    IMAGE_MIN_DIM = 256
    IMAGE_MAX_DIM = 256
    TRAIN_ROIS_PER_IMAGE = 32
    MAX_GT_INSTANCES = 4
    DETECTION_MAX_INSTANCES = 3
    DETECTION_MIN_CONFIDENCE = 0.78
    DETECTION_NMS_THRESHOLD = 0.01
    STEPS_PER_EPOCH = 200


class InferenceConfig(DetectorConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


class Model:
    ROOT_DIR = 'models'
    MODEL_PATH = 'models/pneumonia20220510T0028/mask_rcnn_pneumonia_0001.h5'
    config = DetectorConfig()

    @staticmethod
    def get_model():
        inference_config = InferenceConfig()

        model = model_lib.MaskRCNN(mode='inference', config=inference_config, model_dir=Model.ROOT_DIR)
        assert Model.MODEL_PATH != "", "Provide path to trained weights"
        model.load_weights(Model.MODEL_PATH, by_name=True)
        model = model_lib.MaskRCNN(mode='inference', config=inference_config, model_dir=Model.ROOT_DIR)
        model.load_weights(Model.MODEL_PATH, by_name=True)
        return model
