import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.to_paint = False

    def state(self):
        self.to_paint = True
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.to_paint:
            self.draw(qp)
        self.to_paint = False
        qp.end()

    def draw(self, qp):
        self.to_paint = True
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(10, self.height() // 2)
        point = QPoint(randint(0, self.height() - r), randint(0, self.width() - r))
        qp.drawEllipse(point, r, r)

    def resizeEvent(self, e):
        self.button.move(self.width() // 2 - self.button.width() // 2, self.height() // 2 - self.button.height() // 2)

    def initUi(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Кружочки 2')
        self.button = QPushButton(self)
        self.button.resize(100, 20)
        self.button.setText('Кружочки')
        self.button.move(self.width() // 2 - self.button.width() // 2, self.height() // 2 - self.button.height() // 2)
        self.button.clicked.connect(self.state)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec_())