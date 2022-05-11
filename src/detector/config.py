from src.mrcnn.config import Config


class DetectorConfig(Config):
    """Configuration for training pneumonia detection on the RSNA pneumonia dataset.
    Overrides values in the base Config class.
    
    """

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
    """ Overrides detector config

    """

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
