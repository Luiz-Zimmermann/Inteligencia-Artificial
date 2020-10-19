from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QHeaderView, QApplication, QWidget, QAction, QTableWidget, \
    QTableWidgetItem, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
import sys

"""
https://pythonspot.com/pyqt5-textbox-example/
https://stackoverflow.com/questions/38098763/pyside-pyqt-how-to-make-set-qtablewidget-column-width-as-proportion-of-the-a
https://pythonspot.com/pyqt5-table/
https://pythonbasics.org/pyqt-table/
https://build-system.fman.io/pyqt5-tutorial

"""


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Modelo RBC"
        self.left = 0
        self.top = 0
        self.width = 1580
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()


        firstLineLayout = QHBoxLayout()
        secondLineLayout = QHBoxLayout()
        inputsLayout = QVBoxLayout()

        # Input para cada atributo
        # Primeira linha
        self.age = QLineEdit()
        self.label_age = QLabel("Idade: ")
        self.w_age = QLineEdit()
        self.w_age.setFixedWidth(20)

        self.sexo = QLineEdit()
        self.label_sexo = QLabel("Sexo: ")
        self.w_sexo = QLineEdit()
        self.w_sexo.setFixedWidth(20)

        self.tipo_dor = QLineEdit()
        self.label_dor = QLabel("Tipo de dor: ")
        self.w_dor = QLineEdit()
        self.w_dor.setFixedWidth(20)

        self.pressao = QLineEdit()
        self.label_pressao = QLabel("Pressão: ")
        self.w_pressao = QLineEdit()
        self.w_pressao.setFixedWidth(20)

        self.colesterol = QLineEdit()
        self.label_col = QLabel("Colesterol: ")
        self.w_col = QLineEdit()
        self.w_col.setFixedWidth(20)

        self.glicose = QLineEdit()
        self.label_glic = QLabel("Glicose: ")
        self.w_glic = QLineEdit()
        self.w_glic.setFixedWidth(20)

        self.eletro = QLineEdit()
        self.label_eletro = QLabel("Eletrocardiograma: ")
        self.w_eletro = QLineEdit()
        self.w_eletro.setFixedWidth(20)

        firstLineLayout.addWidget(self.label_age)
        firstLineLayout.addWidget(self.w_age)
        firstLineLayout.addWidget(self.age)
        firstLineLayout.addWidget(self.label_sexo)
        firstLineLayout.addWidget(self.w_sexo)
        firstLineLayout.addWidget(self.sexo)
        firstLineLayout.addWidget(self.label_dor)
        firstLineLayout.addWidget(self.w_dor)
        firstLineLayout.addWidget(self.tipo_dor)
        firstLineLayout.addWidget(self.label_pressao)
        firstLineLayout.addWidget(self.w_pressao)
        firstLineLayout.addWidget(self.pressao)
        firstLineLayout.addWidget(self.label_col)
        firstLineLayout.addWidget(self.w_col)
        firstLineLayout.addWidget(self.colesterol)
        firstLineLayout.addWidget(self.label_glic)
        firstLineLayout.addWidget(self.w_glic)
        firstLineLayout.addWidget(self.glicose)
        firstLineLayout.addWidget(self.label_eletro)
        firstLineLayout.addWidget(self.w_eletro)
        firstLineLayout.addWidget(self.eletro)

        # Segunda linha

        self.freq = QLineEdit()
        self.label_freq = QLabel("Frequência : ")
        self.w_freq = QLineEdit()
        self.w_freq.setFixedWidth(20)

        self.angina_exerc = QLineEdit()
        self.label_exerc = QLabel("Angina devido exercício: ")
        self.w_exerc = QLineEdit()
        self.w_exerc.setFixedWidth(20)

        self.depre_ST = QLineEdit()
        self.label_ST = QLabel("Depressão no ST devido exercício: ")
        self.w_ST = QLineEdit()
        self.w_ST.setFixedWidth(20)

        self.inclinacao = QLineEdit()
        self.label_incli = QLabel("Inclinação no pico no ST: ")
        self.w_incli = QLineEdit()
        self.w_incli.setFixedWidth(20)

        self.num_arterias = QLineEdit()
        self.label_arte = QLabel("Nº de artérias visíveis: ")
        self.w_arte = QLineEdit()
        self.w_arte.setFixedWidth(20)

        self.mio_talio = QLineEdit()
        self.label_talio = QLabel("Miocárdica com tálio: ")
        self.w_talio = QLineEdit()
        self.w_talio.setFixedWidth(20)

        pesquisa = QPushButton("&Pesquisar")
        pesquisa.clicked.connect(self.search)

        secondLineLayout.addWidget(self.label_freq)
        secondLineLayout.addWidget(self.w_freq)
        secondLineLayout.addWidget(self.freq)
        secondLineLayout.addWidget(self.label_exerc)
        secondLineLayout.addWidget(self.w_exerc)
        secondLineLayout.addWidget(self.angina_exerc)
        secondLineLayout.addWidget(self.label_ST)
        secondLineLayout.addWidget(self.w_ST)
        secondLineLayout.addWidget(self.depre_ST)
        secondLineLayout.addWidget(self.label_incli)
        secondLineLayout.addWidget(self.w_incli)
        secondLineLayout.addWidget(self.inclinacao)
        secondLineLayout.addWidget(self.label_arte)
        secondLineLayout.addWidget(self.w_arte)
        secondLineLayout.addWidget(self.num_arterias)
        secondLineLayout.addWidget(self.label_talio)
        secondLineLayout.addWidget(self.w_talio)
        secondLineLayout.addWidget(self.mio_talio)
        secondLineLayout.addWidget(pesquisa)

        inputsLayout.addLayout(firstLineLayout)
        inputsLayout.addLayout(secondLineLayout)

        # Add box layout, add table to box layout and add box layout to widget
        mainLayout = QGridLayout()
        mainLayout.addLayout(inputsLayout, 0, 0)
        mainLayout.addWidget(self.tableWidget, 1, 0)
        #mainLayout.addWidget(QLineEdit(), 1,1)
        self.setLayout(mainLayout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(65)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.move(0, 0)
        self.tableWidget.setHorizontalHeaderLabels(["Idade","Sexo", "Tipo de dor",
                                                    "Pressão", "Colesterol","Glicose",
                                                    "Eletrocardiograma","Freq cardíaca max(bpm)",
                                                    "Angina induzida por exercício",
                                                    "Depre no ST devido exercício",
                                                    "Inclinação do pico no ST",
                                                    "Nº artérias princ visíveis",
                                                    "Miocárdica com tálio",
                                                    "Diagnostico (grau)", "Similaridade"])
        stylesheet = "QHeaderView::section{Background-color:rgb(0,255,200)}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    @pyqtSlot()
    def search(self):
        print("pesquisa", self.age.text())

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())