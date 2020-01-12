import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
import datetime

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
        self.initUI()
        self.paused = True
        self.consol = QPlainTextEdit(self)

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
        self.timestamp.zoomIn(10)
        self.timestamp.insertPlainText("10:30:00")
        self.timestamp.move(200, 850)
        self.timestamp.show()
        self.timestamp.resize(160, 50)
        self.playpause.move(70, 850)
        self.playpause.resize(100, 50)
        self.playpause.setText("►")
        self.playpause.clicked.connect(self.togglePause)
        self.playpause.setStyleSheet("background-color: red")
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

        self.set_person({
        "device": "door sensor",
        "device-id": "156b",
        "event": "unlocked no keycard",
        "guest-id": "Marc-Andre"
    })
        self.set_person({
        "device": "access point",
        "device-id": "ap1-1",
        "event": "new client",
        "guest-id": "Jason"
    })
        self.set_person({
            "device": "access point",
            "device-id": "101",
            "event": "new client",
            "guest-id": "James"
        })



        self.show()

    def changeValue(self, value):
        self.timestamp.setPlainText(time.strftime('%H:%M:%S', time.localtime(int(1578151800 + value*60*15))))

    def togglePause(self):
        self.paused = not self.paused

        if self.paused:
            self.playpause.setText("►")
        else:
            self.playpause.setText("⏸")
            # self.timer()

    # def timer(self):
    #     counter = 0
    #     # utc_time = datetime.strptime("2020-01-04T"+self.timestamp.toPlainText(), "%Y-%m-%dT%H:%M:%S")
    #     # startTime = time.gmtime(utc_time + 1)
    #
    #     def add1sec(strtime):
    #         arr = strtime.split(":")
    #         if int(arr[2]) < 59:
    #             arr[2] = str(int(arr[2]) + 1)
    #         elif arr[2] == "59" and arr[1] == "59":
    #             arr[1] = "00"
    #             arr[2] = "00"
    #             if arr[0] == "23":
    #                 arr[0] = "00"
    #             else:
    #                 arr[0] = str(int(arr[0]) + 1)
    #         elif arr[2] == "59":
    #             arr[2] = "00"
    #             arr[1] = str(int(arr[1]) + 1)
    #
    #         arr = ["0" + i if len(i) == 1 else i for i in arr]
    #         return ":".join(arr)
    #
    #     while True:
    #         curtime = time.time() * 1000
    #         print(curtime-counter)
    #         if curtime - counter < 100:
    #             print("here")
    #             time.sleep(0.1)
    #             # do nothing
    #             continue
    #         else:
    #             print('bruh')
    #             # time.sleep(0.1)
    #             self.timestamp.setPlainText(add1sec(self.timestamp.toPlainText()))
    #             counter = time.time() * 1000
    #         print(self.paused)
    #         if self.timestamp.toPlainText() == "10:29:59" or self.paused:
    #             print("am breaking")
    #             break

    def set_person(self, info):
        if info["guest-id"] == "Veronica":
            self.Veronica.setStyleSheet("background-color: red")
            self.Veronica.move(self.set_location(info["device-id"]))
        elif info["guest-id"] == "Jason":
            self.Jason.setStyleSheet("background-color: blue")
            self.Jason.move(self.set_location(info["device-id"]) + QPoint(0, 5))
        elif info["guest-id"] == "Thomas":
            self.Thomas.setStyleSheet("background-color: green")
            self.Thomas.move(self.set_location(info["device-id"]) + QPoint(0, 10))
        elif info["guest-id"] == "Eugene":
            self.Eugene.setStyleSheet("background-color: yellow")
            self.Eugene.move(self.set_location(info["device-id"]) + QPoint(0, 15))
        elif info["guest-id"] == "Salina":
            self.Salina.setStyleSheet("background-color: pink")
            self.Salina.move(self.set_location(info["device-id"]) + QPoint(0, 20))
        elif info["guest-id"] == "Rob":
            self.Rob.setStyleSheet("background-color: orange")
            self.Rob.move(self.set_location(info["device-id"]) + QPoint(0, 25))
        elif info["guest-id"] == "Kristina":
            self.Kristina.setStyleSheet("background-color: purple")
            self.Kristina.move(self.set_location(info["device-id"]) + QPoint(0, 30))
        elif info["guest-id"] == "Alok":
            self.Alok.setStyleSheet("background-color: brown")
            self.Alok.move(self.set_location(info["device-id"]) + QPoint(0, 35))
        elif info["guest-id"] == "Marc-Andre":
            self.MarcAndre.setStyleSheet("background-color: magenta")
            self.MarcAndre.move(self.set_location(info["device-id"]) + QPoint(0, 40))
        elif info["guest-id"] == "n/a":
            self.na.setStyleSheet("background-color: gray")
            self.na.move(self.set_location(info["device-id"]) + QPoint(0, 45))
        elif info["guest-id"] == "Dave":
            self.Dave.setStyleSheet("background-color: cyan")
            self.Dave.move(self.set_location(info["device-id"]) + QPoint(0, 50))
        elif info["guest-id"] == "James":
            self.James.setStyleSheet("background-color: Maroon")
            self.James.move(self.set_location(info["device-id"]) + QPoint(0, 55))
        elif info["guest-id"] == "Harrison":
            self.Harrison.setStyleSheet("background-color: black")
            self.Harrison.move(self.set_location(info["device-id"]) + QPoint(0, 60))

    def set_location(self, id_):
        if id_ == "ap1-1":
            return QPoint(500, 20)

        elif id_ == "ap1-2":
            return QPoint(1000, 240)

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
            return QPoint(498, 225)

        elif id_ == "130":
            return QPoint(493, 313)

        elif id_ == "151":
            return QPoint(936, 53)

        elif id_ == "152":
            return QPoint(905, 351)

        elif id_ == "154":
            return QPoint(1015, 351)

        elif id_ == "155":
            return QPoint(1083, 20)

        elif id_ == "156":
            return QPoint(1114, 321)

        elif id_ == "156b":
            return QPoint(1111, 412)

        elif id_ == "210":
            return QPoint(465, 505)

        elif id_ == "231":
            return QPoint(592, 502)

        elif id_ == "233":
            return QPoint(719, 503)

        elif id_ == "235":
            return QPoint(841, 505)

        elif id_ == "241":
            return QPoint(965, 505)

        elif id_ == "247":
            return QPoint(1094, 510)

        elif id_ == "200":
            return QPoint(935, 683)

        elif id_ == "250":
            return QPoint(1191, 688)

        elif id_ == "248":
            return QPoint(1146, 782)

        elif id_ == "244":
            return QPoint(1013, 784)

        elif id_ == "236":
            return QPoint(897, 828)

        elif id_ == "234":
            return QPoint(723, 803)

        elif id_ == "232":
            return QPoint(547, 824)

        elif id_ == "220":
            return QPoint(421, 734)

        else:
            return QPoint(0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
