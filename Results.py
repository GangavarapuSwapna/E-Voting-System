
from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import sys
class Ui_Results(object):

    def viewres(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("SELECT NAME,symbol,vcnt FROM voting WHERE vcnt=(SELECT MAX(vcnt) FROM voting)")
            row = cursor.fetchall()
            for r in row:
                self.nm.setText(r[0])
                self.symbl.setText(r[1])
                self.vcnt.setText(str(r[2]))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)





    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 356)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 120, 151, 51))
        self.label.setStyleSheet("font: 14pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.label_2.setStyleSheet("font: 14pt \"Franklin Gothic Heavy\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 125, 161, 41))
        self.label_3.setStyleSheet("font: 14pt \"Franklin Gothic Heavy\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 131, 41))
        self.label_4.setStyleSheet("font: 14pt \"Franklin Gothic Heavy\";\n"
"color: rgb(85, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.nm = QtWidgets.QLabel(Dialog)
        self.nm.setGeometry(QtCore.QRect(50, 170, 161, 61))
        self.nm.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.nm.setObjectName("nm")
        self.symbl = QtWidgets.QLabel(Dialog)
        self.symbl.setGeometry(QtCore.QRect(280, 170, 161, 61))
        self.symbl.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.symbl.setObjectName("symbl")
        self.vcnt = QtWidgets.QLabel(Dialog)
        self.vcnt.setGeometry(QtCore.QRect(470, 170, 131, 61))
        self.vcnt.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.vcnt.setObjectName("vcnt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Results"))
        self.label.setText(_translate("Dialog", "Nominee Name"))
        self.label_2.setText(_translate("Dialog", "Symbol"))
        self.label_3.setText(_translate("Dialog", "No.of Votes"))
        self.label_4.setText(_translate("Dialog", "Results"))
        self.nm.setText(_translate("Dialog", "TextLabel"))
        self.symbl.setText(_translate("Dialog", "TextLabel"))
        self.vcnt.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Results()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

