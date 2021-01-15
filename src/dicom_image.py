import pydicom


class DicomImage:
    def __init__(self, image, file_path):
        self.__image = image
        self.__image = pydicom.read_file(file_path)
        self.__filePath = file_path

    @property
    def image(self):
        return self.__image

    @property
    def file_path(self):
        return self.__filePath

    @property
    def file_name(self):
        return self.__filePath.split('\\')[-1].split('/')[-1]


class DisplayImageContainer:
    def __init__(self, image, file_path):
        self.__image = image
        self.__filePath = file_path

    @property
    def image(self):
        return self.__image

    @property
    def file_path(self):
        return self.__filePath

    @property
    def file_name(self):
        return self.__filePath.split('\\')[-1].split('/')[-1]
