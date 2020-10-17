class HeartDisease():
    age = 0             # Idade
    sex = ""            # Sexo
    cp = ""             # Tipo de dor peitoral
    trestbps = 0        # Pressão sanguínea
    chol = 0            # Colesterol sérico
    fbs = False         # Glicose >120mg/dL
    restecg = ""        # Resultados eletrocardiograficos
    thalach = 150       # Frequência cardíaca máxima
    exang = False       # Angina induzida por exercício?
    oldpeak = False     # Depressão no segmento ST induzida por exercício
    slope = ""          # Inclinação no pico do segmento ST
    ca = 0              # Número de artérias visíveis
    thal = 3            # Viabilidade miocardica com talio
    result = 0     # Resultado


    def __init__(self, case):
        self.age = case[0]
        self.sex = case[1] 
        self.cp = case[2] 
        self.trestbps = case[3] 
        self.chol = case[4] 
        self.fbs = case[5] 
        self.restecg = case[6] 
        self.thalach = case[7] 
        self.exang = case[8] 
        self.oldpeak = case[9] 
        self.slope = case[10] 
        self.ca = case[11] 
        self.thal = case[12] 

    def similarityAge(self, entry):
       return 1 - ( abs(self.age - entry) / (100) )
    
    def similaritySex(self, entry):
        return 1 if self.sex == entry else 0

    def similarityCp(self, entry):
        # asympt = assintomatico
        # angina = angina tipica
        # abnang = angina atipica
        # notang = sem dor aginosa
        if self.cp == entry: return 1

        if entry == "angina":   # angina tipica
            if self.cp == "abnang": return 0.4
            if self.cp == "notang": return 0.2
            else: return 0
        elif entry == "abnang":  # angina atipica
            if self.cp == "angina": return 0.4
            if self.cp == "notang": return 0.6
            else: return 0
        elif entry == "notang":  # sem dor anginosa
            if self.cp == "angina": return 0.2
            if self.cp == "abnang": return 0.6
            else: return 0
        else: return 0   # assintomatico

    def similarityTrestbps(self, entry):
        return 1 - ( abs(self.trestbps - entry) / (self.trestbps + entry) )
    
    def similarityChol(self, entry):
        return 1 - ( abs(self.chol - entry) / (self.chol + entry) )

    def similarityFbs(self, entry): 
        return 1 if self.fbs == entry else 0

    def similarityRestecg(self, entry):
        # norm = normal
        # abn = anormalidade no segmento ST-T
        # hyper = hipertrofia ventricular esquerda
        if self.restecg == entry: return 1

        if entry == "norm":   # normal
            if self.restecg == "abn": return 0
            else: return 0.4    # hyper
        elif entry == "abn":  # anormalidade no segmento ST-T
            if self.restecg == "norm": return 0
            else: return 0.6    # hyper
        else:
            if self.restecg == "norm": return 0.4
            else: return 0.6    # abn

    def similarityThalach(self, entry):
        return 1 - ( abs(self.thalach - entry) / (self.thalach + entry) )

    def similarityExang(self, entry): 
        return 1 if self.exang == entry else 0

    def similarityOldpeak(self, entry): 
        return 1 if self.oldpeak == entry else 0

    def similaritySlope(self, entry):
        # down = inclinado para baixo
        # flat = plano
        # up = inclinado para cima
        if self.slope == entry: return 1
        elif entry == "plan" or self.slope == "plan": return 0.5
        else: return 0
    
    def similarityCa(self, entry):
        return 1 - ( abs(self.ca - entry) / (self.ca + entry) )

    def similarityThal(self, entry): 
        return 1 if self.thal == entry else 0
    
    def vns(self, entry, numberCases, weights):   # Variable Neighborhood Search = Algorítmo de Busca por Vizinhaça
        """
        #  SOMA(Wi * sim(fl, fr)) / SOMA(Wi)
        #   - W: Peso do atributo
        #   - sim: Função de similaridade
        #   - fl: Valor do atributo (i) para o caso da base
        #   - fr: Valor do atributo (i) para o caso problema
        """
        pass