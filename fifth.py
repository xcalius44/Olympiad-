# from os import random
import random
import time
import sys
from threading import Timer

# print("Code Execution Started")


# def display():
#     print("Welcome to Guru99 Tutorials")


# t = Timer(5)
# t.start()

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time


IMG_CAR1 = QImage(
    "images/modern-car-isolated-on-transparent-background-3d-rendering-illustration-png.png"
)
IMG_CAR2 = QImage("images/images.png")
IMG_CAR3 = QImage(
    "images/transparent-car-top-view-car-top-view-white-vehicle-white-car-hood-and-top-view6608ad72b8bc39.76661637.webp"
)
IMG_FONT = QImage("images/завантаження.jpg")


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(1200, 600)
        self.setWindowTitle("Драг-рейсинг")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.place = 0
        self.labelFont = QLabel(self)
        self.labelImage1 = QLabel(self)
        self.labelImage2 = QLabel(self)
        self.labelImage3 = QLabel(self)
        self.times_pressed = 0
        self.header_label = QLabel(
            "Драг-рейсинг",
            self,
        )
        self.header_label.setWordWrap(True)
        self.header_label.move(300, 20)
        self.button = QPushButton("почати гру ", self)
        self.button.move(300, 70)
        self.button.clicked.connect(self.buttonClicked)
        self.resize(600, 600)
        car1 = QPixmap(IMG_CAR1)
        font = QPixmap(IMG_FONT)
        car2 = QPixmap(IMG_CAR2)
        car3 = QPixmap(IMG_CAR3)
        pixmap_font = font.scaled(1200, 600)
        pixmap_1_car = car1.scaled(100, 100)
        pixmap_2_car = car2.scaled(100, 100)
        pixmap_3_car = car3.scaled(100, 100)
        self.labelFont.setPixmap(pixmap_font)
        self.labelImage1.setPixmap(pixmap_1_car)
        self.labelImage2.setPixmap(pixmap_2_car)
        self.labelImage3.setPixmap(pixmap_3_car)
        self.labelImage1.move(self.place, 160)
        self.labelImage2.move(self.place, 220)
        self.labelImage3.move(self.place, 320)

    def buttonClicked(self):

        self.times_pressed += 1
        if self.times_pressed == 1:
            self.button.setGeometry(60, 160, 150, 30)
            self.button.move(2700, 2050)
            self.button.setText("тисни щоьб йихати")
            self.header_label.setText("")
            self.car1(
                speed=random.randrange(1000, 9000),
                speed2=random.randrange(1000, 9000),
                speed3=random.randrange(1000, 9000),
            )

            # self.self.cars =

        # if self.times_pressed > 1:
        #     pass

    def car1(self, speed, speed2, speed3):
        self.labelImage1.resize(100, 100)
        self.anim1 = QPropertyAnimation(self.labelImage1, b"pos")
        self.anim1.setEndValue(QPoint(1105, 160))
        self.anim1.setDuration(speed)
        self.anim1.start()

        self.labelImage2.resize(100, 100)
        self.anim2 = QPropertyAnimation(self.labelImage2, b"pos")
        self.anim2.setEndValue(QPoint(1105, 220))
        self.anim2.setDuration(speed2)
        self.anim2.start()

        self.labelImage3.resize(100, 100)
        self.anim3 = QPropertyAnimation(self.labelImage3, b"pos")
        self.anim3.setEndValue(QPoint(1105, 320))
        self.anim3.setDuration(speed3)
        self.thread.finished.connect(
            self.car_resing_finished(speed=speed, speed2=speed2, speed3=speed3)
        )
        self.anim3.start()

    def car_resing_finished(self, speed, speed2, speed3):
        self.cars = [speed, speed2, speed3]
        if min(self.cars) == speed:
            print("car1")
            self.cars.remove(speed)
            if min(self.cars) == speed2:
                print("car2")
                print("car3")
            else:
                print("car3")
                print("car2")
        elif min(self.cars) == speed2:
            print("car2")
            self.cars.remove(speed2)
            if min(self.cars) == speed:
                print("car1")
                print("car3")
            else:
                print("car3")
                print("car1")
        else:
            print("car3")
            self.cars.remove(speed3)
            if min(self.cars) == speed2:
                print("car2")
                print("car1")
            else:
                print("car1")
                print("car2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
