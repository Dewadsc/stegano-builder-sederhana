from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QMessageBox

class Ui_contact(object):
    def tampilanContact(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 345)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_website = QtWidgets.QPushButton(self.centralwidget)
        self.btn_website.setGeometry(QtCore.QRect(10, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_website.setFont(font)
        self.btn_website.setStyleSheet("#btn_website {\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"    transition: 2s;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#btn_website:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_website.setObjectName("btn_website")
        self.btn_website.clicked.connect(self.openWebsite)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 551, 192))
        self.textBrowser.setStyleSheet("#textBrowser {\n"
"    border: 0;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.btn_yt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yt.setGeometry(QtCore.QRect(10, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yt.setFont(font)
        self.btn_yt.setStyleSheet("#btn_yt {\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"    transition: 2s;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#btn_yt:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_yt.setObjectName("btn_yt")
        self.btn_yt.clicked.connect(self.openYouTube)
        self.btn_blogger = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blogger.setGeometry(QtCore.QRect(200, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_blogger.setFont(font)
        self.btn_blogger.setStyleSheet("#btn_blogger {\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"    transition: 2s;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#btn_blogger:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_blogger.setObjectName("btn_blogger")
        self.btn_blogger.clicked.connect(self.openBlogger)
        self.btn_wa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_wa.setGeometry(QtCore.QRect(200, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_wa.setFont(font)
        self.btn_wa.setStyleSheet("#btn_wa {\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"    transition: 2s;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#btn_wa:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_wa.setObjectName("btn_wa")
        self.btn_wa.clicked.connect(self.openWhatsApp)
        self.btn_email1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_email1.setGeometry(QtCore.QRect(400, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_email1.setFont(font)
        self.btn_email1.setStyleSheet("#btn_email1 {\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"    transition: 2s;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#btn_email1:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_email1.setObjectName("btn_email1")
        self.btn_email1.clicked.connect(self.email1)
        self.btn_email2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_email2.setGeometry(QtCore.QRect(400, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_email2.setFont(font)
        self.btn_email2.setStyleSheet("#btn_email2 {\n"
"    background-color: #81d4f4;\n"
"    color: #ffffff;\n"
"    transition: 2s;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#btn_email2:hover {\n"
"    background-color: salmon;\n"
"}")
        self.btn_email2.setObjectName("btn_email2")
        self.btn_email2.clicked.connect(self.email2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openWebsite(self):
        self.web = QWebEngineView()
        self.web.load(QUrl("https://dstartup.000webhostapp.com"))
        self.web.show()
    
    def openYouTube(self):
        self.web = QWebEngineView()
        self.web.load(QUrl("https://www.youtube.com/channel/UCtS2N4D_UYa_yhFAZNEGHMg"))
        self.web.show()
    
    def openBlogger(self):
        self.web = QWebEngineView()
        self.web.load(QUrl("https://dstartup0.blogspot.com"))
        self.web.show()
    
    def openWhatsApp(self):
        self.web = QWebEngineView()
        self.web.load(QUrl("http://wa.me/6285891304086"))
        self.web.show()
    
    def email1(self):
        msg = QMessageBox()
        msg.setWindowTitle("Email Pertama")
        msg.setText("Email : dstartup_a@protonmail.com")
        msg.exec_()
    
    def email2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Email Kedua")
        msg.setText("Email : dstartup0@gmail.com")
        msg.exec_()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact"))
        self.label_3.setText(_translate("MainWindow", "Contact"))
        self.btn_website.setText(_translate("MainWindow", "Website"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Jika ada yang salah atau ada yang kurang dari program ini silahkan kalian kirim ke kontak gw bro, dibawah gw dah sediain. Ada link website, yt, wa, dan juga blogger gw juga bro. Jangan lupa download juga program yang lainnya dari D\'Startup dengan cara cek melalui website D\'Startup atau cek di chanel yt D\'Startup.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Jika ada yang kurang paham dengan cara penggunaan dari program ini silahkan kalian bisa baca melalui menu help atau japri gw bro.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Terima kasih buat yang udah download program sederhana gw ini bro.</span></p></body></html>"))
        self.btn_yt.setText(_translate("MainWindow", "YouTube"))
        self.btn_blogger.setText(_translate("MainWindow", "Blogger"))
        self.btn_wa.setText(_translate("MainWindow", "WhatsApp"))
        self.btn_email1.setText(_translate("MainWindow", "Email 1"))
        self.btn_email2.setText(_translate("MainWindow", "Email 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_contact()
    ui.tampilanContact(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
