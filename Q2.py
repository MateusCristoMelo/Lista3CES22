class Car():
    def __init__(self, color = "None", place = "None"):
        self.color = color
        self.place = place

    @staticmethod #metodo estatico nao precisa de criar um objeto, eh possivel fazer a comparacao abaixo sem criar objeto
    def checkisred(color):
        return color is ("Red" or "red")

cars = {"blue" : 1, "black": 2, "orange" : 3, "Red" : 4, "Silver" : 5}

for i in cars:
    print("That random car is red?", Car.checkisred(i))

