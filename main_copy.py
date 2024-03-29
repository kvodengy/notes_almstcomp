# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

notes = []




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(773, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 441, 521))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 10, 81, 16))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(460, 30, 301, 161))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 200, 141, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 200, 141, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 230, 301, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 260, 71, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(460, 280, 301, 161))
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 450, 301, 20))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 510, 301, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 480, 141, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 480, 141, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget.itemClicked.connect(self.show_note)
        self.pushButton.clicked.connect(self.add_note)
        self.pushButton_3.clicked.connect(self.save_text)
        
        

    def show_note(self):
        key = self.listWidget.selectedItems()[0].text()
        for note in notes:
            if note[0] == key:
                self.textEdit.setText(notes[1])
                self.listWidget_2.clear()
                self.listWidget_2.addItems(notes[2])

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.pushButton.setText(_translate("MainWindow", "Створити замітку"))
        self.pushButton_2.setText(_translate("MainWindow", "Видалити замітку"))
        self.pushButton_3.setText(_translate("MainWindow", "Зберегти  замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", "Шукати замітки по тегу"))
        self.pushButton_5.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.pushButton_6.setText(_translate("MainWindow", "Додати до замітки"))

    def add_note(self):
        name, ok = QtWidgets.QInputDialog.getText(self.centralwidget,"Додати замітку", "Назва замітки")
        if name != "" and ok:
            note = [name,"",[]]
            notes.append(note)
            self.listWidget.addItem(name)
            self.listWidget_2.addItems(note[2])
            with open(str(len(notes)-1)+".txt", "w", encoding="utf-8") as file:
                file.write(note[0]+"\n")



    def save_text(self):
        if self.listWidget.selectedItems():
            key = self.listWidget.selectedItems()[0].text()
            i = 0
            for note in notes:
                if note[0] == key:
                    note[1]=self.textEdit.toPlainText()
                with open(str(i)+".txt", "w", encoding="utf-8") as file:
                    file.write(note[0]+"\n")
                    file.write(note[1]+"\n")
                    for tag in note[2]:
                        file.write(tag + " ")
                    file.write("\n")
            i+=1
        else:
            win = QtWidgets.QMessageBox()
            win.setText("Не обрана замітка для збереження")
            win.exec()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    name = 0
    note = []
    while True:
        filename = str(name)+".txt"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.replace("\n", "")
                    note.append(line)
            tags = note[2].split(" ")
            note[2]=tags
            notes.append(note)
            note=[]
            name+=1
        except IOError:
            break
    for note in notes:
        ui.listWidget.addItems(note[0])
    sys.exit(app.exec_())
