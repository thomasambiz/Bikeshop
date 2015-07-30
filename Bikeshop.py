class Bicycle(object):
    def __init__(self, model, kilos, price):
        self.model = model
        self.weight = kilos
        self.cost = price

class Shop(object):
    def __inti__(self, name, inventory, margin, profit):
        self.name = name
        self.inventory = {}
        self.margin = 20
        self.profit = 0
        
class Customer(object):
    def __init__(self, name, funds, bike):
        self.name = name
        self.funds = funds
        self.bike = None

jake = Customer("Jake", 200, None)
george = Customer("George", 500, None)
merideth = Customer("Merideth", 1000, None)

breezer = Bicycle("Breezer", 8, 949)
fall_Creek = Bicycle("Fall Creek", 10, 749)
whetstone = Bicycle("Whetstone", 13, 449)
slick_banana = Bicycle("The Slick Banana", 15, 399)
buzzer = Bicycle("Buzzer", 16, 179)
roadster = Bicycle("Roadster", 19, 99)

