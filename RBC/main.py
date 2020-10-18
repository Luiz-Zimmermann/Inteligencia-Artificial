import numpy as np

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

arquivo = open("processed.cleveland.data.txt","r")

for linha in arquivo:
    data = linha.split(",")
    print(data)

"""
linhas = arquivo.readlines()
linhas[i]
"""