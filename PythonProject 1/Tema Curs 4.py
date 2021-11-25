class Fractie():
    def __init__(self,numarator1,numitor1,numarator2,numitor2):
        self.numarator1 = numarator1
        self.numitor1 = numitor1
        self.numarator2 = numarator2
        self.numitor2 = numitor2

    def __str__(self):
        return f"Prima fractie  este {self.numarator1}/{self.numitor1} si a doua fractie este {self.numarator2}/{self.numitor2}"


    def __add__(self, other):
        numarator_1 = self.numarator1
        numitor_1 = self.numitor1

        numarator_2 = self.numarator2
        numitor_2 = self.numitor2
        rezultat_final = int((self.numarator1 * other.numitor2)+(other.numarator2 * self.numitor1))/int((self.numitor1*other.numitor2))
        if numitor_1 == numitor_2:
            return self.numarator1 + other.numarator2,"/",self.numitor1 + other.numitor2
        else:
            return f"Rezultatul adunarii este: {(self.numarator1 * other.numitor2)+(other.numarator2 * self.numitor1)}/{self.numitor1*other.numitor2} => {rezultat_final}"

    def __sub__(self, other):
        numarator_1 = self.numarator1
        numitor_1 = self.numitor1

        numarator_2 = self.numarator2
        numitor_2 = self.numitor2
        rezultat_fina = int((self.numarator1 * other.numitor2) - (other.numarator2 * self.numitor1)) / int((self.numitor1 * other.numitor2))
        if numitor_1 == numitor_2:
            return self.numarator1 + other.numarator2,"/",self.numitor1 + other.numitor2
        else:
            return f"Rezultatul scaderii este: {(self.numarator1 * other.numitor2)-(other.numarator2 * self.numitor1)}/{self.numitor1*other.numitor2} => {rezultat_fina}"

    def inverse(self):
        numarator_1 = self.numarator1
        numitor_1 = self.numitor1

        numarator_2 = self.numarator2
        numitor_2 = self.numitor2
        return f"Prima fractie inversata este {numitor_1}/{numarator_1} si a doua fractie inversata este {numitor_2}/{numarator_2}"




calcul = Fractie(1,2,3,4)
print(calcul)

print(calcul.__add__(calcul))
print(calcul.__sub__(calcul))
print(calcul.inverse())