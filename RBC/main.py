import numpy as np
import heartDisease

"""
Protótipo de RBC -> Diagnóstico de Pacientes com Possíveis Problemas Cardíacos
    Alunos: Lucas José da Cunha e Luiz Alberto Zimmermann Zabel Martins Pinto
    Professor: Rudimar Dazzi
    Disciplina: Inteligência Artificial
    Curso: Engenharia de Computação - UNIVALI
"""

# Atributos:
#   age; sex (1,0); cp (1-4); trestbps; chol; fbs (1,0); restecg (0,1,2);
#   thalach; exang (1,0); oldpeak; slope (1,2,3); ca; thal (3,6,7);
#   class att: 0 is healthy, 1,2,3,4 is sick.


def buildObject(obj, data, entry, weights):

    try:
        caso = obj(data)
        return caso, caso.vns(entry, weights)

    except (ValueError, RuntimeError, TypeError, NameError) as erro:
        print("Erro em main.buildObject: {0}".format(erro))
        return




def init(entry, weights):
    arquivo = open("processed.cleveland.data.txt","r")
    casos = []
    sim = []

    try:
        for linha in arquivo:
            data = linha.split(",")
            caso, similaridade = buildObject(heartDisease.HeartDisease, data, entry, weights)

            casos.append(caso)
            sim.append(similaridade)
    except (ValueError, RuntimeError, TypeError, NameError) as erro:
        print("Erro em na chamada para construir os objetos, main.init: {0}".format(erro))
        return

    casos10 = []
    simil10 = []

    try:
        for i in range(10):

            # retorna o indice do caso que tem a maior similaridade
            index = np.argmax(sim)
            casos10.append(casos[index])
            simil10.append(sim[index])

            # Atribui zero para posteriormente encontrar os proximos maximos
            sim[index] = 0

        return casos10, simil10
    except (ValueError, RuntimeError, TypeError, NameError) as erro:
        print("Erro em recuperar os primeiros 10 casos, main.init: {0}".format(erro))
        return
