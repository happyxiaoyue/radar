#!/usr/bin/env python3
# -- coding utf-8 --

from Core.Protocol.EchoLineProtocol import EchoLineProtocol

import sys,os
gRootDir = os.path.join(os.getcwd(), "..", "..")
sys.path.append(gRootDir)
from cfg import gEchoLineCountAFrame
gEchoLineCountAFrame = 2048

class EchoLine():
    """
    回波线内部格式为字典:
    强度1: [ (起点11, 终点11), (起点12, 终点12), (起点13, 终点13), …… ]
    强度2: [ (起点21, 终点21), (起点22, 终点22), (起点23, 终点23), …… ]
    ……
    """
    mData = {}
    def __init__(self, echoLineStr):
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

    def Print(self):
        #print(self.mData)
        print(gEchoLineCountAFrame)

if __name__ == "__main__":
    print("EchoLine 没有测试")

