import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint
from TestClass import Data

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.data = Data()
        self.title = 'Murder Mystery'
        self.left = 100
        self.top = 20
        self.width = 640
        self.height = 480
        self.timestamp = QPlainTextEdit(self)
        self.timestamp.setReadOnly(True)
        self.namelabel = QLabel(self)
        self.events = QListWidget(self)
        self.paused = True
        self.Veronica = QPushButton(self)
        self.Jason = QPushButton(self)
        self.Thomas = QPushButton(self)
        self.Eugene = QPushButton(self)
        self.Salina = QPushButton(self)
        self.Rob = QPushButton(self)
        self.Kristina = QPushButton(self)
        self.Alok = QPushButton(self)
        self.MarcAndre = QPushButton(self)
        self.na = QPushButton(self)
        self.Dave = QPushButton(self)
        self.James = QPushButton(self)
        self.Harrison = QPushButton(self)
        self.peopleplaces = {}
        self.latestplaces = {}
        self.advance = QPushButton(self)
        self.mySlider = QSlider(Qt.Horizontal, self)
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

        self.mySlider.setGeometry(30, 900, 350, 30)
        self.mySlider.setMaximum(96)
        self.mySlider.valueChanged[int].connect(self.changeValue)
        self.timestamp.zoomIn(10)
        self.timestamp.insertPlainText("10:30:00")
        self.timestamp.move(200, 850)
        self.timestamp.show()
        self.timestamp.resize(160, 50)
        self.Veronica.resize(25, 25)
        self.Jason.resize(25, 25)
        self.Thomas.resize(25, 25)
        self.Eugene.resize(25, 25)
        self.Salina.resize(25, 25)
        self.Rob.resize(25, 25)
        self.Kristina.resize(25, 25)
        self.Alok.resize(25, 25)
        self.MarcAndre.resize(25, 25)
        self.na.resize(25, 25)
        self.Dave.resize(25, 25)
        self.James.resize(25, 25)
        self.Harrison.resize(25, 25)
        self.Veronica.raise_()
        self.Jason.raise_()
        self.Thomas.raise_()
        self.Eugene.raise_()
        self.Salina.raise_()
        self.Rob.raise_()
        self.Kristina.raise_()
        self.Alok.raise_()
        self.MarcAndre.raise_()
        self.na.raise_()
        self.Dave.raise_()
        self.James.raise_()
        self.Harrison.raise_()
        self.events.move(30, 50)
        self.events.resize(350, 500)
        self.events.clicked.connect(self.clickitem)
        self.events.itemSelectionChanged.connect(self.clickitem)
        self.namelabel.move(30, 670)
        self.namelabel.resize(500, 70)
        self.namelabel.setStyleSheet("font: 18pt Arial")
        self.namelabel.show()
        self.namelabel.raise_()
        self.changeValue(0)
        self.advance.move(50, 850)
        self.advance.resize(100, 50)
        self.advance.setText("+ 15 min")

        self.Veronica.clicked.connect(self.vclick)
        self.Jason.clicked.connect(self.jnclick)
        self.Thomas.clicked.connect(self.tclick)
        self.Eugene.clicked.connect(self.eclick)
        self.Salina.clicked.connect(self.sclick)
        self.Rob.clicked.connect(self.rclick)
        self.Kristina.clicked.connect(self.kclick)
        self.Alok.clicked.connect(self.aclick)
        self.MarcAndre.clicked.connect(self.mclick)
        self.na.clicked.connect(self.naclick)
        self.Dave.clicked.connect(self.dclick)
        self.James.clicked.connect(self.jsclick)
        self.Harrison.clicked.connect(self.hclick)
        self.show()

    # def plus15(self):
        # print(self.timestamp.value())

    def vclick(self):
        self.namelabel.setText("Name: Veronica (guest)")

    def jnclick(self):
        self.namelabel.setText("Name: Jason (guest)")

    def tclick(self):
        self.namelabel.setText("Name: Thomas (guest)")

    def eclick(self):
        self.namelabel.setText("Name: Eugene (?)")

    def sclick(self):
        self.namelabel.setText("Name: Salina (staff)")

    def rclick(self):
        self.namelabel.setText("Name: Rob (guest)")

    def kclick(self):
        self.namelabel.setText("Name: Kristina (guest)")

    def aclick(self):
        self.namelabel.setText("Name: Alok (?)")

    def mclick(self):
        self.namelabel.setText("Name: Marc-Andre (staff)")

    def naclick(self):
        self.namelabel.setText("Name: N/A")

    def dclick(self):
        self.namelabel.setText("Name: Dave (staff)")

    def jsclick(self):
        self.namelabel.setText("Name: James (?)")

    def hclick(self):
        self.namelabel.setText("Name: Harrison (staff)")

    def clickitem(self):
        self.clearPeople()
        item = self.events.currentItem()
        self.set_person(list(self.peopleplaces.items())[self.events.currentRow()][1])
        curtime = list(self.peopleplaces.items())[self.events.currentRow()][0]
        ppl = self.data.people
        for k in ppl.keys():
            for i in range(len(ppl[k])):
                if ppl[k][i]["time"] <= int(curtime) and not ppl[k][i]["guest-id"] == "n/a":
                    print(ppl[k][i])
                    self.set_person(ppl[k][i])
        print(curtime)

    def clearPeople(self):
        self.Veronica.move(-20, -20)
        self.Jason.move(-20, -20)
        self.Thomas.move(-20, -20)
        self.Eugene.move(-20, -20)
        self.Salina.move(-20, -20)
        self.Rob.move(-20, -20)
        self.Kristina.move(-20, -20)
        self.Alok.move(-20, -20)
        self.MarcAndre.move(-20, -20)
        self.na.move(-20, -20)
        self.Dave.move(-20, -20)
        self.James.move(-20, -20)
        self.Harrison.move(-20, -20)

    def set_person(self, info):
        if info["guest-id"] == "Veronica":
            self.Veronica.setStyleSheet("background-color: red")
            self.Veronica.move(self.set_location(info["device-id"]))
        elif info["guest-id"] == "Jason":
            self.Jason.setStyleSheet("background-color: blue")
            self.Jason.move(self.set_location(info["device-id"]) + QPoint(-25, 5))
        elif info["guest-id"] == "Thomas":
            self.Thomas.setStyleSheet("background-color: green")
            self.Thomas.move(self.set_location(info["device-id"]) + QPoint(25, 10))
        elif info["guest-id"] == "Eugene":
            self.Eugene.setStyleSheet("background-color: yellow")
            self.Eugene.move(self.set_location(info["device-id"]) + QPoint(0, 15))
        elif info["guest-id"] == "Salina":
            self.Salina.setStyleSheet("background-color: pink")
            self.Salina.move(self.set_location(info["device-id"]) + QPoint(-25, 20))
        elif info["guest-id"] == "Rob":
            self.Rob.setStyleSheet("background-color: orange")
            self.Rob.move(self.set_location(info["device-id"]) + QPoint(25, 25))
        elif info["guest-id"] == "Kristina":
            self.Kristina.setStyleSheet("background-color: purple")
            self.Kristina.move(self.set_location(info["device-id"]) + QPoint(0, 30))
        elif info["guest-id"] == "Alok":
            self.Alok.setStyleSheet("background-color: brown")
            self.Alok.move(self.set_location(info["device-id"]) + QPoint(-25, 35))
        elif info["guest-id"] == "Marc-Andre":
            self.MarcAndre.setStyleSheet("background-color: magenta")
            self.MarcAndre.move(self.set_location(info["device-id"]) + QPoint(25, 40))
        elif info["guest-id"] == "n/a":
            self.na.setStyleSheet("background-color: gray")
            self.na.move(self.set_location(info["device-id"]) + QPoint(0, 45))
        elif info["guest-id"] == "Dave":
            self.Dave.setStyleSheet("background-color: cyan")
            self.Dave.move(self.set_location(info["device-id"]) + QPoint(-25, 50))
        elif info["guest-id"] == "James":
            self.James.setStyleSheet("background-color: Maroon")
            self.James.move(self.set_location(info["device-id"]) + QPoint(25, 55))
        elif info["guest-id"] == "Harrison":
            self.Harrison.setStyleSheet("background-color: black")
            self.Harrison.move(self.set_location(info["device-id"]) + QPoint(0, 60))

    def set_location(self, id_):
        if id_ == "ap1-1":
            return QPoint(500, 20)

        elif id_ == "ap1-2":
            return QPoint(1000, 215)

        elif id_ == "ap1-3":
            return QPoint(700, 300)

        elif id_ == "ap1-4":
            return QPoint(700, 20)

        elif id_ == "ap2-1":
            return QPoint(580, 640)

        elif id_ == "ap2-2":
            return QPoint(1020, 677)

        elif id_ == "ap2-3":
            return QPoint(860, 640)

        elif id_ == "100":
            return QPoint(700, 70)

        elif id_ == "101":
            return QPoint(500, 500)

        elif id_ == "105":
            return QPoint(722, 324)

        elif id_ == "110":
            return QPoint(573, 94)

        elif id_ == "130":
            return QPoint(560, 381)

        elif id_ == "151":
            return QPoint(936, 89)

        elif id_ == "152":
            return QPoint(905, 351)

        elif id_ == "154":
            return QPoint(1015, 340)

        elif id_ == "155":
            return QPoint(1083, 122)

        elif id_ == "156":
            return QPoint(1114, 321)

        elif id_ == "156b":
            return QPoint(1111, 412)

        elif id_ == "210":
            return QPoint(465, 650)

        elif id_ == "231":
            return QPoint(592, 594)

        elif id_ == "233":
            return QPoint(719, 597)

        elif id_ == "235":
            return QPoint(841, 594)

        elif id_ == "241":
            return QPoint(965, 626)

        elif id_ == "247":
            return QPoint(1094, 620)

        elif id_ == "200":
            return QPoint(935, 683)

        elif id_ == "250":
            return QPoint(1191, 728)

        elif id_ == "248":
            return QPoint(1146, 828)

        elif id_ == "244":
            return QPoint(1013, 828)

        elif id_ == "236":
            return QPoint(897, 870)

        elif id_ == "234":
            return QPoint(723, 803)

        elif id_ == "232":
            return QPoint(547, 870)

        elif id_ == "220":
            return QPoint(421, 771)

        elif id_ == "elevator":
            return QPoint(732, 200)

        elif id == "150":
            return QPoint(1170, 240)

        elif id_ == "stairwell":
            return QPoint(1170, 240)

        else:
            return QPoint(0, 0)

    def changeValue(self, value):
        self.events.clear()
        self.timestamp.setPlainText(time.strftime('%H:%M:%S', time.localtime(int(1578151800 + value*60*15))))
        d = self.data.getEvents(1578151800 + value*60*15)
        for i in d:
            item = QListWidgetItem(time.strftime('%H:%M:%S', time.localtime(int(i))) + ": " + d[i]["guest-id"] + " " + "accessed" + " " + d[i]["device"] + " " + d[i]["device-id"])
            self.events.addItem(item)
        self.peopleplaces = d

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
