#CLASSES 
#-------------------------------------------------

#BURGER CLASSES
class Burger:
  def __init__(self, name, unitPrice, amount):
    self.name = name
    self.unitPrice = unitPrice
    self.amount = amount
  
  def orderBurger(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))

class BeefBurger(Burger):
  def orderBurger(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))


#FRIES CLASSES
class Fries:
  def __init__(self, name, unitPrice, amount):
    self.name = name
    self.unitPrice = unitPrice
    self.amount = amount

  def orderFries(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))


#CHICKENNUGGETS CLASSES
class chickenNuggets:
  def __init__(self, name, unitPrice, amount):
      self.name = name
      self.unitPrice = unitPrice
      self.amount = amount

  def orderchickenNuggets(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))

#DRINKS CLASSES
class Water:
  def __init__(self, name, unitPrice, amount):
      self.name = name
      self.unitPrice = unitPrice
      self.amount = amount
      
  def orderWater(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))

class Coke(Water):
  def orderCoke(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))

class Sprite(Water):
  def orderSprite(self):
    print(self.name, self.unitPrice, self.amount)
    return(float(self.unitPrice) * int(self.amount))

#USER CLASS
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def printname(self):
        print(self.name, self.phone)
        return()


#Details Class
class Details:
    def __init__(self, name, price):
        self.name = name
        self.price = price

