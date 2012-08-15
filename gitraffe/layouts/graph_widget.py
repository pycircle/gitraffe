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
        for j in range(len(self.commit)):
            if self.commit[j] == '*':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/commit.png'))
                i += 17.5
            elif self.commit[j] == '|':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/line.png'))
                i += 17.5
            elif self.commit[j] == '\\':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/left.png'))
                i += 17.5
            elif self.commit[j] == '/':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/right.png'))
                i += 17.5
            elif self.commit[j] == '_':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/line-flipped.png'))
                i += 17.5
            elif self.commit[j] == ' ':
                i += 17.5
        painter.end()
