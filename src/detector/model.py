from src.mrcnn import model as model_lib

from src.detector.config import DetectorConfig, InferenceConfig


class Model:
    """ Model class

    """

    ROOT_DIR = 'models'
    MODEL_PATH = 'models/pneumonia20220510T0028/mask_rcnn_pneumonia_0001.h5'
    config = DetectorConfig()

    @staticmethod
    def get_model() -> None:
        """ Gets prepaired model from MODEL_PATH

        Args: None

        Returns: None

        """

        inference_config = InferenceConfig()

        model = model_lib.MaskRCNN(mode='inference', config=inference_config, model_dir=Model.ROOT_DIR)
        
        assert Model.MODEL_PATH != '', 'Provide path to trained weights'

        model.load_weights(Model.MODEL_PATH, by_name=True)
        model = model_lib.MaskRCNN(mode='inference', config=inference_config, model_dir=Model.ROOT_DIR)
        model.load_weights(Model.MODEL_PATH, by_name=True)

        return model
