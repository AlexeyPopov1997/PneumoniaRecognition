from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


from .style_sheet import StyleSheet


class MainWindowUi(object):
    def setup_ui(self, MainWindow):
        # Set MainWindow
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QSize(500, 700))

        # Set central_widget
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")

        # Set vertical layout for central_widget
        self.central_widget_vertical_layout = QVBoxLayout(self.central_widget)
        self.central_widget_vertical_layout.setObjectName(u"central_widget_vertical_layout")

        # Set central_widget_frame
        self.central_widget_frame = QFrame(self.central_widget)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setStyleSheet(StyleSheet.get_central_widget_frame_style())

        # Set vertical layout for central_widget_frame
        self.central_widget_frame_vertical_layout = QVBoxLayout(self.central_widget_frame)
        self.central_widget_frame_vertical_layout.setSpacing(0)
        self.central_widget_frame_vertical_layout.setObjectName(u"central_widget_frame_vertical_layout")
        self.central_widget_frame_vertical_layout.setContentsMargins(0, 0, 0, 0)

        # Set title_bar_frame
        self.title_bar_frame = QFrame(self.central_widget_frame)
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_frame.setMinimumSize(QSize(16777215, 30))
        self.title_bar_frame.setMaximumSize(QSize(16777215, 30))
        self.title_bar_frame.setStyleSheet(StyleSheet.get_title_bar_frame_style())

        # Set horizontal layout for title_bar_frame
        self.title_bar_frame_horizontal_layout = QHBoxLayout(self.title_bar_frame)
        self.title_bar_frame_horizontal_layout.setObjectName(u"title_bar_frame_horizontal_layout")
        self.title_bar_frame_horizontal_layout.setContentsMargins(15, 0, 0, 0)
        self.title_bar_frame_horizontal_layout.setSpacing(0)

        # Set menu_frame
        self.menu_frame = QFrame(self.title_bar_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(30, 16777215))
        self.menu_frame.setMaximumSize(QSize(30, 16777215))
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Plain)

        # Set horizontal layout for menu_frame
        self.menu_frame_horizontal_layout = QHBoxLayout(self.menu_frame)
        self.menu_frame_horizontal_layout.setObjectName(u"menu_frame_horizontal_layout")
        self.menu_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame_horizontal_layout.setSpacing(0)

        # Set logo lebel
        self.logo_label = QLabel(self.menu_frame)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(30, 16777215))
        self.logo_label.setMaximumSize(QSize(30, 16777215))
        self.logo_label.setText(u"")
        self.logo_label.setPixmap(QPixmap(u"icons/window_logo.png"))

        self.menu_frame_horizontal_layout.addWidget(self.logo_label)
        self.title_bar_frame_horizontal_layout.addWidget(self.menu_frame)

        # Set title_frame
        self.title_frame = QFrame(self.title_bar_frame)
        self.title_frame.setObjectName(u"title_frame")

        # Set horizontal layout for title_frame
        self.title_frame_horizontal_layout = QHBoxLayout(self.title_frame)
        self.title_frame_horizontal_layout.setObjectName(u"title_frame_horizontal_layout")
        self.title_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.title_frame_horizontal_layout.setSpacing(0)

        # Set title label
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_font =  QFont()
        title_font.setFamily(u"Roboto")
        title_font.setPointSize(10)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet(StyleSheet.get_title_label_style())

        self.title_frame_horizontal_layout.addWidget(self.title_label)
        self.title_bar_frame_horizontal_layout.addWidget(self.title_frame)
        
        # Set frame for buttons
        self.buttons_frame = QFrame(self.title_bar_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(150, 30))
        self.buttons_frame.setMaximumSize(QSize(150, 30))

        # Set horizontal Layout for buttons_frame
        self.buttons_frame_horizontal_layout = QHBoxLayout(self.buttons_frame)
        self.buttons_frame_horizontal_layout.setObjectName(u"buttons_frame_horizontal_layout")
        self.buttons_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_frame_horizontal_layout.setSpacing(0)

        # Set minimize_button
        self.minimize_button = QPushButton(self.buttons_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(50, 30))
        self.minimize_button.setMaximumSize(QSize(50, 30))
        self.minimize_button.setStyleSheet(StyleSheet.get_mimimize_button_style())

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/hide.png"), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)

        self.buttons_frame_horizontal_layout.addWidget(self.minimize_button)

        # Set maximize_button
        self.maximize_button = QPushButton(self.buttons_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMinimumSize(QSize(50, 30))
        self.maximize_button.setMaximumSize(QSize(50, 30))
        self.maximize_button.setStyleSheet(StyleSheet.get_maximize_button_style())

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/maximize.png"), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon)

        self.buttons_frame_horizontal_layout.addWidget(self.maximize_button)

        # Set close_button
        self.close_button = QPushButton(self.buttons_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(50, 30))
        self.close_button.setMaximumSize(QSize(50, 30))
        self.close_button.setStyleSheet(StyleSheet.get_close_button_style())

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/close.png"), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)

        self.buttons_frame_horizontal_layout.addWidget(self.close_button)
        self.title_bar_frame_horizontal_layout.addWidget(self.buttons_frame)
        self.central_widget_frame_vertical_layout.addWidget(self.title_bar_frame)

        # Set content_bar_frame
        self.content_bar_frame = QFrame(self.central_widget_frame)
        self.content_bar_frame.setObjectName(u"content_bar_frame")
        self.content_bar_frame.setStyleSheet(StyleSheet.get_content_bar_frame_style())
        self.content_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.content_bar_frame.setFrameShadow(QFrame.Raised)

        # Set vertical layout for content_bar_frame
        self.content_bar_frame_vertical_layout = QVBoxLayout(self.content_bar_frame)
        self.content_bar_frame_vertical_layout.setObjectName(u"content_bar_frame_vertical_layout")
        self.content_bar_frame_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.content_bar_frame_vertical_layout.setSpacing(0)

        # Set frame for content bar buttons
        self.content_bar_buttons_frame = QFrame(self.content_bar_frame)
        self.content_bar_buttons_frame.setObjectName(u"content_bar_buttons_frame")

        # Set horizontal layout for content_bar_frame
        self.content_bar_buttons_horizontal_layout = QHBoxLayout(self.content_bar_buttons_frame)
        self.content_bar_buttons_horizontal_layout.setObjectName("content_bar_horizontal_layout")
        self.content_bar_buttons_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.content_bar_buttons_horizontal_layout.setSpacing(0)

        # Set Open DICOM Image button
        self.open_button = QPushButton(self.content_bar_buttons_frame)
        self.open_button.setStyleSheet(StyleSheet.get_content_bar_buttons_style())
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/open.png"), QIcon.Normal, QIcon.Off)
        self.open_button.setIcon(icon)
        self.open_button.setIconSize(QSize(48, 48))
        self.open_button.setObjectName("open_button")
        self.open_button.setMinimumHeight(70)
        self.content_bar_buttons_horizontal_layout.addWidget(self.open_button)

        # Set Analyse button
        self.analyse_button = QPushButton(self.content_bar_buttons_frame)
        self.analyse_button.setStyleSheet(StyleSheet.get_content_bar_buttons_style())
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/analyse.png"), QIcon.Normal, QIcon.Off)
        self.analyse_button.setIcon(icon)
        self.analyse_button.setIconSize(QSize(48, 48))
        self.analyse_button.setObjectName("analyse_button")
        self.analyse_button.setMinimumHeight(70)
        self.content_bar_buttons_horizontal_layout.addWidget(self.analyse_button)

        self.content_bar_frame_vertical_layout.addWidget(self.content_bar_buttons_frame)

        # Set Graphics View
        self.graphics_view = QGraphicsView(self.content_bar_frame)
        self.graphics_view.setObjectName("graphicsView")
        self.graphics_view.setStyleSheet(StyleSheet.get_content_bar_buttons_style())

        self.content_bar_frame_vertical_layout.addWidget(self.graphics_view)

        self.central_widget_frame_vertical_layout.addWidget(self.content_bar_frame)

        # Set credit_bar_frame
        self.credit_bar_frame = QFrame(self.central_widget_frame)
        self.credit_bar_frame.setObjectName(u"credit_bar_frame")
        self.credit_bar_frame.setMinimumSize(QSize(16777215, 30))
        self.credit_bar_frame.setMaximumSize(QSize(16777215, 30))
        self.credit_bar_frame.setStyleSheet(StyleSheet.get_credit_bar_frame_style())
        self.credit_bar_frame.setFrameShape(QFrame.NoFrame)
        self.credit_bar_frame.setFrameShadow(QFrame.Raised)

        # Set horizontal layout for credit_bar_frame
        self.credit_bar_frame_horizontal_layout = QHBoxLayout(self.credit_bar_frame)
        self.credit_bar_frame_horizontal_layout.setSpacing(0)
        self.credit_bar_frame_horizontal_layout.setObjectName(u"credit_bar_frame_horizontal_layout")
        self.credit_bar_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)

        # Set credit_bar_label_frame
        self.credit_bar_label_frame = QFrame(self.credit_bar_frame)
        self.credit_bar_label_frame.setObjectName(u"credit_bar_label_frame")
        self.credit_bar_label_frame.setFrameShape(QFrame.StyledPanel)
        self.credit_bar_label_frame.setFrameShadow(QFrame.Raised)

        # Set vertical layout for credit_bar_label_frame
        self.credit_bar_label_frame_vertical_layout = QVBoxLayout(self.credit_bar_label_frame)
        self.credit_bar_label_frame_vertical_layout.setSpacing(0)
        self.credit_bar_label_frame_vertical_layout.setObjectName(u"credit_bar_label_frame_vertical_layout")
        self.credit_bar_label_frame_vertical_layout.setContentsMargins(15, 0, 0, 0)

        # Set label on credit_bar_label_frame
        self.credits_label = QLabel(self.credit_bar_label_frame)
        self.credits_label.setObjectName(u"credits_label")
        credits_label_font = QFont()
        credits_label_font.setFamily(u"Roboto")
        self.credits_label.setFont(credits_label_font)
        self.credits_label.setStyleSheet(StyleSheet.get_credits_label_style())

        self.credit_bar_label_frame_vertical_layout.addWidget(self.credits_label)
        self.credit_bar_frame_horizontal_layout.addWidget(self.credit_bar_label_frame)

        # Set grip_frame
        self.grip_frame = QFrame(self.credit_bar_frame)
        self.grip_frame.setObjectName(u"grip_frame")
        self.grip_frame.setMinimumSize(QSize(30, 30))
        self.grip_frame.setMaximumSize(QSize(30, 30))
        self.grip_frame.setStyleSheet(StyleSheet.get_grip_frame_style())
        self.grip_frame.setFrameShape(QFrame.StyledPanel)
        self.grip_frame.setFrameShadow(QFrame.Raised)

        self.credit_bar_frame_horizontal_layout.addWidget(self.grip_frame)
        self.central_widget_frame_vertical_layout.addWidget(self.credit_bar_frame)
        self.central_widget_vertical_layout.addWidget(self.central_widget_frame)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate('MainWindow', u'MainWindow', None))
        self.title_label.setText(QCoreApplication.translate('MainWindow', u'Pneumonia Detector', None))
        self.minimize_button.setToolTip(QCoreApplication.translate('MainWindow', u'Hide', None))
        self.maximize_button.setToolTip(QCoreApplication.translate('MainWindow', u'Maximize', None))
        self.close_button.setToolTip(QCoreApplication.translate('MainWindow', u'Close', None))
        self.open_button.setToolTip(QCoreApplication.translate('MainWindow', u'Open DICOM File', None))
        self.analyse_button.setToolTip(QCoreApplication.translate('MainWindow', u'Analyse', None))
        self.credits_label.setText(QCoreApplication.translate('MainWindow', u'Developed by Alexey Popov. May 2022', None))
