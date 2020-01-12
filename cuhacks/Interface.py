import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Murder Mystery'
        self.left = 100
        self.top = 20
        self.width = 640
        self.height = 480
        self.timestamp = QPlainTextEdit(self)
        self.playpause = QPushButton(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        menuShift = 400
        # Create widget
        labelTop = QLabel(self)
        pixmap1 = QPixmap('firstFloor.png')
        labelTop.setPixmap(pixmap1)
        labelTop.move(menuShift, 0)
        labelBot = QLabel(self)
        pixmap2 = QPixmap('secondFloor.png')
        labelBot.setPixmap(pixmap2)
        labelBot.move(menuShift, pixmap1.height())
        self.resize(max(pixmap1.width(), pixmap2.width()) + menuShift, pixmap1.height() + pixmap2.height())
        mySlider = QSlider(Qt.Horizontal, self)
        mySlider.setGeometry(30, 900, 350, 30)
        mySlider.setMaximum(96)
        mySlider.valueChanged[int].connect(self.changeValue)
        self.timestamp.insertPlainText("Time")
        self.timestamp.move(200, 850)
        self.timestamp.resize(160, 50)
        self.show()

    def changeValue(self, value):
        self.timestamp.move(100, 850)
        self.timestamp.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
