from PyQt4.QtGui import QWidget, QPainter, QImage
from PyQt4.QtCore import QPoint
import os

class DefinedGraphWidget(QWidget):
    def __init__(self, image):
        super().__init__()
        self.image = image

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        painter.drawImage(QPoint(0,0), QImage(os.path.dirname(__file__)+'/icons/'+self.image))
        painter.end()
