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
        obj.age = data[0]
        obj.sex = data[1]
        obj.cp = data[2]
        obj.trestbps = data[3]
        obj.chol = data[4]
        obj.fbs = data[5]
        obj.restecg = data[6]
        obj.thalach = data[7]
        obj.exang = data[8]
        obj.oldpeak = data[9]
        obj.slope = data[10]
        obj.ca = data[11]
        obj.thal = data[12]

        return obj, obj.vns(entry, weights)

    except:
        print("Erro no try, buildObject")
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
    except:
        print("Erro no for init")
        return

    print("Casos init: ", casos)
    print("Sim init: ", sim)

    """
    casos10 = []
    simil10 = []
    
    for i in range(10):

        # retorna o indice do caso que tem a maior similaridade
        index = np.argmax(sim)
        casos10.append(casos[index])
        simil10.append(sim[index])

        # Atribui zero para posteriormente encontrar os proximos maximos
        sim[index] = 0

    return casos10, simil10
    """
