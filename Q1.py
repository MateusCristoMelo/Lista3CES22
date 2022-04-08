from abc import abstractmethod

class Car():
    #metodo de instancia eh uma propriedade que o objeto e apeans ele possui, como place e speed
    def __init__(self, speed = 0, place = "None"):
        self.speed = speed
        self.place = place
    
    def changespeed(self, speed):
        self.speed = speed

    @staticmethod #metodo estatico nao precisa de criar um objeto, eh possivel fazer a comparacao abaixo sem criar objeto
    def abovespeedlimit(speed):
        return speed > 40
    
    @abstractmethod #metodo abstrato define um metodo que deve ser implementado em quem herda a classe, mas nao nela mesma
    def changecolor(self, color):
        pass

    @classmethod #metodo de classe cria um objeto do tipo da classe, porem com os parametros que sao passados a ele
    def checkisnational(cls, location):
        if location is "Brazil":
            return cls(0, "Brazil")
        else:
            return cls(0, "International")

class Hyundai(Car):
    def __init__(self, speed=0, place="None", color = "None"):
        super().__init__(speed, place)
        self.color = color
    def changecolor(self, color):
        self.color = color

#metodo de instancia -> mudar a velocidade do carro Etios
Etios = Car(75, "Brazil")
print(Etios.speed)
Etios.changespeed(30)
print(Etios.speed)

#medoto estatico -> verificar se uma velocidade esta ou nao acima do limite
print(Car.abovespeedlimit(50))

#metodo abstrato -> muda a cor do veiculo da subclasse hyundai
hb20 = Hyundai(30, "USA", "Black")
print(hb20.color)
hb20.changecolor("White")
print(hb20.color)

#metodo de classe -> cria um objeto e verifica se um veiculo eh do brazil ou de outro pais (internacional)
sandero = Car.checkisnational("Italia")
print(sandero.place)