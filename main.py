import  sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBrowser")
        self.setWindowIcon(QIcon("icons/Browser-icon.png"))
        self.setGeometry(200,200,1000,600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backbutton = QPushButton()
        self.backbutton.setIcon(QIcon("icons/Back.png"))
        self.backbutton.setIconSize(QSize(36,36))
        toolbar.addWidget(self.backbutton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/Forward.png"))
        self.forwardButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.forwardButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("icons/Reload.png"))
        self.reloadButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.reloadButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/Home.png"))
        self.homeButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.homeButton)





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())