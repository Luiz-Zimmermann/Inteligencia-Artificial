from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
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
https://www.learnpyqt.com/courses/adanced-ui-features/creating-multiple-windows/
"""

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Modelo RBC"
        self.left = 0
        self.top = 0
        self.width = 1540
        self.height = 420
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

        # Conectando os layouts
        inputsLayout.addLayout(self.firstLineLayout)
        inputsLayout.addLayout(self.secondLineLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(inputsLayout)
        self.setLayout(self.mainLayout)

        # Show widget
        self.show()
        self.subtitleLayout = SubLayout()
        self.subtitleLayout.show()


    def createTable(self, topCase, topSim):
        # Create table
        """
        if self.tableWidget is None:
            print("não há tabela")
        else:
            print("já há uma tabela")
        """

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(15)

        # Preenche a tabela
        for line in range(10):
            self.tableWidget.setItem(line, 0, QTableWidgetItem(str(topCase[line].age)))
            self.tableWidget.setItem(line, 1, QTableWidgetItem(str(topCase[line].sex)))
            self.tableWidget.setItem(line, 2, QTableWidgetItem(str(topCase[line].cp)))
            self.tableWidget.setItem(line, 3, QTableWidgetItem(str(topCase[line].trestbps)))
            self.tableWidget.setItem(line, 4, QTableWidgetItem(str(topCase[line].chol)))
            self.tableWidget.setItem(line, 5, QTableWidgetItem(str(topCase[line].fbs)))
            self.tableWidget.setItem(line, 6, QTableWidgetItem(str(topCase[line].restecg)))
            self.tableWidget.setItem(line, 7, QTableWidgetItem(str(topCase[line].thalach)))
            self.tableWidget.setItem(line, 8, QTableWidgetItem(str(topCase[line].exang)))
            self.tableWidget.setItem(line, 9, QTableWidgetItem(str(topCase[line].oldpeak)))
            self.tableWidget.setItem(line, 10, QTableWidgetItem(str(topCase[line].slope)))
            self.tableWidget.setItem(line, 11, QTableWidgetItem(str(topCase[line].ca)))
            self.tableWidget.setItem(line, 12, QTableWidgetItem(str(topCase[line].thal)))
            self.tableWidget.setItem(line, 13, QTableWidgetItem(str(topCase[line].result)))
            self.tableWidget.setItem(line, 14, QTableWidgetItem("{:.4}".format(str(topSim[line]*100.0))+"%"))

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

        #self.refreshTable(top, simtop)
        self.createTable(top, simtop)


class SubLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Legenda de entradas")
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 100

        self.layout = QVBoxLayout()

        self.label_st_age = QLabel("Idade: valores de 0 a Indeterminado.")
        self.label_st_age.setFont(QFont("Arial", 12))

        self.label_st_sex = QLabel("Sexo:  ")
        self.label_st_sex.setFont(QFont("Arial", 12))
        self.label_st_sex_wom = QLabel("* Mulher = 0")
        self.label_st_sex_man = QLabel("* Homem = 1")

        self.label_st_dor = QLabel("Tipo de dor peitoral:")
        self.label_st_dor.setFont(QFont("Arial", 12))
        self.label_st_dor_angina = QLabel("* Angina típica = 1.")
        self.label_st_dor_abnang = QLabel("* Angina atípica = 2.")
        self.label_st_dor_notang = QLabel("* Sem dor aginosa = 3.")
        self.label_st_dor_asympt = QLabel("* Assintomático = 4.")

        self.label_st_pressao = QLabel("Pressão sanguínea: valores de 0 a 200.")
        self.label_st_pressao.setFont(QFont("Arial", 12))
        self.label_st_colest = QLabel("Colesterol sérico: valores de 0 a 417.")
        self.label_st_colest.setFont(QFont("Arial", 12))
        self.label_st_glic = QLabel("Glicose no sangue: Se maior que 120mg/dL, valor é 1, se não é 0.")
        self.label_st_glic.setFont(QFont("Arial", 12))

        self.label_st_eletro = QLabel("Resultados eletrocardiograficos: ")
        self.label_st_eletro.setFont(QFont("Arial", 12))
        self.label_st_eletro_norm = QLabel("* Normal = 0.")
        self.label_st_eletro_abn = QLabel("* Anormalidade no segmento ST-T = 1.")
        self.label_st_eletro_hyper = QLabel("* Hipertrofia ventricular esquerda = 2.")

        self.label_st_freq = QLabel("Frequência cardíaca máxima: valores de 0 a 250.")
        self.label_st_freq.setFont(QFont("Arial", 12))
        self.label_st_exang = QLabel("Angina induzida por exercício: Se sim, valor é 1, se não é 0")
        self.label_st_exang.setFont(QFont("Arial", 12))
        self.label_st_oldpeak = QLabel("Depressão no segmento ST induzida por exercício: valores float")
        self.label_st_oldpeak.setFont(QFont("Arial", 12))

        self.label_st_slope = QLabel("Inclinação no pico do segmento ST: ")
        self.label_st_slope.setFont(QFont("Arial", 12))
        self.label_st_slope_down = QLabel("* Inclinado para baixo = 3.")
        self.label_st_slope_flat = QLabel("* Plano = 2.")
        self.label_st_slope_up = QLabel("* Inclinado para cima = 1.")

        self.label_st_ca = QLabel("Número de artérias visíveis: de 0 a 3")
        self.label_st_ca.setFont(QFont("Arial", 12))

        self.label_st_thal = QLabel("Viabilidade miocardica com talio: ")
        self.label_st_thal.setFont(QFont("Arial", 12))
        self.label_st_thal_sick = QLabel("* Normal = 3.")
        self.label_st_thal_fix = QLabel("* Defeito corrigido = 6.")
        self.label_st_thal_rev = QLabel("* Defeito reversível = 7.")

        self.layout.addWidget(self.label_st_age)
        self.layout.addWidget(self.label_st_sex)
        self.layout.addWidget(self.label_st_sex_wom)
        self.layout.addWidget(self.label_st_sex_man)
        self.layout.addWidget(self.label_st_dor)
        self.layout.addWidget(self.label_st_dor_angina)
        self.layout.addWidget(self.label_st_dor_abnang)
        self.layout.addWidget(self.label_st_dor_notang)
        self.layout.addWidget(self.label_st_dor_asympt)
        self.layout.addWidget(self.label_st_pressao)
        self.layout.addWidget(self.label_st_colest)
        self.layout.addWidget(self.label_st_glic)
        self.layout.addWidget(self.label_st_eletro)
        self.layout.addWidget(self.label_st_eletro_norm)
        self.layout.addWidget(self.label_st_eletro_abn)
        self.layout.addWidget(self.label_st_eletro_hyper)
        self.layout.addWidget(self.label_st_freq)
        self.layout.addWidget(self.label_st_exang)
        self.layout.addWidget(self.label_st_oldpeak)
        self.layout.addWidget(self.label_st_slope)
        self.layout.addWidget(self.label_st_slope_down)
        self.layout.addWidget(self.label_st_slope_flat)
        self.layout.addWidget(self.label_st_slope_up)
        self.layout.addWidget(self.label_st_ca)
        self.layout.addWidget(self.label_st_thal)
        self.layout.addWidget(self.label_st_thal_sick)
        self.layout.addWidget(self.label_st_thal_fix)
        self.layout.addWidget(self.label_st_thal_rev)

        self.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())