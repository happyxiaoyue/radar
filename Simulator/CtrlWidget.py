#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QGroupBox
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLabel

from PyQt4.QtCore import pyqtSignal

import re
import sys,os
gRootDir = os.path.join(os.getcwd(), "..")
sys.path.append(gRootDir)
from Core.Widget.LabelWithLineEditWidget import LabelWithLineEditWidget

gCfgNameEchoFileStr = "回波文件"
gCfgName = "para.cfg"
gParrern = r"^([\S]*)[\s]*=[\s]*(.*)$"

class CtrlWidget(QWidget):
    msPlayAFrame = pyqtSignal(str, name='msPlayAFrame')

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.mLayout = QVBoxLayout()
        self.mInfoLayout = QVBoxLayout()
        self.mButtonLayout = QHBoxLayout()
        self.mPlayAFrameButton = QPushButton("放映一帧")
        self.mRunButton = QPushButton("运行")

        self.mInfograoupBox = QGroupBox("链路信息")
        self.GetALabelWithLineEditWidgets()

        for widget in self.mWidgets: 
            self.mInfoLayout.addWidget(widget)

        self.mInfograoupBox.setLayout(self.mInfoLayout)
        self.mButtonLayout.addWidget(self.mPlayAFrameButton)
        self.mButtonLayout.addWidget(self.mRunButton)

        self.mLayout.addWidget(self.mInfograoupBox)
        self.mLayout.addStretch()
        self.mLayout.addLayout(self.mButtonLayout)

        self.setLayout(self.mLayout)

        self.mPlayAFrameButton.clicked.connect(self.PlayAFrameButtonSlot)

    def GetALabelWithLineEditWidgets(self):
        cfgFile = open(gCfgName, "r", encoding = "utf8")
        self.mWidgets = []

        for line in cfgFile:
            #print(line) 

            p = re.compile(gParrern)
            m = p.match(line)

            #print(m.group(1))
            #print(m.group(2))

            labelStr = m.group(1) + "："
            lineEditStr = m.group(2)
            widget = LabelWithLineEditWidget(self, labelStr, lineEditStr)
            self.mWidgets.append(widget)
            
        cfgFile.close()

    def PlayAFrameButtonSlot(self):
        echoFileName = self.GetEchoFileName()
        self.PlayAFrame(echoFileName)
     
    def PlayAFrame(self, echoFileName):
        self.msPlayAFrame.emit(echoFileName)

    def GetEchoFileName(self):
        rst = None

        cfgFile = open(gCfgName, "r", encoding = "utf8")

        for line in cfgFile:
            p = re.compile(gParrern)
            m = p.match(line)

            labelStr = m.group(1)
            lineEditStr = m.group(2)
            if gCfgNameEchoFileStr == labelStr:
                rst = lineEditStr

        cfgFile.close()
        if None == rst:
            assert 0, gCfgName + "中找不到回波文件的配置"

        return rst

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = CtrlWidget()
    win.show()

    sys.exit(app.exec_())


