import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("TM.exe_404")
        self.resize(1280, 720)
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QIcon("image/logo_tm.png"))

        #call func
        self.createAreaText()
        self.createActionBar()

        self.createMenuBar()



    def createAreaText(self):
        self.AreaText = QTextEdit(self)
        self.AreaText.setGeometry(QtCore.QRect(0,20,1280,720))
        self.AreaText.setStyleSheet("background-color: #333333;"
                                    "color: white;"
                                    "background-image: url(image/bgNotepad.png);"
                                    "background-repeat: no-repeat;"
                                    "background-position: center;"
                                    "border: 2px solid red;"
                                    "font: Bold 20px")

    def createMenuBar(self):
        global cek

        self.cek = 1

        menuBar= self.menuBar()
        self.fileMenu = menuBar.addMenu(QIcon("image/open.png"),"&file")
        self.testMenu = QAction(self)
        self.testMenu.setText("nonAktifkan")
        self.testMenu.triggered.connect(self.checkToolBar)


        self.fileMenu.addAction(self.testMenu)
        self.fileToolBar = self.addToolBar("file")
        self.fileToolBar.setStyleSheet("border:2px solid red;")
        self.fileToolBar.addAction(self.openAction)
        self.fileToolBar.addAction(self.newAction)
        self.fileToolBar.addAction(self.saveAction)
        self.resize(10,10)
        self.fileToolBar.show()

    def createActionBar(self):
        self.openAction = QAction(QIcon("image/folderic.jpg"),"&open",self)
        self.openAction.setText("&Open")
        self.openAction.triggered.connect(self.openFile)
        self.newAction = QAction(QIcon("image/new_ic.jpg"),"&new",self)
        self.newAction.setText("&New")
        self.newAction.triggered.connect(self.newFile)
        self.saveAction = QAction(QIcon("image/save_ic.jpg"),"&save",self)
        self.saveAction.setText("&Save")
        self.saveAction.triggered.connect(self.saveFile)

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self,"Open File","","Text File (*.text *.txt)")
        if filename[0]:
            f = open(filename[0],"r")
            with f:
                data=f.read()
                self.AreaText.setText(data)
                print("data Sudah masuk")

    def newFile(self):
        self.AreaText.setText("")

    def saveFile(self):
        filename = QFileDialog.getSaveFileName(self, "Save File","","Text File (*.text *.txt")
        file = open(filename[0],"w")
        file.write(self.AreaText.toPlainText())

    def checkToolBar(self):
        if self.cek == 1:
            self.fileToolBar.hide()
            self.testMenu.setText("Aktifkan")
            self.fileMenu.setIcon(QIcon("image/close.png"))
            self.cek = 0
        elif self.cek == 0:
            self.fileToolBar.show()
            self.testMenu.setText("NonAktifkan")
            self.fileMenu.setIcon(QIcon("image/open.png"))
            self.cek = 1

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())
