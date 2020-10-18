from PyQt5.QtWidgets import QMainWindow, QLineEdit, QHeaderView, QApplication, QWidget, QAction, QTableWidget, \
    QTableWidgetItem, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
import sys

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
        age = QLineEdit()
        label_age = QLabel("Idade: ")
        sexo = QLineEdit()
        label_sexo = QLabel("Sexo: ")
        tipo_dor = QLineEdit()
        label_dor = QLabel("Tipo de dor: ")
        pressao = QLineEdit()
        label_pressao = QLabel("Pressão: ")
        colesterol = QLineEdit()
        label_col = QLabel("Colesterol: ")
        glicose = QLineEdit()
        label_glic = QLabel("Glicose: ")
        eletro = QLineEdit()
        label_eletro = QLabel("Eletrocardiograma: ")

        firstLineLayout.addWidget(label_age)
        firstLineLayout.addWidget(age)
        firstLineLayout.addWidget(label_sexo)
        firstLineLayout.addWidget(sexo)
        firstLineLayout.addWidget(label_dor)
        firstLineLayout.addWidget(tipo_dor)
        firstLineLayout.addWidget(label_pressao)
        firstLineLayout.addWidget(pressao)
        firstLineLayout.addWidget(label_col)
        firstLineLayout.addWidget(colesterol)
        firstLineLayout.addWidget(label_glic)
        firstLineLayout.addWidget(glicose)
        firstLineLayout.addWidget(label_eletro)
        firstLineLayout.addWidget(eletro)

        # Segunda linha

        freq = QLineEdit()
        label_freq = QLabel("Frequência : ")
        angina_exerc = QLineEdit()
        label_exerc = QLabel("Angina devido exercício: ")
        depre_ST = QLineEdit()
        label_ST = QLabel("Depressão no ST devido exercício: ")
        inclinacao = QLineEdit()
        label_incli = QLabel("Inclinação no pico no ST: ")
        num_arterias = QLineEdit()
        label_arte = QLabel("Nº de artérias visíveis: ")
        mio_talio = QLineEdit()
        label_talio = QLabel("Miocárdica com tálio: ")

        pesquisa = QPushButton("&Pesquisar")

        secondLineLayout.addWidget(label_freq)
        secondLineLayout.addWidget(freq)
        secondLineLayout.addWidget(label_exerc)
        secondLineLayout.addWidget(angina_exerc)
        secondLineLayout.addWidget(label_ST)
        secondLineLayout.addWidget(depre_ST)
        secondLineLayout.addWidget(label_incli)
        secondLineLayout.addWidget(inclinacao)
        secondLineLayout.addWidget(label_arte)
        secondLineLayout.addWidget(num_arterias)
        secondLineLayout.addWidget(label_talio)
        secondLineLayout.addWidget(mio_talio)
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



if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())