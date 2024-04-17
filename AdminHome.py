

from PyQt5 import QtCore, QtGui, QtWidgets
from AddNominee import Ui_AddNominee
from ViewNominee import Ui_ViewNominee
from Results import Ui_Results
class Ui_AdminHome(object):

    def __init__(self, Dialog):
        self.dialog = Dialog

    def addnomine(self):
        try:
            self.adnm = QtWidgets.QDialog()
            self.ui1 = Ui_AddNominee()
            self.ui1.setupUi(self.adnm)
            self.adnm.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewnomine(self):
        try:
            self.viewnm = QtWidgets.QDialog()
            self.ui1 = Ui_ViewNominee()
            self.ui1.setupUi(self.viewnm)
            self.ui1.details()
            self.viewnm.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def results(self):

        self.res = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.res)
        self.ui.viewres()
        self.res.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 418)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 90, 201, 41))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addnomine);
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 170, 201, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.viewnomine);
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 250, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.results);

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Add Nominee"))
        self.pushButton_2.setText(_translate("Dialog", "View Nominees"))
        self.pushButton_3.setText(_translate("Dialog", "Results"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

