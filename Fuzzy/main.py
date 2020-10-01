import skfuzzy as fzy
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Tamanho do gráfico (eixo X)
lenght = np.arange(0, 11, 1)
direcao_fixa = "Direita"

# Entradas
velocidade_entrada = np.arange(0,11,1)
proximidade = np.arange(0,11,1)
posicao = np.arange(0,11,1)

# Saídas
direcao = np.arange(0,11,1)
velocidade_saida = np.arange(0,11,1)

#### Fuzzyficação ####
# trimf = triângulo, trampf = trapézio
# Velocidade de entrada: low = baixa; medium = normal; high = alta
vel_en_l = fzy.trapmf(velocidade_entrada, [0,0,2,4])
vel_en_m = fzy.trimf(velocidade_entrada, [3,5,7])
vel_en_h = fzy.trapmf(velocidade_entrada, [6,8,10,10])

# Proximidade: close = perto; medium = normal; far = longe
pro_c = fzy.trapmf(proximidade, [0,0,2,4])
pro_m = fzy.trimf(proximidade, [3,5,7])
pro_f = fzy.trapmf(proximidade, [6,8,10,10])

# Posição: left = esquerda; center = centro; right = direita
pos_l = fzy.trimf(posicao, [0,0,5])
pos_c = fzy.trimf(posicao, [4,5,6])
pos_r = fzy.trimf(posicao, [5,10,10])

# Direção: low = esquerda; medium = centro; high = direita
direct_l = fzy.trimf(direcao, [0,0,5])
direct_m = fzy.trimf(direcao, [4,5,6])
direct_h = fzy.trimf(direcao, [5,10,10])

# Velocidade de saida: low = baixa; medium = normal; high = alta
vel_sa_l = fzy.trapmf(velocidade_saida, [0,0,2,4])
vel_sa_m = fzy.trimf(velocidade_saida, [3,5,7])
vel_sa_h = fzy.trapmf(velocidade_saida, [6,8,10,10])

# Define as entradas e saidas do sistema
velocidade_entrada = ctrl.Antecedent(velocidade_entrada, "Velocidade de Entrada")
proximidade = ctrl.Antecedent(proximidade, "Proximidade")
posicao = ctrl.Antecedent(posicao, "Posição")
direcao = ctrl.Consequent(direcao, "Direção")
velocidade_saida = ctrl.Consequent(velocidade_saida, "Velocidade de Saida")

# Faixa de valores para utilizar nas regras
velocidade_entrada["Baixa"] = vel_en_l
velocidade_entrada["Normal"] = vel_en_m
velocidade_entrada["Alta"] = vel_en_h

proximidade["Perto"] = pro_c
proximidade["Normal"] = pro_m
proximidade["Longe"] = pro_f

posicao["Esquerda"] = pos_l
posicao["Centro"] = pos_c
posicao["Direita"] = pos_r

direcao["Esquerda"] = direct_l
direcao["Centro"] = direct_m
direcao["Direita"] = direct_h

velocidade_saida["Baixa"] = vel_sa_l
velocidade_saida["Normal"] = vel_sa_m
velocidade_saida["Alta"] = vel_sa_h

# Plota os graficos das entradas e saidas
velocidade_entrada.view()
proximidade.view()
posicao.view()
direcao.view()
velocidade_saida.view()

# Definição das regras
regra1 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Baixa"])
regra2 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Baixa"])
regra3 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Baixa"])

regra4 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Baixa"])
regra5 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Baixa"])
regra6 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Baixa"])

regra7 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Baixa"])
regra8 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Baixa"])
regra9 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Baixa"])


regra10 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Normal"])
regra11 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Normal"])
regra12 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Normal"])

regra13 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Normal"])
regra14 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Normal"])
regra15 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Normal"])

regra16 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Normal"])
regra17 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Normal"])
regra18 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Normal"])


regra19 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Normal"])
regra20 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Normal"])
regra21 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Normal"])

regra22 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Normal"])
regra23 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Normal"])
regra24 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Normal"])

regra25 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Esquerda"], direcao["Direita"] & velocidade_saida["Normal"])
regra26 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Centro"], direcao[direcao_fixa] & velocidade_saida["Normal"])
regra27 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Direita"], direcao["Esquerda"] & velocidade_saida["Normal"])

regra28 = ctrl.Rule(None, velocidade_saida["Alta"])
# --------------------------------------------------------------- #
lista_regras = [regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9,
                regra10, regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18,
                regra19, regra20, regra21, regra22, regra23, regra24, regra25, regra26, regra27,
                regra28]
controle = ctrl.ControlSystem(lista_regras)
simulacao = ctrl.ControlSystemSimulation(controle)

# simulacao.input["Velocidade de Entrada"] = 3
# simulacao.input["Posição"] = 5
simulacao.compute()

print(simulacao.output["Direção"])
direcao.view(sim=simulacao)
print(simulacao.output["Velocidade de Saida"])
velocidade_saida.view(sim=simulacao)

plt.show()
