#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QTabWidget
from PyQt4.QtGui import QLabel

from Assistant.Assistant import Assistant
from Simulator.Simulator import Simulator

class RadarTool(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)

        self.mSimulator = Simulator()
        self.mAssistant = Assistant()
        self.mEchoEditer = QLabel("回波编辑 控件")

        self.addTab(self.mSimulator, "模拟器")
        self.addTab(self.mAssistant, "调试助手")
        self.addTab(self.mEchoEditer, "回波编辑")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = RadarTool()
    win.show()

    sys.exit(app.exec_())


