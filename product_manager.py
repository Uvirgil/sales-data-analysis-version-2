## Create class ProductManager
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        # return f"Product {product.name} added."
    
    def display_products(self):
        for product in self.products:
            print(product.display_info())
        
    def total_products_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
            return total
        
    def remove_product(self, name):
        self.products = [product for product in self.products if product.name != name]