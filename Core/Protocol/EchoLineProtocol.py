#!/usr/bin/env python3
# -- coding utf-8 --

class EchoLineProtocol():
    """
    回波文件中每行代表一条回波线,一条回波线有多个回波段
    每个回波段的的格式为:
    强度(1Byte) 空格 起点(低Byte) 空格 起点(高Byte)) 空格 终点(低Byte) 空格 终点(高Byte)
    """
    def __init__(self, echoLine):
        self.mEchoLine = echoLine

    def ParseEchoLine(self, echoLineStr):
        segStrLength = 15

        echoLineStrLength = len(echoLineStr)
        iMax = echoLineStrLength - 1
        #print("echoLineStr:" + echoLineStr)
        i = 0
        echoSegStr = []
        while i < iMax:
            echoSegStr = echoLineStr[i:i+segStrLength]
            self.ParseEchoSeg(echoSegStr)
            i += segStrLength

    def ParseEchoSeg(self, echoSegStr):
        #print("echoSegStr:" + echoSegStr)

        strengthStr = echoSegStr[0] + echoSegStr[1]
        strength = int(strengthStr, base = 16)
        #print("strengthStr:" + strengthStr)
        #print("strength:%d" % strength)

        startStr = echoSegStr[6] + echoSegStr[7] + echoSegStr[3] + echoSegStr[4]
        start = int(startStr, base = 16)
        #print("startStr:" + startStr)
        #print("start:%d" % start)

        endStr = echoSegStr[12] + echoSegStr[13] + echoSegStr[9] + echoSegStr[10]
        end = int(endStr, base = 16)
        #print("endStr:" + endStr)
        #print("end:%d" % end)
        self.mEchoLine.AddSeg(strength, start, end)

if __name__ == "__main__":
    print("EchoLine 没有测试")

