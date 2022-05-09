import sys
import SimpleITK as sTk

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog

from src.viewer import Viewer, AppString
from src.pneumonia_detection import Images
from src.dicom_image import DicomImage, DisplayImageContainer


class MainUI(object):
    def __init__(self):
        self.viewer = Viewer(self)
        self.toolbar = self.addToolBar('ToolBar')
        self.analyzeBtn = QAction(QIcon('./icons/analyse.png'), '', self)
        self.loadFileBtn = QAction(QIcon('./icons/open.png'), '', self)
        self.windowWidth = 600
        self.windowHeight = 650
        self.windowTitle = AppString.TITLE.value
        self.windowXPos = 300
        self.windowYPos = 200
        self.allowImageType = '(*.dcm)'

    def setup_ui(self):
        self.loadFileBtn.setIconText(AppString.LOADFILE.value)
        self.analyzeBtn.setIconText(AppString.SAVE.value)

        font = QFont('Roboto', 9)
        self.loadFileBtn.setFont(font)
        self.analyzeBtn.setFont(font)

        self.toolbar.setMovable(False)
        self.toolbar.addActions([self.loadFileBtn, self.analyzeBtn])

        for action in self.toolbar.actions():
            widget = self.toolbar.widgetForAction(action)
            widget.setFixedSize(299, 60)

        self.toolbar.setIconSize(QSize(30, 30))
        self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon | Qt.AlignLeading)
        self.toolbar.setStyleSheet('''
                                        QToolBar {
                                            padding-right: 30px;
                                        }
                                        QToolButton {
                                            border: none;
                                            background-color: rgb(255, 255, 255);
                                        }
                                        QToolButton:hover {	
                                            background-color: rgb(229, 229, 229);
                                        }
                                        font-family: cursive;
                                    ''')

        self.setCentralWidget(self.viewer)
        self.setGeometry(self.windowXPos, self.windowYPos, self.windowWidth, self.windowHeight)
        self.setWindowIcon(QIcon('icons/taskbar_logo.png'))
        self.setWindowTitle(self.windowTitle)
        self.setStyleSheet('background-color: rgb(255, 255, 255)')


class PneumoniaDetection(QMainWindow, MainUI):
    dicomImage: DicomImage

    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setMinimumSize(self.windowWidth, self.windowHeight)
        self.loadFileBtn.triggered.connect(self.open_file_dialogue)
        self.analyzeBtn.triggered.connect(self.analyze_image)
        self.show()
        self.setFocus()
        self.loadImage = None
        self.dicomImage = None
        self.imagePath = None

    def initialize(self):
        self.loadImage = None
        self.dicomImage = None

    def open_file_dialogue(self):
        imagePath, fileType = QFileDialog.getOpenFileName(self, 'Select Image', '',
                                                          'Image files {}'.format(self.allowImageType),
                                                          options=QFileDialog.DontUseNativeDialog)

        if imagePath != '':
            img = sTk.ReadImage(imagePath)
            img = sTk.IntensityWindowing(img, -1000, 1000, 0, 255)
            img = sTk.Cast(img, sTk.sitkUInt8)
            sTk.WriteImage(img, "./.temp_files/temp.png")
            rawImage = QImage('./.temp_files/temp.png')

            self.initialize()
            self.viewer.initialize()
            self.loadImage = DisplayImageContainer(rawImage, imagePath)
            self.dicomImage = DicomImage(rawImage, imagePath)
            self.viewer.setPixmap(QPixmap.fromImage(rawImage.scaled(self.viewer.width(), self.viewer.height())))
            self.imagePath = imagePath

    def analyze_image(self):
        imagePath = Images.analyze_image(self.imagePath)
        if imagePath != '':
            rawImage = QImage('./.temp_files/temp1.png')

            self.initialize()
            self.viewer.initialize()
            self.loadImage = DisplayImageContainer(rawImage, imagePath)
            self.viewer.setPixmap(QPixmap.fromImage(rawImage.scaled(self.viewer.width(), self.viewer.height())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PneumoniaDetection()
    sys.exit(app.exec_())
