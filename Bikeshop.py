class Bicycle:
    def __init__(self, model, kilos, cost):
        self.model = model
        self.kilos = kilos
        self.cost = cost
    def __repr__(self):
        temp = "Bike: {0}\n Weight: {1}kg\n Cost: ${2}\n"
        return temp.format(self.model, self.kilos, self.cost)
        
class Shop:
    def __init__(self, name, margin, bikes):
        self.name = name
        self.margin = margin
        self.profit = 0
        self.stock = {}
        
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
        customer.funds -=bike.price
        self.profit += bike.markup
        del self.stock[bike.model]
       
class Customer:
    def __init__(self, name, funds, bike):
        self.name = name
        self.funds = funds
        self.bike = None