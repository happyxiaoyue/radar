#!/usr/bin/env python3
# -- coding utf-8 --

import math

from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor

from Core.Protocol.EchoLineProtocol import EchoLineProtocol

class EchoLine():
    """
    回波线内部格式为字典:
    强度1: [ (起点11, 终点11), (起点12, 终点12), (起点13, 终点13), …… ]
    强度2: [ (起点21, 终点21), (起点22, 终点22), (起点23, 终点23), …… ]
    ……
    """
    def __init__(self, echoLineStr):
        self.mData = {}
        echoLineProtocol = EchoLineProtocol(self)
        echoLineProtocol.ParseEchoLine(echoLineStr)

    def AddSeg(self, strength, start, end):
        posPair = (start, end)

        if strength not in self.mData:
            """
            第一次出现的强度值 需要初始化列表
            """
            self.mData[strength] = []

        self.mData[strength].append(posPair)

    def Draw(self, p, center, radius, cosAngle, sinAngle, radarRange, precision):
        pointAEchoLine = radarRange / precision
        rStep = radius / pointAEchoLine
        for strength in self.mData:
            assert 0 <= strength <= 255, "强度值必须在0,255之间"
            for seg in self.mData[strength]:
                start = seg[0]
                end = seg[1]

                rStart = rStep * start
                xStart = int(rStart * cosAngle + center.x())
                yStart = int(rStart * sinAngle + center.y())

                rEnd = rStep * end
                xEnd = int(rEnd * cosAngle + center.x())
                yEnd = int(rEnd * sinAngle+ center.y())
                
                # TODO: 使用彩色
                pen = QPen(QColor(0, strength, 0))
                p.setPen(pen)
                p.drawLine(xStart, yStart, xEnd, yEnd)
                #print("%d:(%f, %f) => (%f, %f)" % (strength, xStart, yStart, xEnd, yEnd))

    def Print(self):
        print(self.mData)


if __name__ == "__main__":
    print("EchoLine 没有测试")

