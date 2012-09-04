from PyQt4.QtGui import QWidget, QPainter, QImage
from PyQt4.QtCore import QPoint
from os.path import dirname

class GraphWidget(QWidget):
    def __init__(self, commit, next_commit=None):
        super().__init__()
        self.commit = commit
        self.next_commit = next_commit
        self.char_size = 13
        self.size = 15*len(self.commit)

    def commit_image(self):
        return QImage(dirname(__file__)+'/icons/commit.png')

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        i = 0
        for j in range(len(self.commit)):
            if self.commit[j] == '*':
                painter.drawImage(QPoint(i,0), self.commit_image())
            elif self.commit[j] == '|':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/line.png'))
            elif self.commit[j] == '\\':
                #painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/left-new.png'))
                if self.next_commit != None and len(self.next_commit) > j and self.next_commit[j+1] == '\\':
                    painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/left-half.png'))
                else:
                    painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/left.png'))
            elif self.commit[j] == '/':
                #painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/right-new.png'))
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/right.png'))
            elif self.commit[j] == '_':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/line-flipped.png'))
            '''elif self.commit[j] == '-':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/line-flipped-new.png'))
            elif self.commit[j] == '_':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/line-flipped-half.png'))
            elif self.commit[j] == 'D':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/left-right.png'))'''
            i += self.char_size
        painter.end()

class FirstGraphWidget(GraphWidget):
    def __init__(self, commit, next_commit):
        super().__init__(commit, next_commit)

    def commit_image(self):
        return QImage(dirname(__file__)+'/icons/commit-first.png')

class LastGraphWidget(GraphWidget):
    def __init__(self, commit):
        super().__init__(commit)

    def commit_image(self):
        return QImage(dirname(__file__)+'/icons/commit-last.png')
