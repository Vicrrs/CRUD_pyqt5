import sys
from janela import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.adicionar_item_qpushbutton.clicked.connect(self.add_item)
        # self.adicionando_item_qlineEdit.clicked.connect(self.add_item)
        self.deletando_item_qpushbutton.clicked.connect(self.delete_item)
        self.limparlista_qpushbutton.clicked.connect(self.clear_item)

    def add_item(self):
        # pegue o item da caixa de listagem
        item = self.adicionando_item_qlineEdit.text()
        # adicionando item na lista
        self.minhaLista_listWidget.addItem(item)
        # limpando a caixa
        self.adicionando_item_qlineEdit.setText("")

    def delete_item(self):
        # pega a linha selecionada ou a linha atual
        seleciona = self.minhaLista_listWidget.currentRow()
        # Deletar linha selecionada
        self.minhaLista_listWidget.takeItem(seleciona)

    def clear_item(self):
        self.minhaLista_listWidget.clear()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
