class HeartDisease():
    def __init__(self, case):
        try:
            self.age = float(case[0])
            self.sex = float(case[1])
            self.cp = float(case[2])
            self.trestbps = float(case[3])
            self.chol = float(case[4])
            self.fbs = float(case[5])
            self.restecg = float(case[6])
            self.thalach = float(case[7])
            self.exang = float(case[8])
            self.oldpeak = float(case[9])
            self.slope = float(case[10])
            self.ca = float(case[11])
            self.thal = float(case[12])
            self.result = float(case[13])

        except (ValueError, RuntimeError, TypeError, NameError) as erro:
            print("Erro na atribuição das variavies ao objeto: {0}".format(erro))

    # Idade (age)
    def similarityAge(self, entry): # Float (0.0 ~ 100.0)
       return 1 - ( abs(self.age - entry) / (100) )
    
    # Sexo (sex)
    def similaritySex(self, entry): # Float (0: Mulher / 1: Homem)
        return 1 if self.sex == entry else 0

    # Tipo de dor peitoral (cp)
    def similarityCp(self, entry):  # Float
        # 1.0 = angina = angina tipica
        # 2.0 = abnang = angina atipica
        # 3.0 = notang = sem dor aginosa
        # 4.0 = asympt = assintomatico
        if self.cp == entry: return 1

        if entry == 1:   # angina tipica
            if self.cp == 2: return 0.4
            if self.cp == 3: return 0.2
            else: return 0
        elif entry == 2:  # angina atipica
            if self.cp == 1: return 0.4
            if self.cp == 3: return 0.6
            else: return 0
        elif entry == 3:  # sem dor anginosa
            if self.cp == 1: return 0.2
            if self.cp == 2: return 0.6
            else: return 0
        else: return 0   # assintomatico

    # Pressão sanguínea (trestbps)
    def similarityTrestbps(self, entry): # Float (0.0 ~ 200.0)
        return 1 - ( abs(self.trestbps - entry) / (self.trestbps + entry))
    
    # Colesterol sérico (chol)
    def similarityChol(self, entry):    # Float (0.0 ~ 417.00)
        return 1 - ( abs(self.chol - entry) / (self.chol + entry))

    # Glicose no sangue > 120mg/dL (fbs)
    def similarityFbs(self, entry):     # Float (0: False / 1: True)
        return 1 if self.fbs == entry else 0

    # Resultados eletrocardiograficos (restecg)
    def similarityRestecg(self, entry): # Float
        # 0.0 = norm = normal
        # 1.0 = abn = anormalidade no segmento ST-T
        # 2.0 = hyper = hipertrofia ventricular esquerda
        if self.restecg == entry: return 1

        if entry == 0:   # normal
            if self.restecg == 1: return 0
            else: return 0.4    # hyper
        elif entry == 1:  # anormalidade no segmento ST-T
            if self.restecg == 0: return 0
            else: return 0.6    # hyper
        else:
            if self.restecg == 0: return 0.4
            else: return 0.6    # abn

    # Frequência cardíaca máxima (thalach)
    def similarityThalach(self, entry): # Float (0.0 ~ 250)
        return 1 - ( abs(self.thalach - entry) / (self.thalach + entry) )

    # Angina induzida por exercício (exang)
    def similarityExang(self, entry): # Float (0: False / 1: True)
        return 1 if self.exang == entry else 0

    # # Depressão no segmento ST induzida por exercício (oldpeak)
    def similarityOldpeak(self, entry): # Float (0.0)
        return 1 - (abs(self.oldpeak - entry) / (self.ca + entry))

    # Inclinação no pico do segmento ST (slope)
    def similaritySlope(self, entry):   # Float
        # 3.0 = down = inclinado para baixo
        # 2.0 = flat = plano
        # 1.0 = up = inclinado para cima
        if self.slope == entry: return 1
        elif entry == 2 or self.slope == 2: return 0.5
        else: return 0

    # Número de artérias visíveis (ca)
    def similarityCa(self, entry):  # Float (0.0 ~ 3.0)
        return 1 - ( abs(self.ca - entry) / (self.ca + entry) )

    # Viabilidade miocardica com talio (thal)
    def similarityThal(self, entry): # Float (3.0: sick, 6.0: fix, 7.0: rev)
        return 1 if self.thal == entry else 0
    
    # Diagnóstico
    def vns(self, entry, weights):   # Variable Neighborhood Search = Algorítmo de Busca por Vizinhaça
        """
        #  SOMA(Wi * sim(fl, fr)) / SOMA(Wi)
        #   - W: Peso do atributo
        #   - sim: Função de similaridade
        #   - fl: Valor do atributo (i) para o caso da base
        #   - fr: Valor do atributo (i) para o caso problema
        """

        try:

            similarity = (
                (float(weights[0]) * self.similarityAge(float(entry[0]))) +
                (float(weights[1]) * self.similaritySex(float(entry[1]))) +
                (float(weights[2]) * self.similarityCp(float(entry[2]))) +
                (float(weights[3]) * self.similarityTrestbps(float(entry[3]))) +
                (float(weights[4]) * self.similarityChol(float(entry[4]))) +
                (float(weights[5]) * self.similarityFbs(float(entry[5]))) +
                (float(weights[6]) * self.similarityRestecg(float(entry[6]))) +
                (float(weights[7]) * self.similarityThalach(float(entry[7]))) +
                (float(weights[8]) * self.similarityExang(float(entry[8]))) +
                (float(weights[9]) * self.similarityOldpeak(float(entry[9]))) +
                (float(weights[10]) * self.similaritySlope(float(entry[10]))) +
                (float(weights[11]) * self.similarityCa(float(entry[11]))) +
                (float(weights[12]) * self.similarityThal(float(entry[12])))
            )/float(sum(weights))
        except (ValueError, RuntimeError, TypeError, NameError) as erro:
            print("Erro no calculo de similaridade: {0}".format(erro))

        return similarity