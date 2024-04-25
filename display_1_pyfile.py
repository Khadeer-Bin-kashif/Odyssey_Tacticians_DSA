
from PyQt5 import QtCore, QtGui, QtWidgets
from display_2_pyfile import Ui_Dialog_2
import DSA_proj
from display_3 import Ui_Dialog_3


class Ui_Dialog_1(object):
    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_2()
        self.ui.setupUi(self.window, Dialog1)
        self.window.show()
        Dialog1.hide()

    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Odyssey Tactician")
        Dialog1.resize(1093, 844)
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 871))
        self.label.setStyleSheet("background-image: url(:/newPrefix/Screenshot (1).png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Screenshot (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(240, 530, 631, 101))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(210, 640, 681, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog1, clicked= lambda: self.open_window())
        self.pushButton.setGeometry(QtCore.QRect(460, 740, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

        self.pushButton.clicked.connect(self.open_window)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Odyssey Tactician"))
        self.label_2.setText(_translate("Dialog1", "Odyssey Tactician"))
        self.label_3.setText(_translate("Dialog1", "Your ultimate travelling salesman solution"))
        self.pushButton.setText(_translate("Dialog1", "Click Here"))
    
    def push(self):
        self.pushButton.clicked.connect(lambda: self.ui.extract_from_graph(DSA_proj.graph))


    

import map_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Dialog_1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())
