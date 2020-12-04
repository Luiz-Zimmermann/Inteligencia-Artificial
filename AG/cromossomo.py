'''
    Genes -> Cidades
    Cromossomo -> Rotas
    distanciaTotal -> Valor para verificação e geração dos filhos
'''
class Cromossomo:
    def __init__(self, rotas, distanciaTotal):
        self.rotas = rotas
        self.distanciaTotal = distanciaTotal