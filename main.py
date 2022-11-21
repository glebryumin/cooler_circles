import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from  PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.state)
        self.setWindowTitle('Кружочки')
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
        qp.setBrush(QColor(255, 255, 0))
        r = randint(10, self.height() // 2)
        point = QPoint(randint(0, self.height() - r), randint(0, self.width() - r))
        qp.drawEllipse(point, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec_())