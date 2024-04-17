

from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_Admin
from User import Ui_User
import sys
class Ui_Dialog(object):

    def adminlogin(self,event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Admin(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def voterlogin(self,event):
        try:
            self.usr = QtWidgets.QDialog()
            self.ui = Ui_User( self.usr)
            self.ui.setupUi(self.usr)
            self.usr.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 448)
        Dialog.setStyleSheet("background-color: rgb(85, 0, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 681, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Vani\";")
        self.label.setObjectName("label")
        self.faculty = QtWidgets.QLabel(Dialog)
        self.faculty.setGeometry(QtCore.QRect(380, 140, 241, 161))
        self.faculty.setStyleSheet("image: url(../E-Voting/images/voters.png);")
        self.faculty.setText("")
        self.faculty.setObjectName("faculty")
        self.faculty.mousePressEvent = self.voterlogin
        self.admin = QtWidgets.QLabel(Dialog)
        self.admin.setGeometry(QtCore.QRect(60, 150, 271, 151))
        self.admin.setStyleSheet("image: url(../E-Voting/images/adminn.png);")
        self.admin.setText("")
        self.admin.setObjectName("admin")
        self.admin.mousePressEvent=self.adminlogin
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 320, 121, 31))
        self.label_2.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(460, 320, 121, 31))
        self.label_3.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "E-Voting"))
        self.label.setText(_translate("Dialog", "       Online Voting on Face Recognition"))
        self.label_2.setText(_translate("Dialog", "Admin"))
        self.label_3.setText(_translate("Dialog", "Voter"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

