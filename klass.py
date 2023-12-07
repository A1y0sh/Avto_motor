class Avto:
    def __init__(self, modeli, reni, karopka, senasi):
        self.modeli = modeli
        self.reni = reni
        self.karopka = karopka
        self.senasi = senasi
        self.kilometr = 1

    def avto_modeli(self):
        return self.modeli

    def avto_reni(self):
        return self.reni

    def avto_karopkasi(self):
        return self.karopka

    def avto_senasi(self):
        return self.senasi

    def avto_klometr(self):
        return self.kilometr

    def prastoy(self):
        return self.modeli, self.reni, self.karopka, self.karopka, self.senasi, self.kilometr

    def avto1(self):
        print(
            f"mashinnin ati {self.modeli}, reni {self.reni}, karopkasi {self.karopka}, senasi {self.senasi}, {self.kilometr} kilometir jurgu")


magliwmat_avto = Avto('jentra', 'qara', 'aptamat', 25000)

magliwmat_avto.avto1()



