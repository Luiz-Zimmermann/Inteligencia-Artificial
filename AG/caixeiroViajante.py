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
from AG.cromossomo import *
import random

def population_generator(populacao, cities, length):

    for i in range(length):
        # Cria um cromossomo, cada gene é uma cidade
        genes = np.array(random.sample(list(cities), len(cities)))
        cromossomo = Cromossomo(genes, getDistance(genes, distance))
        populacao.append(cromossomo)

    return populacao

def evaluation(populacao):

    populacao = sorted(populacao, key=lambda cromossomo: cromossomo.distanciaTotal)
    if len(populacao) >= 2:
        nova_populacao = populacao[:len(populacao)//2]
        return nova_populacao
    return populacao

def exists(rna_1, rna_2):
    for gene in rna_1:
        if gene in rna_2:
            return True
    return False


def mutation(populacao):

    new_population = []
    population_len = len(populacao)
    dna_length = len(populacao[0].rotas)
    rna_length = int(dna_length//2)
    rna_gap = (dna_length - rna_length)

    print("DNA: ", dna_length)
    print("RNA: ", rna_length)
    print("RNA gap: ", rna_gap)

    # Embaralha a população
    populacao = random.sample(populacao, len(populacao))
    iterations = 0
    while not len(populacao) <= 1:
        done = False
        limit = len(populacao)
        while not done and not iterations >= limit*2:

            # Escolha dos pais
            parents = random.sample(populacao, 2)
            parent1 = parents[0]
            parent2 = parents[1]

            # Copia genes dos cromossomos pais
            parent1_rna = parent1.rotas[:rna_length]
            parent2_rna = parent2.rotas[rna_gap-1:]

            if not exists(parent1_rna, parent2_rna):
                print("Tamanho da população antes da mutação: ", len(populacao))
                print("Filho: ", parent1_rna, parent2_rna, "Mutação nº: ", iterations, "limite: ", limit*2)

                # Geração do filho
                new_genesis = np.append(parent1_rna, parent2_rna)
                new_cromo = Cromossomo(new_genesis, getDistance(new_genesis, distance))

                # Remove os cromossomos que formaram um novo
                populacao.remove(parent1)
                populacao.remove(parent2)

                print("Filho: ", new_cromo.rotas, new_cromo.distanciaTotal)
                print("Tamanho da população apos mutação: ", len(populacao))
                new_population.append(new_cromo)
                done = True
                iterations = 0
            else:
                print("Fusão fracassada: ", parent1.rotas, parent2.rotas, "Mutação nº: ", iterations, "limite: ", limit*2)
            iterations += 1

        if iterations >= limit*2:
            print("Passou do limite!!")
            print(new_population)
            return new_population

    if len(populacao) == 1: new_population.append(populacao.pop(0))
    print(new_population)
    return new_population

def evolution(population, cities, iterations):

    for i in range(iterations):
        print("##################################")
        print("iteração: ", i)
        new_population = mutation(population)
        print("nova população dps da mutação: ", new_population)
        best_population = evaluation(new_population)

        population_gap = len(population) - len(best_population)
        print("População original: ", len(population), "população nova: ", len(best_population), "Falta na população: ", population_gap)
        new_population = []
        new_population = population_generator(new_population, cities, population_gap)

        print("-------------------------------------")
        print("Nova população: ")
        for cromo in new_population:
            print("população: ", cromo.rotas, cromo.distanciaTotal)
        print("Melhor população: ")
        for cromo in best_population:
            print("população: ", cromo.rotas, cromo.distanciaTotal)
        print("-------------------------------------")

        print("Nova + evoluida: ", len(new_population), len(best_population))
        next_generation = new_population + best_population

        population = next_generation
        for cromo in population:
            print("população: ", cromo.rotas, cromo.distanciaTotal)
        print("-------------------------------------")
        print("##################################")

    return evaluation(population)

def getDistance(rotas, distance):
    totalDistance = 0
    rangeCities = zeros(len(rotas))
    for i in range(len(rotas)):
        for j in range(cityNumbers):
            for k in range(cityNumbers):
                if j != k:
                    if i >= len(rotas)-1:
                        totalDistance += 0
                    elif j+1 == rotas[i] and k+1 == rotas[i+1]:
                        rangeCities[i] = distance[j][k]
                        totalDistance += distance[j][k]

    #print("Total distancias: ", rangeCities)
    return 2 * totalDistance

# TODO apresentar gráficos e informações
if __name__ == "__main__":
    
    # Lendo o arquivo de entrada
    #inputFile = open("C:\\Users\\lucas\\Desenvolvimento\\inteligencia_artificial\\Inteligencia-Artificial\\AG\\input.txt", 'r')
    inputFile = open("input.txt", 'r')
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

    
    # Montando a matriz das distancias
    distance = zeros((cityNumbers, cityNumbers))
    i = 0
    for j in range(cityNumbers):
        for k in range(cityNumbers):
            if (j != k) and k > j:
                distance[j][k] = content[i]
                distance[k][j] = content[i]
                i += 1
                #print(j, " ~ ", k, " = ", distance[j][k])
                #         
    print("Matriz de distâncias: \n", distance)

    # Cria a população inicial
    cities = arange(1, cityNumbers+1)
    print("Cidades: ", cities)
    populacao = []
    populacao = population_generator(populacao, cities, population)

    populacao = evolution(populacao, cities, int(input("Quantas interações? ")))
    for cromo in populacao:
        print("Ultima geração: ", cromo.rotas, cromo.distanciaTotal)

    MVP = populacao[0]
    print("Melhor individuo: ", MVP.rotas, MVP.distanciaTotal)


    """
    for i in populacao:
        print("Indivíduo: ", i.rotas, "\tDistância: ", getDistance(i.rotas, distance))

    print("----------------------------------")
    populacao = evaluation(populacao)
    for i in populacao:
        print("população: ", i.rotas, i.distanciaTotal)
    print("-------------------------------------")

    populacao = mutation(populacao)

    print("Retornou da mutação!!")

    if len(populacao) == 0:
        print("Não fez mutação")
    else:
        print("Fez mutação")
        for i in populacao:
            print("população: ", i.rotas, i.distanciaTotal)
    """


