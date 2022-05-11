import pydicom


class DicomImage:
    """ DICOM Image View Class

    """

    def __init__(self, image, file_path):
        self.__image = image
        self.__image = pydicom.read_file(file_path)
        self.__filePath = file_path

    @property
    def image(self) -> None:
        """ Define image property

        """

        return self.__image

    @property
    def file_path(self):
        """ Define file path property
        
        """

        return self.__filePath

    @property
    def file_name(self):
        """ Define file name property
        
        """

        return self.__filePath.split('\\')[-1].split('/')[-1]


class DisplayImageContainer:
    """ Image container class for DICOM image displaying in Qt applitation

    """

    def __init__(self, image, file_path):
        self.__image = image
        self.__filePath = file_path

    @property
    def image(self):
        """ Define image property

        """

        return self.__image

    @property
    def file_path(self):
        """ Define file path property
        
        """

        return self.__filePath

    @property
    def file_name(self):
        """ Define file name property
        
        """
        
        return self.__filePath.split('\\')[-1].split('/')[-1]
