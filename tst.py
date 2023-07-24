from msilib.schema import Directory
from tkinter import Image, Widget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_main(object):
    def tampilanmain(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 250, 461, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 551, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 280, 461, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 310, 461, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.btn_pilih_gambar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pilih_gambar.setGeometry(QtCore.QRect(480, 250, 81, 21))
        self.btn_pilih_gambar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pilih_gambar.setStyleSheet("#btn_pilih_gambar {\n"
"    border-radius: 5px;\n"
"    transition: 0.25s;\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#btn_pilih_gambar:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_pilih_gambar.setObjectName("btn_pilih_gambar")
        self.btn_pilih_gambar.clicked.connect(self.pilihGambar)
        self.btn_pilih_file_sisip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pilih_file_sisip.setGeometry(QtCore.QRect(480, 280, 81, 21))
        self.btn_pilih_file_sisip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pilih_file_sisip.setStyleSheet("#btn_pilih_file_sisip {\n"
"    border-radius: 5px;\n"
"    transition: 0.25s;\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#btn_pilih_file_sisip:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_pilih_file_sisip.setObjectName("btn_pilih_file_sisip")
        self.btn_pilih_file_sisip.clicked.connect(self.pilihFile)
        self.btn_pilih_file_akhir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pilih_file_akhir.setGeometry(QtCore.QRect(480, 310, 81, 21))
        self.btn_pilih_file_akhir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pilih_file_akhir.setStyleSheet("#btn_pilih_file_akhir {\n"
"    transition: 0.25s;\n"
"    background-color: salmon;\n"
"    color: #ffffff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#btn_pilih_file_akhir:hover {\n"
"    background-color: #81d4f4;\n"
"}")
        self.btn_pilih_file_akhir.setObjectName("btn_pilih_file_akhir")
        self.btn_pilih_file_akhir.clicked.connect(self.pilihFolder)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pilihGambar(self):
        lokasiGambar = QFileDialog.getOpenFileName()
        self.lineEdit.setText(lokasiGambar[0])
    
    def pilihFile(self):
        lokasiFile = QFileDialog.getOpenFileName()
        self.lineEdit_2.setText(lokasiFile[0])
    
    def pilihFolder(self):
        url = QFileDialog.getExistingDirectory()
        if url:
            self.lineEdit_3.setText(url)
        else:
            print("Gagal")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganografi Builder"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Gambar yang akan disisipkan pesan"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Steganografi adalah sebuah ilmu atau seni menyembunyikan pesan rahasia dengan suatu cara sedemikian sehingga tidak seorang pun yang mengetahui keberadaan pesan tersebut. Tujuan nya yang jelas adalah agar pesan tersebut tidak mudah diketahui oleh banyak orang.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Ada banyak cara agar dapat melakukan steganografi, misalnya kita dapat membuat sebuah kalimat yang dimana terdapat sebuah pesan tersembunyi. Selain dengan cara itu kita juga bisa menyembunyikan sebuah pesan yang sudah kita buat pada file .txt yang akan kita sisipkan pada file .jpg atau .png</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Steganografi Builder"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "File yang ingin di sembunyikan"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Hasil akhir"))
        self.btn_pilih_gambar.setText(_translate("MainWindow", "Open File"))
        self.btn_pilih_file_sisip.setText(_translate("MainWindow", "Open File"))
        self.btn_pilih_file_akhir.setText(_translate("MainWindow", "Select Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.tampilanmain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())