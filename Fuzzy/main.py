import skfuzzy as fzy
import numpy as np
import matplotlib.pyplot as plt


# Tamanho do gráfico (eixo X)
velocidade = np.arange(0,10,1)
direcao = np.arange(0,10,1)

# Fuzzyficação
# trimf = triângulo, trampf = trapézio
# Velocidade: low = baixa; medium = normal; high = alta
# Definir valores para l,n e h no trabalho
vel_l = fzy.trapmf(velocidade, [0,0,2,4])
vel_m = fzy.trimf(velocidade, [3,5,7])
vel_h = fzy.trapmf(velocidade, [6,8,10,10])

# Direção: low = esquerda; medium = centro; high = direita
# Definir valores para l,n e h no trabalho
direc_l = fzy.trimf(direcao, [0,0,5])
direc_m = fzy.trimf(direcao, [4,5,6])
direc_h = fzy.trimf(direcao, [5,10,10])

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

"""
# Turn off top/right axes
for ax in (ax0, ax1):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
"""
plt.tight_layout()
plt.show()