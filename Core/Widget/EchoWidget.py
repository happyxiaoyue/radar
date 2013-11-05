#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QWidget 
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QSizePolicy

from PyQt4.QtCore import Qt
from PyQt4.QtCore import QPoint

import sys,os
gRootDir = os.path.join(os.getcwd(), "..", "..")
sys.path.append(gRootDir)
from Core.Data.EchoSet import EchoSet
from cfg import gEchoLineCountAFrame

gEchoLineCountAFrame = 2048

class EchoWidget(QWidget):
    mFrameIndex = 0                    # 用于记录当前放映的帧编号

    def __init__(self, parent=None):
        QWidget.__init__(self, parent) 
        
        self.setMinimumSize(200,200)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)

        self.mPixmap = QPixmap(self.width(), self.height())
        self.mPixmap.fill(Qt.black)
        self.mEchoSet = EchoSet()

        center = QPoint(self.width() / 2, self.height() / 2)        # 绘制的圆心
        radius = 0                                                  # 绘制的半径
        if self.width() < self.height():
            radius = self.width()
        radius = self.height()
        radius /= 2

        self.mEchoSet.SetCenter(center)
        self.mEchoSet.SetRadius(radius)
        self.mEchoSet.SetRange("3nm")

    def resizeEvent(self, event):
        center = QPoint(self.width() / 2, self.height() / 2)        # 绘制的圆心
        radius = 0                                                  # 绘制的半径
        if self.width() < self.height():
            radius = self.width()
        radius = self.height()
        radius /= 2
        self.mEchoSet.SetCenter(center)
        self.mEchoSet.SetRadius(radius)
        self.mPixmap = QPixmap(self.width(), self.height())
        self.mPixmap.fill(Qt.black)

    def paintEvent(self, event): 
        # 回波绘制 绘制到后台缓存
        painterToPixmap = QPainter(self.mPixmap)
        self.mEchoSet.Draw(painterToPixmap)

        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.width(), self.height(), self.mPixmap)

    def PlayAFrame(self, echoFileName):
        echoFile = open(echoFileName, "r", encoding = "utf8")

        # 偏移到 本帧处
        echoSetStrs = self.ReadAFrame(echoFile)
        self.mEchoSet.SetData(echoSetStrs)

        echoFile.close()
        self.mFrameIndex += 1 
        
        while True:
            self.repaint()

    def ReadAFrame(self, f):
        data = []

        i = 0
        while i < gEchoLineCountAFrame:
            line = f.readline()
            data.append(line)
            i += 1

        return data

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = EchoWidget()
    win.show()

    sys.exit(app.exec_())

