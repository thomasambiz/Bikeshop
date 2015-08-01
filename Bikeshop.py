import random

class Bicycle:
    def __init__(self, model, kilos, cost):
        self.model = model
        self.weight = kilos
        self.cost = cost
    def __repr__(self):
        temp = "Bike: {0}\n Weight: {1}kg\n Cost: ${2}"
        return temp.format(self.model, self.cost, self.weight)
        
class Shop:
    def __inti__(self, name, margin, stock):
        self.name = name
        self.stock = {}
        self.margin = 0.2
        self.profit = 0
        
        for bike in bikes:
            bike.markup = int(bike.cost*self.margin)
            bike.price = int(bike.cost + bike.markup)
            self.stock[bike.model] = bike
            
    def __repr__(self):
        temp = "\n{0} \n${1} profit\n{2}"
        bikes = "\n".join(str(bike) for bike in self.stock.values())
        return temp.format(self.name, self.profit, bikes)
        
    def check(self, budget):
       bikes = self.stock.values()
       return [bike for bike in bikes if bike.price < budget]
       
    def sell(self, bike, customer):
        customer.bike = bike
        customer.fund -=bike.price
        self.profit += bike.markup
        del self.stock[bike.model]
       
class Customer:
    def __init__(self, name, funds, bike):
        self.name = name
        self.funds = funds
        self.bike = None

bikes = [
    Bicycle("Breezer", 8, 800),
    Bicycle("Fall Creek", 10, 700),
    Bicycle("Whetstone", 13, 400),
    Bicycle("The Slick Banana", 15, 350),
    Bicycle("Buzzer", 16, 150),
    Bicycle("Roadster", 19, 100)
]

customers = [
    Customer("Jake",200,None),
    Customer("George", 500,None),
    Customer("Merideth", 1000, None)
]

shop = Shop("Pedal Power", 0.2, bikes)

for customer in customers:
    bikes = ", ".join(bike.model for bike in shop.check(customer.funds))
    print customer.name, bikes
    
print shop

temp = "{0} purchased {1} for ${2} \n Remaining balance: ${3}"

for customer in customers:
    canbuy = shop.check(customer.funds)
    shop.sell(random.choice(canbuy), customer)
    print temp.format(customer.name, customer.bike.model, customer.bike.price, customer.funds)
    
print shop