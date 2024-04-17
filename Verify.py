from PyQt5 import QtCore, QtGui, QtWidgets
from Camera1 import CaptureImage
from VoterHome import Ui_VoterHome
import os
#from Home import Home
from predict import face_recognition,predict,show_prediction_labels_on_image,train
import datetime
class Ui_Verify(object):

    unmlist=[]
    def __init__(self,Dialog,unm):
        self.dialog=Dialog
        self.unm=unm
    def getCameraImage(self,event):
        try:
            CaptureImage()
            self.showMessageBox("Information", "Picture Captured..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def submit(self):
        try:

            namelist = []
            namelist.clear()

            print("Training KNN classifier...")
            classifier = train("../E-Voting/photos", model_save_path="trained_knn_model.clf", n_neighbors=1)
            print("Training complete!")

            # STEP 2: Using the trained classifier, make predictions for unknown images
            for image_file in os.listdir("../E-Voting/test"):
                full_file_path = os.path.join("../E-Voting/test", image_file)

                print("Looking for faces in {}".format(image_file))

                # Find all people in the image using a trained classifier model
                # Note: You can pass in either a classifier file name or a classifier model instance
                predictions = predict(full_file_path, model_path="trained_knn_model.clf")

                # Print results on the console
                for name, (top, right, bottom, left) in predictions:



                    if(str(name.strip())==str(self.unm.strip())):

                        self.showMessageBox("Information", "Authorized..!")
                        print("authen")

                        self.vh = QtWidgets.QDialog()
                        self.ui = Ui_VoterHome(self.unm)
                        self.ui.setupUi(self.vh)
                        self.vh.show()
                        self.dialog.hide()
                    else:
                        self.showMessageBox("Information", "Not Authorized..!")

                # Display results overlaid on an image
                #show_prediction_labels_on_image(os.path.join("../E-Voting/test", image_file), predictions)

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)


    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 503)
        Dialog.setStyleSheet("background-color: rgb(200, 129, 152);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 50, 201, 31))
        self.label.setStyleSheet("font: 75 16pt \"Vani\";")
        self.label.setObjectName("label")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(210, 120, 161, 121))
        self.camera.setStyleSheet("image: url(../E-Voting/images/camera.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent=self.getCameraImage
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 250, 181, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 350, 121, 41))
        self.pushButton.setStyleSheet("font: 75 12pt \"Vani\";\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Verification"))
        self.label.setText(_translate("Dialog", "Face Authentication"))
        self.label_5.setText(_translate("Dialog", "Click on Camera"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        #self.pushButton_2.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Verify()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

