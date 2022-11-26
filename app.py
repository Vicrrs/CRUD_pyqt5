import sys
from janela import *
from PyQt5.QtWidgets import QMainWindow, QApplication
import sqlite3


# criando conexao com db
conn = sqlite3.connect('minha_lista.db')
# cirando cursor
c = conn.cursor()

# criando tabela
c.execute("""CREATE TABLE if not exists todo_list(
    list_item text)
    """)

# commitando as mudanças
conn.commit()

# fechar conexão
conn.close()


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.adicionar_item_qpushbutton.clicked.connect(self.add_item)
        self.deletando_item_qpushbutton.clicked.connect(self.delete_item)
        self.limparlista_qpushbutton.clicked.connect(self.clear_item)
        self.salvadb_pushButton.clicked.connect(self.save_item)
        # pega todos os itens do banco de dados
        self.grab_all()

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

    def save_item(self):
        # criando conexao com db
        conn = sqlite3.connect('minha_lista.db')
        # cirando cursor
        c = conn.cursor()

        # excluindo tudo na tabela do banco de dados
        c.execute('DELETE FROM todo_list;',)

        # criar lista em branco para armazenar itens de tarefas
        items = []
        # percorrer a lista e retirar cada item
        for index in range(self.minhaLista_listWidget.count()):
            items.append(self.minhaLista_listWidget.item(index))

        for item in items:
            # print(item.text())
            # adicionando as coisas na tabela
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {
                          'item': item.text(),
                      })

            # commitando as mudanças
        conn.commit()

        # fechar conexão
        conn.close()

    def grab_all(self):
        # criando conexao com db
        conn = sqlite3.connect('minha_lista.db')
        # cirando cursor
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        # commitando as mudanças
        conn.commit()

        # fechar conexão
        conn.close()

        # fazer loop através de registros e adicionar à tela
        for record in records:
            self.minhaLista_listWidget.addItem(str(record))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
