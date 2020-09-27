import skfuzzy as fzy
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


# Tamanho do gráfico (eixo X)
# Entradas
velocidade = np.arange(0,11,1)
posicao = np.arange(0,11,1)

# Saídas
direcao = np.arange(0,11,1)

#### Fuzzyficação ####
# trimf = triângulo, trampf = trapézio
# Velocidade: low = baixa; medium = normal; high = alta
# Definir valores para l,n e h no trabalho
vel_l = fzy.trapmf(velocidade, [0,0,2,4])
vel_m = fzy.trimf(velocidade, [3,5,7])
vel_h = fzy.trapmf(velocidade, [6,8,10,10])

# Posição: low = esquerda; medium = centro; high = direita
# Definir valores para l,n e h no trabalho
pos_l = fzy.trimf(posicao, [0,0,5])
pos_m = fzy.trimf(posicao, [4,5,6])
pos_h = fzy.trimf(posicao, [5,10,10])

# Direção: low = esquerda; medium = centro; high = direita
# Definir valores para l,n e h no trabalho
direct_l = fzy.trimf(direcao, [0,0,5])
direct_m = fzy.trimf(direcao, [4,5,6])
direct_h = fzy.trimf(direcao, [5,10,10])


"""
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 9))

ax0.plot(velocidade, vel_l, 'b', linewidth=1.5, label='Baixa')
ax0.plot(velocidade, vel_m, 'g', linewidth=1.5, label='Normal')
ax0.plot(velocidade, vel_h, 'r', linewidth=1.5, label='Alta')
ax0.set_title('Velocidade')
ax0.legend()

ax1.plot(direcao, direc_l, 'b', linewidth=1.5, label='Esquerda')
ax1.plot(direcao, direc_m, 'g', linewidth=1.5, label='Centro')
ax1.plot(direcao, direc_h, 'r', linewidth=1.5, label='Direita')
ax1.set_title('Direção')
ax1.legend()


# Turn off top/right axes
for ax in (ax0, ax1):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
"""

velocidade = ctrl.Antecedent(velocidade,"Velocidade")
posicao = ctrl.Antecedent(posicao,"Posição")
direcao = ctrl.Consequent(direcao,"Direção")


velocidade["Baixa"] = vel_l
velocidade["Normal"] = vel_m
velocidade["Alta"] = vel_h

posicao["Esquerda"] = pos_l
posicao["Centro"] = pos_m
posicao["Direita"] = pos_h

direcao["Esquerda"] = direct_l
direcao["Centro"] = direct_m
direcao["Direita"] = direct_h

velocidade.view()
posicao.view()
direcao.view()

regra1 = ctrl.Rule(velocidade["Alta"] & posicao["Esquerda"], direcao["Direita"])
regra2 = ctrl.Rule(velocidade["Alta"] & posicao["Direita"], direcao["Esquerda"])
regra3 = ctrl.Rule(velocidade["Alta"] & posicao["Centro"], direcao["Direita"])

regra4 = ctrl.Rule(velocidade["Normal"] & posicao["Esquerda"], direcao["Direita"])
regra5 = ctrl.Rule(velocidade["Normal"] & posicao["Direita"], direcao["Esquerda"])
regra6 = ctrl.Rule(velocidade["Normal"] & posicao["Centro"], direcao["Direita"])

regra7 = ctrl.Rule(velocidade["Baixa"] & posicao["Esquerda"], direcao["Direita"])
regra8 = ctrl.Rule(velocidade["Baixa"] & posicao["Direita"], direcao["Esquerda"])
regra9 = ctrl.Rule(velocidade["Baixa"] & posicao["Centro"], direcao["Direita"])


print(regra1)
print(regra2)
print(regra3)

controle = ctrl.ControlSystem([regra1,regra2,regra3,regra4,regra5,regra6,regra7,regra8,regra9])
simulacao = ctrl.ControlSystemSimulation(controle)

simulacao.input["Velocidade"] = 3
simulacao.input["Posição"] = 5
simulacao.compute()

print(simulacao.output["Direção"])
direcao.view(sim=simulacao)

plt.show()
