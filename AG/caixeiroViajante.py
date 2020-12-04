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
from AG.graph import *

import random

def population_generator(population, cities, length):
    # Genes -> Cidades
    # Cromossomo -> Rotas
    for i in range(length): 
        genes = np.array(random.sample(list(cities), len(cities)))
        cromossomo = Cromossomo(genes, getDistance(genes, distance))
        population.append(cromossomo)

    return population

def evaluation(population):
    population = sorted(population, key=lambda cromossomo: cromossomo.distanciaTotal)
    if len(population) >= 2:
        nova_population = population[:len(population)//2]
        return nova_population
    return population

def exists(rna_1, rna_2):
    # Verifica se dentro de um cromossomo há um gene idêntico ao outro cromossomo
    for gene in rna_1:
        if gene in rna_2:
            return True
    return False

def mutation(population):
    # Geração de uma nova mutação através da população gerada
    new_population = []
    # Definição do DNA e RNA:
    #   DNA -> Primeira metade do cromossomo
    #   RNA -> Segunda metade do cromossomo
    dna_length = len(population[0].rotas)
    rna_length = int(dna_length//2)
    rna_gap = (dna_length - rna_length)

    #print("DNA: ", dna_length)
    #print("RNA: ", rna_length)
    #print("RNA gap: ", rna_gap)

    # Embaralha a população
    population = random.sample(population, len(population))
    iterations = 0
    while not len(population) <= 1:
        done = False
        limit = len(population)
        while not done and not iterations >= limit * 2:
            # Escolha dos pais
            parents = random.sample(population, 2)
            parent1 = parents[0]
            parent2 = parents[1]

            # Copia genes dos cromossomos pais
            parent1_rna = parent1.rotas[:rna_length]
            parent2_rna = parent2.rotas[rna_gap-1:]

            # Verifica caso haja algum gene igual nos dois cromossomos
            if not exists(parent1_rna, parent2_rna):
                print("\nTamanho da população antes da mutação: ", len(population))
                print("Filho: ", parent1_rna, parent2_rna, "\tMutação[", iterations, "]\tLimite: ", limit * 2)

                # Geração do filho
                new_genesis = np.append(parent1_rna, parent2_rna)
                new_cromo = Cromossomo(new_genesis, getDistance(new_genesis, distance))

                # Remove os cromossomos que formaram um novo
                population.remove(parent1)
                population.remove(parent2)

                print("Filho: ", new_cromo.rotas, new_cromo.distanciaTotal)
                print("Tamanho da população apos mutação: ", len(population), "\n")
                new_population.append(new_cromo)
                done = True
                iterations = 0

            else:
                print("Fusão fracassada: ", parent1.rotas, parent2.rotas, "\tMutação[", iterations, "]\tLimite: ", limit * 2)
            iterations += 1

        if iterations >= limit * 2:
            print("\nPassou do limite!!")

            return new_population

    if len(population) == 1: new_population.append(population.pop(0))

    return new_population

def evolution(population, cities, iterations):

    minimum_values = []

    print("\n##################################")
    print("Geração original: ")
    for cromo in population:
        print("Individuo: ", cromo.rotas, cromo.distanciaTotal)

    for i in range(iterations):
        print("\n##################################")
        print("Geração: ", i)
        new_population = mutation(population)
        print("\nPopulação após mutação: ")
        for cromo in new_population:
            print("Individuo: ", cromo.rotas, cromo.distanciaTotal)
        print("-------------------------------------")

        best_population = evaluation(new_population)

        population_gap = len(population) - len(best_population)
        print("População original: ", len(population), "\tPopulação nova: ", len(best_population), "\tFalta na população: ", population_gap)
        new_population = []
        new_population = population_generator(new_population, cities, population_gap)

        print("-------------------------------------")
        print("Próxima população: ")
        for cromo in new_population:
            print("Individuo: ", cromo.rotas, cromo.distanciaTotal)
        print("Melhor da população anterior: ")
        for cromo in best_population:
            print("Individuo: ", cromo.rotas, cromo.distanciaTotal)
        print("-------------------------------------")

        print("Nova população : ", len(new_population), len(best_population))
        next_generation = new_population + best_population

        population = next_generation
        for cromo in population:
            print("Individuo: ", cromo.rotas, cromo.distanciaTotal)
        print("-------------------------------------")
        print("##################################")

        # Armazena os menores valores atingidos durante a evolução
        minimum_values.append(evaluation(population)[0].distanciaTotal)

    return evaluation(population), minimum_values

def getDistance(rotas, distance):
    # Calcula as distâncias a partir dos cromossomos (rotas)
    # Após o termino, é cálculado o retorno ao ponto inicial
    totalDistance = 0
    rangeCities = zeros(len(rotas))
    for i in range(len(rotas)):
        for j in range(cityNumbers):
            for k in range(cityNumbers):
                if j != k:
                    if i == len(rotas)-1:
                        if j+1 == rotas[i] and k+1 == rotas[0]:
                            rangeCities[i] = distance[j][k]
                            totalDistance += distance[j][k]
                    elif j+1 == rotas[i] and k+1 == rotas[i+1]:
                        rangeCities[i] = distance[j][k]
                        totalDistance += distance[j][k]

    #print("Total distancias: ", rangeCities)
    return totalDistance

def getRangeBetweenAandB(a, b, cityNumbers, distance):
    for j in range(cityNumbers):
        for k in range(cityNumbers):
            if (j != k) and k > j:
                if j+1 == a and k+1 ==b:
                    return distance[j][k]


# TODO apresentar gráficos e informações
if __name__ == "__main__":
    # Lendo o arquivo de entrada
    #inputFile = open("C:\\Users\\lucas\\Desenvolvimento\\inteligencia_artificial\\Inteligencia-Artificial\\AG\\input.txt", 'r')
    inputFile = open("input.txt", 'r')
    content = (inputFile.read()).split(";")
    #print("Conteudo: ", content)

    # Definindo numero de cidades
    cityNumbers = int(content[0])
    print("Nº de Cidades:", cityNumbers)
    content = content[1:]

    # Definindo população inicial / nº individuos
    if cityNumbers <= 5:
        populationMax = 10
    elif cityNumbers > 5 and cityNumbers <= 10:
        populationMax = 50
    else:    
        populationMax = 100

    print("População inicial: ", populationMax)

    
    # Montando a matriz das distancias entre as cidades
    distance = zeros((cityNumbers, cityNumbers))
    i = 0
    for j in range(cityNumbers):
        for k in range(cityNumbers):
            if (j != k) and k > j:
                distance[j][k] = content[i]
                distance[k][j] = content[i]
                i += 1
                #print(j, " ~ ", k, " = ", distance[j][k])

    #print("Matriz de distâncias: \n", distance)

    # Cria a população inicial
    cities = arange(1, cityNumbers + 1)
    #print("Cidades: ", cities)
    population = []
    population = population_generator(population, cities, populationMax)

    # Iniciando a evolução, definindo número de iterações
    population, minimum_values = evolution(population, cities, int(input("Quantas iterações?: ")))
    print("Top 5 melhores indivíduos: \n")
    for cromo in population:
        print("Individuo", cromo.rotas, cromo.distanciaTotal)

    # Definindo o melhor individuo após as iterações
    mvp = population[0]
    print("\nMelhor individuo: ", mvp.rotas, mvp.distanciaTotal)
    # Plota o grafico dos melhores valores por geração

    plt.title(u"Gráfico Distância mínima X geração")
    plt.xlabel("Geração")
    plt.ylabel("Distância")
    plt.grid(1)
    plt.plot( arange(0, len(minimum_values), 1), minimum_values)
    plt.show()

    draw_graph(population,cities)



