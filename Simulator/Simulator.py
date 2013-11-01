#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLabel

import sys,os
gRootDir = os.path.join(os.getcwd(), "..")
sys.path.append(gRootDir)
from Core.Widget.EchoWidget import EchoWidget
from Simulator.CtrlWidget import CtrlWidget

class Simulator(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.mLayout = QHBoxLayout()

        self.mEchoWidget = EchoWidget();
        self.mCtrlWidget = CtrlWidget();

        self.mLayout.addWidget(self.mEchoWidget)
        self.mLayout.addWidget(self.mCtrlWidget)
        self.setLayout(self.mLayout)

        self.mCtrlWidget.msPlayAFrame.connect(self.mEchoWidget.PlayAFrame)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = Simulator()
    win.show()

    sys.exit(app.exec_())


