class Item:

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def __getattribute__(self, name):
    if name == "total":
      price = object.__getattribute__(self, "price")
      quantity = object.__getattribute__(self, "quantity")
      return price * quantity

    elif name == "name":
      original_name = object.__getattribute__(self, "name")
      return original_name.title()

    return object.__getattribute__(self, name)

fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)
