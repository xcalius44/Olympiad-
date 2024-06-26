# from os import random
import random
import time
import sys
from threading import Timer


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
        self.header_label.setFont(QFont("Arial", 18))
        self.header_label.setWordWrap(True)
        self.header_label.move(565, 20)
        self.header_label.resize(200, 100)
        self.button = QPushButton("почати гру ", self)
        self.button.move(600, 100)
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
        self.speed = random.randrange(1000, 9000)
        self.speed2 = random.randrange(1000, 9000)
        self.speed3 = random.randrange(1000, 9000)
        self.cars = [self.speed, self.speed2, self.speed3]

    def buttonClicked(self):

        self.times_pressed += 1
        if self.times_pressed == 1:
            self.button.setGeometry(60, 160, 150, 30)
            self.button.move(2700, 2050)
            self.button.setText("тисни щоб їхати")
            self.header_label.setText("")
            self.car1()

    def car1(self):
        stop = max(self.cars)
        self.labelImage1.resize(100, 100)
        self.anim1 = QPropertyAnimation(self.labelImage1, b"pos")
        self.anim1.setEndValue(QPoint(1105, 160))
        self.anim1.setDuration(self.speed)
        if stop == self.speed:
            self.anim1.finished.connect(self.car_resing_finished)
        self.anim1.start()

        self.labelImage2.resize(100, 100)
        self.anim2 = QPropertyAnimation(self.labelImage2, b"pos")
        self.anim2.setEndValue(QPoint(1105, 220))
        self.anim2.setDuration(self.speed2)
        if stop == self.speed2:
            self.anim2.finished.connect(self.car_resing_finished)
        self.anim2.start()

        self.labelImage3.resize(100, 100)
        self.anim3 = QPropertyAnimation(self.labelImage3, b"pos")
        self.anim3.setEndValue(QPoint(1105, 320))
        self.anim3.setDuration(self.speed3)
        if stop == self.speed3:
            self.anim3.finished.connect(self.car_resing_finished)
        self.anim3.start()

    def car_resing_finished(self):
        self.header_label.setFont(QFont("Arial", 20))
        if min(self.cars) == self.speed:
            self.cars.remove(self.speed)
            if min(self.cars) == self.speed2:
                self.header_label.setText(
                    "car 1\
                        car 2\
                    car 3"
                )
            else:
                self.header_label.setText(
                    "car 1\
                    car 3\
                        car 2"
                )
        elif min(self.cars) == self.speed2:
            self.cars.remove(self.speed2)
            if min(self.cars) == self.speed:
                self.header_label.setText(
                    "car 2\
                    car 1\
                        car 3"
                )
            else:
                self.header_label.setText(
                    "car 2\
                    car 3\
                        car 1"
                )
        else:
            self.cars.remove(self.speed3)
            if min(self.cars) == self.speed2:
                self.header_label.setText(
                    "car 3\
                    car 2\
                        car 1"
                )
            else:
                self.header_label.setText(
                    "car 3\
                    car 1\
                        car 2"
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
