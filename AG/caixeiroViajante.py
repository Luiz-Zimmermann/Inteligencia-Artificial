"""
Algoritmo Genetico -> Solucao para problema do Caixeiro Viajante
    Alunos:     Lucas José da Cunha e Luiz Alberto Zimmermann Zabel Martins Pinto
    Professor:  Rudimar Dazzi
    Disciplina: Inteligência Artificial
    Curso:      Engenharia de Computação - UNIVALI
"""
from numpy import *
from matplotlib.pyplot import *
from csv import *
import colorama

class Cromossomo:
    def __init__(self, rotas, distanciaTotal):
        self.rotas = rotas
        self.distanciaTotal = distanciaTotal

if __name__ == "__main__":
    
    # Lendo o arquivo de entrada
    inputFile = open("C:\\Users\\lucas\\Desenvolvimento\\inteligencia_artificial\\Inteligencia-Artificial\\AG\\input.txt", 'r')
    content = (inputFile.read()).split(";")
    print("Conteudo: ", content)

    # Definindo numero de cidades
    cityNumbers = int(content[0])
    print("Nº de Cidades:", cityNumbers)
    content = content[1:]

    # Definindo população inicial / individuos
    if cityNumbers <= 5:
        population = 10
    elif cityNumbers > 5 and cityNumbers <= 10:
        population = 50
    else:    
        population = 100

    print("População inicial: ", population)

    distance = zeros((cityNumbers, cityNumbers))
    
    # Montando a matriz das distancias
    i = 0
    column = cityNumbers
    for j in range(cityNumbers):
        for k in range(column):
            if (j != k):
                distance[j][k] = content[i]
                print(j, " ~ ", k, " = ", distance[j][k])
                if i < len(content) - 1:
                    i += 1
        column -= 1

    #cromossomo = Cromossomo()