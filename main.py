from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from help import Ui_help
from contact import Ui_contact
import os

class Ui_steganoBuilder(object):
    def tampilanSteganoBuilder(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 395)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_tumbal = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tumbal.setGeometry(QtCore.QRect(60, 90, 411, 20))
        self.lineEdit_tumbal.setObjectName("lineEdit_tumbal")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 551, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("#textBrowser {\n"
"    border: 0;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_namaAkhir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_namaAkhir.setGeometry(QtCore.QRect(10, 250, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_namaAkhir.setFont(font)
        self.lineEdit_namaAkhir.setStyleSheet("#lineEdit_namaAkhir {\n"
"    border: 1px solid #81d4f4;\n"
"    border-radius: 7px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    transition: 2s;\n"
"}\n"
"\n"
"#lineEdit_namaAkhir:hover {\n"
"    border-color: salmon;\n"
"}")
        self.lineEdit_namaAkhir.setObjectName("lineEdit_namaAkhir")
        self.lineEdit_namaGambar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_namaGambar.setGeometry(QtCore.QRect(10, 280, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_namaGambar.setFont(font)
        self.lineEdit_namaGambar.setStyleSheet("#lineEdit_namaGambar {\n"
"    border: 1px solid #81d4f4;\n"
"    border-radius: 7px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    transition: 2s;\n"
"}\n"
"\n"
"#lineEdit_namaGambar:hover {\n"
"    border-color: salmon;\n"
"}")
        self.lineEdit_namaGambar.setObjectName("lineEdit_namaGambar")
        self.lineEdit_namaFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_namaFile.setGeometry(QtCore.QRect(10, 310, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_namaFile.setFont(font)
        self.lineEdit_namaFile.setStyleSheet("#lineEdit_namaFile {\n"
"    border: 1px solid #81d4f4;\n"
"    border-radius: 7px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    transition: 2s;\n"
"}\n"
"\n"
"#lineEdit_namaFile:hover {\n"
"    border-color: salmon;\n"
"}")
        self.lineEdit_namaFile.setObjectName("lineEdit_namaFile")
        self.btn_buildNow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buildNow.setGeometry(QtCore.QRect(230, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btn_buildNow.setFont(font)
        self.btn_buildNow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_buildNow.setStyleSheet("#btn_buildNow {\n"
"    background-color: salmon;\n"
"    color: #ffffff;\n"
"    transition: 0.25s;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#btn_buildNow:hover {\n"
"    background-color: #81d4f4;\n"
"}")
        self.btn_buildNow.setObjectName("btn_buildNow")
        self.btn_buildNow.clicked.connect(self.build)
        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(10, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_help.setStyleSheet("#btn_help {\n"
"    background-color: salmon;\n"
"    color: #ffffff;\n"
"    transition: 0.25s;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#btn_help:hover {\n"
"    background-color: #81d4f4;\n"
"}")
        self.btn_help.setObjectName("btn_help")
        self.btn_help.clicked.connect(self.openHelp)
        self.btn_contact = QtWidgets.QPushButton(self.centralwidget)
        self.btn_contact.setGeometry(QtCore.QRect(440, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btn_contact.setFont(font)
        self.btn_contact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_contact.setStyleSheet("#btn_contact {\n"
"    background-color: salmon;\n"
"    color: #ffffff;\n"
"    transition: 0.25s;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#btn_contact:hover {\n"
"    background-color: #81d4f4;\n"
"}")
        self.btn_contact.setObjectName("btn_contact")
        self.btn_contact.clicked.connect(self.openContact)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def build(self):
        namaFile = self.lineEdit_namaAkhir.text()
        gambar = self.lineEdit_namaGambar.text()
        file = self.lineEdit_namaFile.text()

        code = ("copy /b " + gambar + "+" + file + " " + namaFile)
        self.lineEdit_tumbal.setText(code)
        eksekusi = self.lineEdit_tumbal.text().strip()
        proses = os.popen(eksekusi)
        if proses:
                msg = QMessageBox()
                msg.setWindowTitle("Berhasil")
                msg.setText("Berhasil dibuat, silahkan anda cek hasilnya")
                msg.exec_()

                self.lineEdit_namaAkhir.setText("")
                self.lineEdit_namaGambar.setText("")
                self.lineEdit_namaFile.setText("")
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Gagal")
                msg.setText("Gagal dibuat, silahkan anda cek kembali apa yang salah")
                msg.exec_()
    
    def openHelp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_help()
        self.ui.tampilanHelp(self.window)
        self.window.show()
    
    def openContact(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_contact()
        self.ui.tampilanContact(self.window)
        self.window.show()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganografi Builder"))
        self.label_2.setText(_translate("MainWindow", "Steganografi Builder"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Steganografi adalah sebuah ilmu atau seni menyembunyikan pesan rahasia dengan suatu cara sedemikian sehingga tidak seorang pun yang mengetahui keberadaan pesan tersebut. Tujuan nya yang jelas adalah agar pesan tersebut tidak mudah diketahui oleh banyak orang.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Ada banyak cara agar dapat melakukan steganografi, misalnya kita dapat membuat sebuah kalimat yang dimana terdapat sebuah pesan tersembunyi. Selain dengan cara itu kita juga bisa menyembunyikan sebuah pesan yang sudah kita buat pada file .txt yang akan kita sisipkan pada file .jpg atau .png</span></p></body></html>"))
        self.lineEdit_namaAkhir.setPlaceholderText(_translate("MainWindow", "Nama File Hasil Build"))
        self.lineEdit_namaGambar.setPlaceholderText(_translate("MainWindow", "Nama File Gambar"))
        self.lineEdit_namaFile.setPlaceholderText(_translate("MainWindow", "Nama File Yang Ingin Disisipkan"))
        self.btn_buildNow.setText(_translate("MainWindow", "Build Now"))
        self.btn_help.setText(_translate("MainWindow", "Help"))
        self.btn_contact.setText(_translate("MainWindow", "Contact"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setIconText(_translate("MainWindow", "Help"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_steganoBuilder()
    ui.tampilanSteganoBuilder(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
