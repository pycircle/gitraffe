from PyQt4.QtGui import QWidget, QPainter, QImage
from PyQt4.QtCore import QPoint
import os

class GraphWidget(QWidget):
    def __init__(self, commit='', next_commit=None):
        super().__init__()
        self.commit = commit
        self.char_size = 13
        self.size = 13*len(self.commit)
        self.next_commit = next_commit

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        i = 0
        for j in range(len(self.commit)):
            if self.commit[j] == '*':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/commit.png'))
            elif self.commit[j] == '|':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/line.png'))
            elif self.commit[j] == '\\':
                if self.next_commit != None and len(self.next_commit) > j and self.next_commit[j+1] == '\\':
                    painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/left-half.png'))
                else:
                    painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/left.png'))
            elif self.commit[j] == '/':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/right.png'))
            elif self.commit[j] == '_':
                painter.drawImage(QPoint(i,0), QImage(os.path.dirname(__file__)+'/icons/line-flipped.png'))
            i += self.char_size
        painter.end()
