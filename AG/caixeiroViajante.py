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

# TODO retornar a distancia total do percurso de acordo com as cidades
def search_table(rota):
    pass


def population_generator(populacao, cities):

    for i in range(population):
        # Cria um cromossomo, cada gene é uma cidade
        genes = np.array(random.sample(list(cities), len(cities)))
        cromossomo = Cromossomo(genes, sum(genes) * 2)
        populacao.append(cromossomo)

def exists(rna_1, rna_2):
    for gene in rna_1:
        print(gene)
        if gene in rna_2:
            return True
    return False

# TODO terminar a geração de cromossomos
def mutation(populacao):
    new_population = []
    population_len = len(populacao)
    dna_length = len(populacao[0].rotas)
    rna_length = int(dna_length//2)
    rna_gap = (dna_length - rna_length)

    print("DNA: ", dna_length)
    print("RNA: ", rna_length)
    print("RNA gap: ", rna_gap)
    print("Tamanho da população antes da mutação: ", len(populacao))


    # Embaralha a população
    populacao = random.sample(populacao, len(populacao))

    #for parents in arange(populacao,step=2):
    done = False
    index1 = 0
    index2 = 0
    while not done:
        # Escolha dos pais
        parent1 = populacao.pop(index1)
        parent2 = populacao.pop(index2)
        parent1_rna = parent1.rotas[:rna_length]
        parent2_rna = parent2.rotas[rna_gap-1:]
        if not exists(parent1_rna, parent2_rna):

            print("Pai 1 e 2: ", parent1.rotas, parent2.rotas)
            print("Filho: ", parent1_rna, parent2_rna)

            # Geração do filho
            new_genesis = np.append(parent1_rna, parent2_rna)
            new_cromo = Cromossomo(new_genesis, sum(new_genesis)*2)

            print("Filho: ", new_cromo.rotas, new_cromo.distanciaTotal)
            print("Tamanho da população apos mutação: ", len(populacao))
            done = True

        ##elif index >= population_len:
          ##  index += 1

    return new_population

def evaluation(populacao):

    populacao = sorted(populacao, key=lambda cromossomo: cromossomo.distanciaTotal)
    nova_populacao = populacao[:len(populacao)//2]
    return nova_populacao


# TODO terminar a integração das funções
def evolution(populacao, iterations):

    for i in range(iterations):
        nova_populacao = evaluation(populacao)
        populacao = mutation(nova_populacao)



# TODO apresentar gráficos e informações
if __name__ == "__main__":
    
    # Lendo o arquivo de entrada
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

    # Cria a população inicial
    cities = arange(1, cityNumbers+1)
    print("Cidades: ", cities)
    populacao = []
    population_generator(populacao, cities)

    for i in populacao:
        print("população: ", i.rotas,i.distanciaTotal)

    print("----------------------------------")
    populacao = evaluation(populacao)
    for i in populacao:
        print("população: ", i.rotas, i.distanciaTotal)
    print("-------------------------------------")

    mutation(populacao)
    #evolution(populacao, int(input("Quantas interações? ")))


