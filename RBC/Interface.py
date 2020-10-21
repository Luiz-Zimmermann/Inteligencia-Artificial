from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QHeaderView, QApplication, QWidget, QAction, QTableWidget, \
    QTableWidgetItem, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
import sys
import main



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




        self.firstLineLayout = QHBoxLayout()
        self.secondLineLayout = QHBoxLayout()
        inputsLayout = QVBoxLayout()

        # Peso padrão
        weight = "1"

        # Input para cada atributo
        # Primeira linha
        self.age = QLineEdit("60")
        self.label_age = QLabel("Idade: ")
        self.w_age = QLineEdit(weight)
        self.w_age.setFixedWidth(20)

        self.sexo = QLineEdit("1")
        self.label_sexo = QLabel("Sexo: ")
        self.w_sexo = QLineEdit(weight)
        self.w_sexo.setFixedWidth(20)

        self.tipo_dor = QLineEdit("1")
        self.label_dor = QLabel("Tipo de dor: ")
        self.w_dor = QLineEdit(weight)
        self.w_dor.setFixedWidth(20)

        self.pressao = QLineEdit("190")
        self.label_pressao = QLabel("Pressão: ")
        self.w_pressao = QLineEdit(weight)
        self.w_pressao.setFixedWidth(20)

        self.colesterol = QLineEdit("200")
        self.label_col = QLabel("Colesterol: ")
        self.w_col = QLineEdit(weight)
        self.w_col.setFixedWidth(20)

        self.glicose = QLineEdit("1")
        self.label_glic = QLabel("Glicose: ")
        self.w_glic = QLineEdit(weight)
        self.w_glic.setFixedWidth(20)

        self.eletro = QLineEdit("1")
        self.label_eletro = QLabel("Eletrocardiograma: ")
        self.w_eletro = QLineEdit(weight)
        self.w_eletro.setFixedWidth(20)

        self.firstLineLayout.addWidget(self.label_age)
        self.firstLineLayout.addWidget(self.w_age)
        self.firstLineLayout.addWidget(self.age)
        self.firstLineLayout.addWidget(self.label_sexo)
        self.firstLineLayout.addWidget(self.w_sexo)
        self.firstLineLayout.addWidget(self.sexo)
        self.firstLineLayout.addWidget(self.label_dor)
        self.firstLineLayout.addWidget(self.w_dor)
        self.firstLineLayout.addWidget(self.tipo_dor)
        self.firstLineLayout.addWidget(self.label_pressao)
        self.firstLineLayout.addWidget(self.w_pressao)
        self.firstLineLayout.addWidget(self.pressao)
        self.firstLineLayout.addWidget(self.label_col)
        self.firstLineLayout.addWidget(self.w_col)
        self.firstLineLayout.addWidget(self.colesterol)
        self.firstLineLayout.addWidget(self.label_glic)
        self.firstLineLayout.addWidget(self.w_glic)
        self.firstLineLayout.addWidget(self.glicose)
        self.firstLineLayout.addWidget(self.label_eletro)
        self.firstLineLayout.addWidget(self.w_eletro)
        self.firstLineLayout.addWidget(self.eletro)

        # Segunda linha

        self.freq = QLineEdit("120")
        self.label_freq = QLabel("Frequência : ")
        self.w_freq = QLineEdit(weight)
        self.w_freq.setFixedWidth(20)

        self.angina_exerc = QLineEdit("1")
        self.label_exerc = QLabel("Angina devido exercício: ")
        self.w_exerc = QLineEdit(weight)
        self.w_exerc.setFixedWidth(20)

        self.depre_ST = QLineEdit("1")
        self.label_ST = QLabel("Depressão no ST devido exercício: ")
        self.w_ST = QLineEdit(weight)
        self.w_ST.setFixedWidth(20)

        self.inclinacao = QLineEdit("0")
        self.label_incli = QLabel("Inclinação no pico no ST: ")
        self.w_incli = QLineEdit(weight)
        self.w_incli.setFixedWidth(20)

        self.num_arterias = QLineEdit("2")
        self.label_arte = QLabel("Nº de artérias visíveis: ")
        self.w_arte = QLineEdit(weight)
        self.w_arte.setFixedWidth(20)

        self.mio_talio = QLineEdit("3")
        self.label_talio = QLabel("Miocárdica com tálio: ")
        self.w_talio = QLineEdit(weight)
        self.w_talio.setFixedWidth(20)

        pesquisa = QPushButton("&Pesquisar")
        pesquisa.clicked.connect(self.search)

        self.secondLineLayout.addWidget(self.label_freq)
        self.secondLineLayout.addWidget(self.w_freq)
        self.secondLineLayout.addWidget(self.freq)
        self.secondLineLayout.addWidget(self.label_exerc)
        self.secondLineLayout.addWidget(self.w_exerc)
        self.secondLineLayout.addWidget(self.angina_exerc)
        self.secondLineLayout.addWidget(self.label_ST)
        self.secondLineLayout.addWidget(self.w_ST)
        self.secondLineLayout.addWidget(self.depre_ST)
        self.secondLineLayout.addWidget(self.label_incli)
        self.secondLineLayout.addWidget(self.w_incli)
        self.secondLineLayout.addWidget(self.inclinacao)
        self.secondLineLayout.addWidget(self.label_arte)
        self.secondLineLayout.addWidget(self.w_arte)
        self.secondLineLayout.addWidget(self.num_arterias)
        self.secondLineLayout.addWidget(self.label_talio)
        self.secondLineLayout.addWidget(self.w_talio)
        self.secondLineLayout.addWidget(self.mio_talio)
        self.secondLineLayout.addWidget(pesquisa)

        inputsLayout.addLayout(self.firstLineLayout)
        inputsLayout.addLayout(self.secondLineLayout)

        # Add box layout, add table to box layout and add box layout to widget
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(inputsLayout)
        #mainLayout.addWidget(QLineEdit(), 1,1)
        self.setLayout(self.mainLayout)


        # Show widget
        self.show()


    def createTable(self, topCase):
        # Create table

        #print(self.mainLayout.findChild("tableWidget"))

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
        self.mainLayout.addWidget(self.tableWidget)

    # Preenche a tabela com os 10 casos mais similares
    def refreshTable(self, topCase,topSim):
        """
        for i in range(10):# linha
            for j in range(12):# coluna
                self.tableWidget.setItem(i, j, QTableWidgetItem(topCase[i][j]))
        """




    @pyqtSlot()
    def search(self):
        weights = []
        att = []

        # Recuperando os pesos
        weights.append(float(self.w_age.text()))
        weights.append(float(self.w_sexo.text()))
        weights.append(float(self.w_dor.text()))
        weights.append(float(self.w_pressao.text()))
        weights.append(float(self.w_col.text()))
        weights.append(float(self.w_glic.text()))
        weights.append(float(self.w_eletro.text()))
        weights.append(float(self.w_freq.text()))
        weights.append(float(self.w_exerc.text()))
        weights.append(float(self.w_ST.text()))
        weights.append(float(self.w_incli.text()))
        weights.append(float(self.w_arte.text()))
        weights.append(float(self.w_talio.text()))

        # Recuperando os atributos
        att.append(self.age.text())
        att.append(self.sexo.text())
        att.append(self.tipo_dor.text())
        att.append(self.pressao.text())
        att.append(self.colesterol.text())
        att.append(self.glicose.text())
        att.append(self.eletro.text())
        att.append(self.freq.text())
        att.append(self.angina_exerc.text())
        att.append(self.depre_ST.text())
        att.append(self.inclinacao.text())
        att.append(self.num_arterias.text())
        att.append(self.mio_talio.text())

        top, simtop = main.init(att, weights)

        print("Top 10: ", top)
        print("Similaridade top 10", simtop)

        #self.refreshTable(top, simtop)
        self.createTable(simtop)






if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())