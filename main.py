import  sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
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
        self.backbutton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backbutton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/Forward.png"))
        self.forwardButton.setIconSize(QSize(36, 36))
        self.forwardButton.clicked.connect(self.fowardBtn)
        toolbar.addWidget(self.forwardButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("icons/Reload.png"))
        self.reloadButton.setIconSize(QSize(36, 36))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/Home.png"))
        self.homeButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.homeButton)
        self.homeButton.clicked.connect(self.homeBtn)

        self.addressBar = QLineEdit()
        self.addressBar.setFont(QFont("comicsans",18))
        toolbar.addWidget(self.addressBar)
        self.addressBar.returnPressed.connect(self.searchBtn)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("icons/Search.png"))
        self.searchButton.setIconSize(QSize(36, 36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.WebengineViwe = QWebEngineView()
        self.setCentralWidget(self.WebengineViwe)
        self.initialURL = 'https://google.com'
        self.addressBar.setText(self.initialURL)
        self.WebengineViwe.load(QUrl(self.initialURL))

    def searchBtn (self):
        url = self.addressBar.text()
        self.WebengineViwe.load(QUrl(url))

    def backBtn (self):
        self.WebengineViwe.back()

    def fowardBtn (self):
        self.WebengineViwe.forward()

    def reloadBtn (self):
        self.WebengineViwe.reload()

    def homeBtn (self):
        self.WebengineViwe.load(QUrl(self.initialURL))






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())