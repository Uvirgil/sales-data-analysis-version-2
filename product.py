## Create class Product

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity =quantity
        
    def display_info(self):
        return f"Product Name: {self.name}, Price: {self.price}£, Quantity: {self.quantity}"
    
    def __str__(self):
        return f"Product Name: {self.name}, Price: {self.price}£, Quantity: {self.quantity}" 
    
    def update_quantity(self, value):
        self.quantity += value
        if self.quantity < 0:
            self.quantity = 0
            print(f"Error: Quantity can't be smaller than 0.")
        return f"Neu quantity: {self.quantity}"