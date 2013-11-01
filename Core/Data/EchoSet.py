#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter

from PyQt4.QtCore import QPoint

import sys,os
gRootDir = os.path.join(os.getcwd(), "..", "..")
sys.path.append(gRootDir)
from Core.Data.EchoLine import EchoLine

class EchoSet(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mCenter = QPoint(0, 0)
        self.mEchoLines = []

    def SetData(self, echoSetStrs):
        for echoStr in echoSetStrs:
            echoLine = EchoLine(echoStr)
            self.mEchoLines.append(echoLine)

    def SetCenter(self, center):
        self.mCenter = center;

    # 回波绘制
    def Draw(self, p):
        pen = QPen(QColor(255, 255, 255))
        p.setPen(pen)
        p.drawText(50, 50, "Draw")

        self.__DrawDisCircle(p)
        self.__DrawRangeCicle(p)
        self.__DrawShipHeadLine(p)
        self.__DrawSysInfo(p)

    def paintEvent(self, paintEvent):
        p = QPainter(self)
        self.Draw(p)
        
    # 绘制量程范围
    def __DrawRangeCicle(self, p):
        pen = QPen(QColor(255, 0, 0))
        p.setPen(pen)
        p.drawText(150, 150, "__DrawRangeCicle")
    
    # 绘制距标圈
    def __DrawDisCircle(self, p):
        pen = QPen(QColor(0, 255, 0))
        p.setPen(pen)
        p.drawText(250, 250, "__DrawDisCircle")

    # 绘制船艏线
    def __DrawShipHeadLine(self, p):
        pen = QPen(QColor(0, 0, 255))
        p.setPen(pen)
        p.drawText(350, 350, "__DrawShipHeadLine")

    # 绘制系统信息
    def __DrawSysInfo(self, p):
        pen = QPen(QColor(255, 255, 0))
        p.setPen(pen)
        p.drawText(450, 450, "__DrawSysInfo")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = EchoSet()
    win.show()

    sys.exit(app.exec_())


