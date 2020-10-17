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
    num = 0     # Resultado
    
    def __init__(self, data):
        data[0] = self.age
        data[1] = self.sex
        data[2] = self.cp
        data[3] = self.trestbps
        data[4] = self.chol
        data[5] = self.fbs
        data[6] = self.restecg
        data[7] = self.thalach
        data[8] = self.exang
        data[9] = self.oldpeak
        data[10] = self.slope
        data[11] = self.ca
        data[12] = self.thal

