#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter

from PyQt4.QtCore import QPoint

import math

import sys,os
gRootDir = os.path.join(os.getcwd(), "..", "..")
sys.path.append(gRootDir)
from Core.Data.EchoLine import EchoLine
from cfg import gEchoLineCountAFrame
from cfg import gPI
from cfg import gRangeTable

class EchoSet(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mCenter = QPoint(0, 0)
        self.mRadius = 0
        self.mEchoLines = []
        
        # 制作回波线角度表，用于提升性能
        step = 2.0 * gPI / gEchoLineCountAFrame
        self.mCosAngleTable = []
        self.mSinAngleTable = []
        for i in range(0, gEchoLineCountAFrame):
            self.mCosAngleTable.append(0)
            self.mSinAngleTable.append(0)
        for i in range(0, gEchoLineCountAFrame):
            self.mCosAngleTable[i] = math.cos(i * step)
            self.mSinAngleTable[i] = math.sin(i * step)

    def SetData(self, echoSetStrs):
        for echoStr in echoSetStrs:
            echoLine = EchoLine(echoStr)
            self.mEchoLines.append(echoLine)
        self.update()

    def SetCenter(self, center):
        self.mCenter = center;

    def SetRadius(self, radius):
        self.mRadius = radius;

    def SetRange(self, radarRange):
        assert radarRange in gRangeTable, "量程表中没有量程:" + radarRange
        self.mRangeName = radarRange
        self.mRange = gRangeTable[radarRange][0]
        self.mPrecision = gRangeTable[radarRange][1]

    # 回波绘制
    def Draw(self, p):
        pen = QPen(QColor(255, 255, 255))
        p.setPen(pen)
        p.drawText(50, 50, "Draw")

        self.__DrawEchoLines(p)

        self.__DrawDisCircle(p)
        self.__DrawRangeCicle(p)
        self.__DrawShipHeadLine(p)
        self.__DrawSysInfo(p)

    def paintEvent(self, paintEvent):
        p = QPainter(self)
        self.Draw(p)
        
    # 绘制量程范围
    def __DrawRangeCicle(self, p):
        pen = QPen(QColor(0, 255, 0))
        p.setPen(pen)
        p.drawText(20, 20, self.mRangeName)
    
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

    # 绘制回波
    def __DrawEchoLines(self, p):
        i = 0
        for echoLine in self.mEchoLines:
            # TODO: 使用查表法 提速
            cosAngle = self.mCosAngleTable[i]
            sinAngle = self.mSinAngleTable[i]
            echoLine.Draw(p, self.mCenter, self.mRadius, cosAngle, sinAngle, self.mRange, self.mPrecision)
            print(str(i) + ":")
            #print(cosAngle)
            #print(sinAngle)
            #print()
            i += 1

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = EchoSet()
    win.show()

    sys.exit(app.exec_())


