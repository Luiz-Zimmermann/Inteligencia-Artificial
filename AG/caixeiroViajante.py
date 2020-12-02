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

    routes = zeros((cityNumbers, cityNumbers))
    '''
    for i in range(len(content)):
        for j in range(cityNumbers):
    '''