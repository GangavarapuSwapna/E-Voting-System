

from PyQt5 import QtCore, QtGui, QtWidgets
from Voting import Ui_Voting
from Results import Ui_Results
class Ui_VoterHome(object):

    def __init__(self,unm):
        self.unm=unm

    def voting(self):
        self.vote = QtWidgets.QDialog()
        self.ui = Ui_Voting(self.vote, self.unm)
        self.ui.setupUi(self.vote)
        self.ui.nominelist()
        self.vote.show()
    def results(self):

        self.res = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.res)
        self.ui.viewres()
        self.res.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 418)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 201, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.voting)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 200, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.results)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "VoterHome"))
        self.pushButton.setText(_translate("Dialog", "Voting"))
        self.pushButton_3.setText(_translate("Dialog", "Results"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_VoterHome("aliya")
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

