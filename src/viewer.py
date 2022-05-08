from enum import Enum

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QLabel


class AppString(Enum):
    TITLE = 'Pneumonia Recognition'
    LOADFILE = 'Open Image'
    SAVE = 'Analyze Image'


class Viewer(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

    def initialize(self):
        self.origin = QPoint()
