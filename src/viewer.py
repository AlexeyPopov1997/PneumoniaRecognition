from enum import Enum

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QLabel


class AppString(Enum):
    """ Enum of application captions

    """

    TITLE = 'Pneumonia Detector'
    LOADFILE = 'Open Image'
    SAVE = 'Analyse Image'


class Viewer(QLabel):
    """ Application's graphics viewer

    """

    def __init__(self, parent):
        super().__init__(parent)

    def update(self):
        """ Update graphics viewer

        """

        self.origin = QPoint()
