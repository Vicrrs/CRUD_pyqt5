# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.adicionar_item_qpushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.adicionar_item_qpushbutton.setGeometry(QtCore.QRect(30, 100, 121, 51))
        self.adicionar_item_qpushbutton.setObjectName("adicionar_item_qpushbutton")
        self.deletando_item_qpushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.deletando_item_qpushbutton.setGeometry(QtCore.QRect(180, 100, 121, 51))
        self.deletando_item_qpushbutton.setObjectName("deletando_item_qpushbutton")
        self.limparlista_qpushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.limparlista_qpushbutton.setGeometry(QtCore.QRect(330, 100, 121, 51))
        self.limparlista_qpushbutton.setObjectName("limparlista_qpushbutton")
        self.adicionando_item_qlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.adicionando_item_qlineEdit.setGeometry(QtCore.QRect(30, 30, 571, 51))
        self.adicionando_item_qlineEdit.setObjectName("adicionando_item_qlineEdit")
        self.minhaLista_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.minhaLista_listWidget.setGeometry(QtCore.QRect(30, 190, 571, 281))
        self.minhaLista_listWidget.setObjectName("minhaLista_listWidget")
        self.salvadb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.salvadb_pushButton.setGeometry(QtCore.QRect(480, 100, 121, 51))
        self.salvadb_pushButton.setObjectName("salvadb_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda"))
        self.adicionar_item_qpushbutton.setText(_translate("MainWindow", "Adicionar Tarefa"))
        self.deletando_item_qpushbutton.setText(_translate("MainWindow", "Deletar Tarefa"))
        self.limparlista_qpushbutton.setText(_translate("MainWindow", "Limpar lista"))
        self.salvadb_pushButton.setText(_translate("MainWindow", "Salvar no db"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
