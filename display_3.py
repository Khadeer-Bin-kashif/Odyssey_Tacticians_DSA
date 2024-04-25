from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class Ui_Dialog_3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog")
        Dialog3.resize(1169, 850)
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(0, 0, 1171, 851))
        self.label.setStyleSheet("background-image: url(:/newPrefix/Screenshot (1).png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Screenshot (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog3)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 220, 861, 491))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(280, 110, 621, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog3)
        self.pushButton.setGeometry(QtCore.QRect(1000, 770, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog3.close)

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)


    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog", "Odyssey Tactician"))
        self.label_2.setText(_translate("Dialog", "The most optimal route for you is:"))
        self.pushButton.setText(_translate("Dialog", "END"))

    def display(self, held, greed):
        result_text = f"<h2>Held-Karp Result:</h2><p>{held}</p><h2>Greedy Result:</h2><p>{greed}</p>"
        self.ui.textBrowser_2.setHtml(result_text)

    def set_text_content(self, content):
        self.textBrowser_2.setText(content)
        

import map_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())