class Airplane():
    def __init__(self, speed = 0, name = "None"):
        self.speed = speed
        self.name = name

class Turbofanplanes(Airplane):
    def __init__(self, speed, name, maxheight):
        super().__init__(speed, name)
        self.maxheight = maxheight

class Turboprop(Airplane):
    def __init__(self, speed, name, maxspeed):
        super().__init__(speed, name)
        self.maxspeed = maxspeed

f14 = Turbofanplanes(85, "F14", 50)
f15 = Turboprop(50, "F15", 10)
print("The speed of", f14.name, "is", f14.speed, "mph.")
print("The speed of", f15.name, "is", f15.speed, "mph.")