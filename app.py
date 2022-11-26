import sys
from janela import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    def add_item(self):
        pass


    def delete_item(self):
        pass


    def clear_item(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
