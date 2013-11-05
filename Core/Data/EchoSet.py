#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter

from PyQt4.QtCore import QPoint
from PyQt4.QtCore import Qt

import math

import sys,os
gRootDir = os.path.join(os.getcwd(), "..", "..")
sys.path.append(gRootDir)
from Core.Data.EchoLine import EchoLine
from cfg import gEchoLineCountAFrame
from cfg import gPI
from cfg import gRangeTable
from cfg import gRadarEchoScale

class EchoSet(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mCenter = QPoint(0, 0)
        self.mRadius = 0
        self.mEchoLines = []

        self.SetCenter(QPoint(0,0))
        self.SetRadius(0)
        self.SetRange("50m")
        self.SetHdt(0)

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

    # 绘制时的圆心坐标
    def SetCenter(self, center):
        self.mCenter = center;

    # 绘制半径
    def SetRadius(self, radius):
        self.mRadius = radius * gRadarEchoScale

    # 设置量程
    def SetRange(self, radarRange):
        assert radarRange in gRangeTable, "量程表中没有量程:" + radarRange
        self.mRangeName = radarRange
        self.mRange = gRangeTable[radarRange][0]
        self.mPrecision = gRangeTable[radarRange][1]

    # 设置船艏向
    def SetHdt(self, hdt):
        self.mHdt = 0

    # 绘制
    def Draw(self, p):
        self.__DrawEchoLines(p)
        self.__DrawShipHeadLine(p)
        self.__DrawDisCircle(p)
        self.__DrawRangeCicle(p)
        self.__DrawSysInfo(p)

    # 绘制量程范围
    def __DrawRangeCicle(self, p):
        pen = QPen(QColor(0, 255, 0))
        p.setPen(pen)

    # 绘制距标圈
    def __DrawDisCircle(self, p):
        pen = QPen(QColor(0, 150, 0))
        p.setPen(pen)
        p.setBrush(Qt.NoBrush)

        r = self.mRadius
        rHalf = 0.5 * r
        rHalfOne = 1.5 * r
        self.__DrawCircle(p, self.mCenter, r)
        self.__DrawCircle(p, self.mCenter, rHalf)
        self.__DrawCircle(p, self.mCenter, rHalfOne)

    # 绘制船艏线
    def __DrawShipHeadLine(self, p):
        pen = QPen(QColor(255, 255, 255))
        p.setPen(pen)

        xStart = int(self.mCenter.x())
        yStart = int(self.mCenter.y())
        xEnd = int(self.mRadius * math.cos(self.mHdt - gPI / 2) + xStart)
        yEnd = int(self.mRadius * math.sin(self.mHdt - gPI / 2) + yStart)

        p.drawLine(xStart, yStart, xEnd, yEnd) 

        brush = QBrush(QColor(255, 255, 255), Qt::SolidPattern);
        p->setBrush(brush);
        
        """
        double ang = angle - 30 * DI_1_DEG;
        cos_a = cos(ang);
        sin_a = sin(ang);
        double x1 = x_end + SHIP_LEGEND_LEN * cos_a;
        double y1 = y_end - SHIP_LEGEND_LEN* sin_a;
        ang = angle + 30 * DI_1_DEG;
        cos_a = cos(ang);
        sin_a = sin(ang);
        double x2 = x_end + SHIP_LEGEND_LEN * cos_a;
        double y2 = y_end - SHIP_LEGEND_LEN* sin_a;
        QPointF ptx[3];
        ptx[0].setX(x1);   ptx[0].setY(y1);
        ptx[1].setX(x2);   ptx[1].setY(y2);
        ptx[2].setX(x_end); ptx[2].setY(y_end);
        p->drawPolygon( ptx, 3);
        """

    # 绘制系统信息
    def __DrawSysInfo(self, p):
        pen = QPen(QColor(0, 255, 0))
        p.setPen(pen)
        p.drawText(2, 20, "量程:" + self.mRangeName)
        p.drawText(2, 40, "船艏:" + str(self.mHdt) + "度")

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

    def __DrawCircle(self, p, center, r):
        x = center.x() - r
        y = center.y() - r

        width = 2 * r
        height = 2 * r

        p.drawEllipse(x, y, width, height)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = EchoSet()
    win.show()

    sys.exit(app.exec_())


