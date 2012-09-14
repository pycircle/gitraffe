from PyQt4.QtGui import QWidget, QPainter, QImage, QPen
from PyQt4.QtCore import QPoint
from os.path import dirname

class GraphWidget(QWidget):
    def __init__(self, commit, next_commit=None):
        super().__init__()
        self.commit = commit
        self.next_commit = next_commit
        self.char_size = 13
        self.size = self.gen_size()

    def gen_size(self):
        max = 0
        for line in self.commit:
            if len(line) > max:
                max = len(line)
        return 15*max

    def commit_image(self):
        return QImage(dirname(__file__)+'/icons/commit-full.png')

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        i = 0
        for j in range(len(self.commit[0])):
            if self.commit[0][j] == '*':
                painter.drawImage(QPoint(i,0), self.commit_image())
            elif self.commit[0][j] == '|':
                painter.drawLine(i+15, 0, i+15, 30/len(self.commit))
            elif self.commit[0][j] == '\\':
                painter.drawLine(i+15, 15, i+30, 15+(15/len(self.commit)))
            elif self.commit[0][j] == '/':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/right.png'))
            elif self.commit[0][j] == '_':
                painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/line-flipped.png'))
            i += self.char_size
        down = 0
        up = 0
        for j in range(1, len(self.commit)):
            i = 0
            for k in range(len(self.commit[j])):
                if self.commit[j][k] == '|':
                    painter.drawLine(i+15, 0, i+15, (30/len(self.commit))*(j+1))
                elif self.commit[j][k] == '\\':
                    painter.drawLine(i+1, 15, i+28, 15+(15/len(self.commit))*(j+1))
                    down = 10
                    up = 2
                elif self.commit[j][k] == '/':
                    print(down)
                    painter.drawLine(i+2, (30/len(self.commit))*(j+1)-up, i+27, down+(15/len(self.commit))*(j+1))
                elif self.commit[j][k] == '_':
                    painter.drawImage(QPoint(i,0), QImage(dirname(__file__)+'/icons/line-flipped.png'))
                i += self.char_size
        painter.end()

class FirstGraphWidget(GraphWidget):
    def __init__(self, commit, next_commit=None):
        super().__init__(commit, next_commit)

    def commit_image(self):
        return QImage(dirname(__file__)+'/icons/commit-first.png')

class LastGraphWidget(GraphWidget):
    def __init__(self, commit):
        super().__init__(commit)

    def commit_image(self):
        return QImage(dirname(__file__)+'/icons/commit-last.png')
