"""
Algoritmo Genetico -> Solucao para problema do Caixeiro Viajante
    Alunos: Lucas José da Cunha e Luiz Alberto Zimmermann Zabel Martins Pinto
    Professor: Rudimar Dazzi
    Disciplina: Inteligência Artificial
    Curso: Engenharia de Computação - UNIVALI
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz
from csv import *

if __name__ == "__main__":
    
    # Lendo o arquivo de entrada
    inputFile = open("C:\\Users\\lucas\\Desenvolvimento\\inteligencia_artificial\\Inteligencia-Artificial\\AG\\input.txt", 'r')
    content = (inputFile.read()).split(";\n")
    print("Conteudo: ", content)

    # Definindo numero de cidades
    cityNumbers = int(content[0])
    print("Nº de Cidades:", cityNumbers)

    population = content[1:]