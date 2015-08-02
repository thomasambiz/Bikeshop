import random
from Bikeshop import Bicycle, Shop, Customer

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

temp = "{0} purchased {1} for ${2} \n Remaining balance: ${3}\n"

for customer in customers:
    canbuy = shop.check(customer.funds)
    shop.sell(random.choice(canbuy), customer)
    print temp.format(customer.name, customer.bike.model, customer.bike.price, customer.funds)
    
print shop