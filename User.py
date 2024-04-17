
from PyQt5 import QtCore, QtGui, QtWidgets
from Register import Ui_Register
from DBConnection import DBConnection
import sys
from Verify import Ui_Verify
class Ui_User(object):

    def __init__(self, Dialog):
        self.dialog = Dialog

    def register(self,event):
        try:
            self.reg = QtWidgets.QDialog()
            self.ui = Ui_Register(self.reg)
            self.ui.setupUi(self.reg)
            self.reg.show()
            event.accept()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def login(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            unm = self.lineEdit.text()
            pwd = self.lineEdit_2.text()
            if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from register where unm='" + unm + "' and pwd='" + pwd + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.verfy = QtWidgets.QDialog()
                    self.ui = Ui_Verify(self.verfy,unm)
                    self.ui.setupUi(self.verfy)
                    self.verfy.show()
                    self.dialog.hide()
                else:
                    self.showMessageBox("Information", "Invalid Credentials..!")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 480)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 60, 251, 51))
        self.label.setStyleSheet("font: 16pt \"Verdana\";\n"
"color: rgb(85, 85, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 150, 151, 21))
        self.label_2.setStyleSheet("color: rgb(85, 85, 127);\n"
"font: 75 14pt \"Vani\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 180, 221, 31))
        self.lineEdit.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 240, 221, 21))
        self.label_3.setStyleSheet("color: rgb(85, 85, 127);\n"
"font: 75 14pt \"Vani\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 270, 221, 31))
        self.lineEdit_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(204, 330, 101, 41))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 110, 181, 231))
        self.label_4.setStyleSheet("image: url(../E-Voting/images/userr.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.register_2 = QtWidgets.QLabel(Dialog)
        self.register_2.setGeometry(QtCore.QRect(470, 330, 121, 51))
        self.register_2.setStyleSheet("image: url(../E-Voting/images/regg.png);")
        self.register_2.setText("")
        self.register_2.setObjectName("register_2")
        self.register_2.mousePressEvent=self.register


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voter Login"))
        self.label.setText(_translate("Dialog", "        Voter Login"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">ASASA</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Login"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_User()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

