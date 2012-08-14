from PyQt4.QtGui import QWidget, QPainter, QImage
from PyQt4.QtCore import QPoint
import os

class GraphWidget(QWidget):
    def __init__(self, commit=''):
        super().__init__()
        self.commit = commit

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        i = 0
        for char in self.commit:
            if char == '*':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/commit.png'))
            elif char == '|':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/line.png'))
            elif char == '\\':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/left.png'))
            elif char == '/':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/right.png'))
            elif char == '_':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/line-flipped.png'))
            i += 30
        painter.end()
