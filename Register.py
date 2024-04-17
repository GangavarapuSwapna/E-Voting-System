
from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import sys
import os
from Camera import CaptureImage
class Ui_Register(object):


    def __init__(self,Dialog):
        self.dialog=Dialog

    def getCameraImage(self, event):
        try:
            CaptureImage()
            self.showMessageBox("Information", "Picture Captured..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def registering(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            name = self.lineEdit.text()
            unm = self.lineEdit_2.text()
            pwd = self.lineEdit_3.text()
            email = self.lineEdit_4.text()
            mno = self.lineEdit_5.text()

            if name == "" or name == "null" or unm == "" or unm == "null" or pwd == "" or pwd == "null" or email == "" or email == "null" or mno == "" or mno == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from register where unm='" + unm + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.showMessageBox("Information", "User Name already exists..!")
                else:

                    imgid = str(unm) + ".jpg"
                    path = "../E-Voting/photos/" + str(unm) + "/"
                    if not os.path.exists(os.path.dirname(path)):
                        try:
                            os.makedirs(os.path.dirname(path))
                        except OSError as exc:  # Guard against race condition
                            if exc.errno != exc.errno.EEXIST:
                                raise
                    sql = "insert into register values(%s,%s,%s,%s,%s,%s)"
                    values = (name, unm, pwd, email, mno,imgid)
                    cursor.execute(sql, values)
                    database.commit()
                    imgdata = self.read_file("cameraimg.jpg")
                    self.write_file(imgdata, imgid, path)
                    self.showMessageBox("Information", "Registered Successfully..!")
                    self.dialog.hide()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def read_file(self, filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def write_file(self, data, imgid, path):
        with open(path + imgid, 'wb') as f:
            f.write(data)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(672, 608)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 60, 261, 51))
        self.label.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 75 16pt \"Verdana\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 61, 16))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Gabriola\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 171, 211, 31))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Times New Roman\";\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 230, 101, 16))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Gabriola\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 300, 71, 16))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Gabriola\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 375, 61, 21))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Gabriola\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 460, 71, 20))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Gabriola\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 250, 211, 31))
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Times New Roman\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 320, 211, 31))
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Times New Roman\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 400, 211, 31))
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Times New Roman\";")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 480, 211, 31))
        self.lineEdit_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Times New Roman\";")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 540, 131, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registering)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(410, 180, 231, 321))
        self.label_7.setStyleSheet("image: url(../E-Voting/images/camera.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.mousePressEvent = self.getCameraImage

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registration"))
        self.label.setText(_translate("Dialog", "         Register Here"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "User Name"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.label_5.setText(_translate("Dialog", "Email"))
        self.label_6.setText(_translate("Dialog", "Mobile No."))
        self.pushButton.setText(_translate("Dialog", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Register(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

