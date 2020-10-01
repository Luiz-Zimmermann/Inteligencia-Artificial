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
#direcao.view()
#velocidade_saida.view()

#------------------------------------------------------#
# Definição das regras sobre direção
regra1 = ctrl.Rule((proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Esquerda"]), direcao["Direita"])
regra2 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Centro"], direcao[direcao_fixa])
regra3 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Direita"], direcao["Esquerda"])

regra4 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Esquerda"], direcao["Direita"])
regra5 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Centro"], direcao[direcao_fixa])
regra6 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Direita"], direcao["Esquerda"])

regra7 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Esquerda"], direcao["Direita"])
regra8 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Centro"], direcao[direcao_fixa])
regra9 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Direita"], direcao["Esquerda"])

regra10 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], direcao["Direita"])
regra11 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Centro"], direcao[direcao_fixa])
regra12 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Direita"], direcao["Esquerda"])

regra13 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Esquerda"], direcao["Direita"])
regra14 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Centro"], direcao[direcao_fixa])
regra15 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Direita"], direcao["Esquerda"])

regra16 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Esquerda"], direcao["Direita"])
regra17 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Centro"], direcao[direcao_fixa])
regra18 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Direita"], direcao["Esquerda"])


regra19 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], direcao["Direita"])
regra20 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Centro"], direcao[direcao_fixa])
regra21 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Direita"], direcao["Esquerda"])

regra22 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Esquerda"], direcao["Direita"])
regra23 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Centro"], direcao[direcao_fixa])
regra24 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Direita"], direcao["Esquerda"])

regra25 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Esquerda"], direcao["Direita"])
regra26 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Centro"], direcao[direcao_fixa])
regra27 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Direita"], direcao["Esquerda"])

#------------------------------------------------------#
# Regras de sobre a velocidade
regra28 = ctrl.Rule((proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Esquerda"]), velocidade_saida["Baixa"])
regra29 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Centro"], velocidade_saida["Baixa"])
regra30 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Baixa"] & posicao["Direita"], velocidade_saida["Baixa"])

regra31 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Esquerda"], velocidade_saida["Baixa"])
regra32 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Centro"], velocidade_saida["Baixa"])
regra33 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Normal"] & posicao["Direita"], velocidade_saida["Baixa"])

regra34 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Esquerda"], velocidade_saida["Baixa"])
regra35 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Centro"], velocidade_saida["Baixa"])
regra36 = ctrl.Rule(proximidade["Perto"] & velocidade_entrada["Alta"] & posicao["Direita"], velocidade_saida["Baixa"])


regra37 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], velocidade_saida["Normal"])
regra38 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Centro"], velocidade_saida["Normal"])
regra39 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Baixa"] & posicao["Direita"], velocidade_saida["Normal"])

regra40 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Esquerda"], velocidade_saida["Normal"])
regra41 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Centro"], velocidade_saida["Normal"])
regra42 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Normal"] & posicao["Direita"], velocidade_saida["Normal"])

regra43 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Esquerda"], velocidade_saida["Normal"])
regra44 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Centro"], velocidade_saida["Normal"])
regra45 = ctrl.Rule(proximidade["Normal"] & velocidade_entrada["Alta"] & posicao["Direita"], velocidade_saida["Normal"])


regra46 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Esquerda"], velocidade_saida["Normal"])
regra47 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Centro"], velocidade_saida["Normal"])
regra48 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Baixa"] & posicao["Direita"], velocidade_saida["Normal"])

regra49 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Esquerda"], velocidade_saida["Normal"])
regra50 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Centro"], velocidade_saida["Normal"])
regra51 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Normal"] & posicao["Direita"], velocidade_saida["Normal"])

regra52 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Esquerda"], velocidade_saida["Normal"])
regra53 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Centro"], velocidade_saida["Normal"])
regra54 = ctrl.Rule(proximidade["Longe"] & velocidade_entrada["Alta"] & posicao["Direita"], velocidade_saida["Normal"])

lista_regras = [regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9,
                regra10, regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18,
                regra19, regra20, regra21, regra22, regra23, regra24, regra25, regra26, regra27,
                regra28, regra29, regra30, regra31, regra32, regra33, regra34, regra35, regra36,
                regra37, regra38, regra39, regra40, regra41, regra42, regra43, regra44, regra45,
                regra46, regra47, regra48, regra49, regra50, regra51, regra52, regra53, regra54]

controle= ctrl.ControlSystem(lista_regras)
simulacao= ctrl.ControlSystemSimulation(controle)


simulacao.input["Velocidade de Entrada"] = 8
simulacao.input["Proximidade"] = 3
simulacao.input["Posição"] = 5

simulacao.compute()

print("Direção: ", simulacao.output["Direção"])
direcao.view(sim=simulacao)
print("Velocidade: ", simulacao.output["Velocidade de Saida"])
velocidade_saida.view(sim=simulacao)

plt.show()
