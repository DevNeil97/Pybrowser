import  sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBrowser")
        self.setWindowIcon(QIcon("icons/Browser-icon.png"))
        self.setGeometry(200,200,1000,600)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())