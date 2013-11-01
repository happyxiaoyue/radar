#!/usr/bin/env python3
# -- coding utf-8 --

from Core.Protocol.EchoLineProtocol import EchoLineProtocol

class EchoLine():
    mData = {}
    def __init__(self, echoLineStr):
        echoLineProtocol = EchoLineProtocol(self)
        echoLineProtocol.ParseEchoLine(echoLineStr)

if __name__ == "__main__":
    print("EchoLine 没有测试")

