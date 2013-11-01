#!/usr/bin/env python3
# -- coding utf-8 --

class EchoLineProtocol():
    """
    回波文件中每行代表一条回波线,一条回波线有多个回波段
    每个回波段的的格式为:
    强度(1Byte) 空格 起点(低Byte) 空格 起点(高Byte)) 空格 终点(低Byte) 空格 终点(高Byte)
    """
    """
    回波线内部格式为字典:
    强度1: [ (起点11, 终点11), (起点12, 终点12), (起点13, 终点13), …… ]
    强度2: [ (起点21, 终点21), (起点22, 终点22), (起点23, 终点23), …… ]
    ……
    """
    def __init__(self, echoLine):
        self.mEchoLine = echoLine

    def ParseEchoLine(self, echoLineStr):
        i = 0
        echoSegStr = []
        echoSegStr = echoLineStr[i:i+15]
        print(echoSegStr)

        strengthStr = echoSegStr[0] + echoSegStr[1]
        strength = int(strengthStr, base = 16)
        print(strength)
        """
        for c in echoLineStr:
            print(c)

        """
        print(echoLineStr)
        exit()

if __name__ == "__main__":
    print("EchoLine 没有测试")

