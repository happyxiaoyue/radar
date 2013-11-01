#!/usr/bin/env python3
# -- coding utf-8 --

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLabel

class LabelWithLineEditWidget(QWidget):
    def __init__(self, parent=None, labelStr="待写入标签", lineStr="待写入内容"):
        QWidget.__init__(self, parent)

        self.mLayout = QHBoxLayout()

        self.mLabel = QLabel(labelStr)
        self.mLabel.setFixedWidth(150)
        self.mLineEdit = QLineEdit(lineStr)
        self.mLineEdit.setFixedWidth(80)
        self.mLineEdit.setReadOnly(True)

        self.mLayout.addWidget(self.mLabel)
        self.mLayout.addWidget(self.mLineEdit)
        self.setLayout(self.mLayout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = LabelWithLineEditWidget()
    win.show()

    sys.exit(app.exec_())


