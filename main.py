from product import Product
from product_manager import ProductManager


## Create the ProductManager instance

product_manager = ProductManager()

product1 = Product("Laptop", 899.99, 56)
product2 = Product("Charger", 9.99, 212)
product3 = Product("Wireless Charger", 22.99, 123)
product4 = Product("Phone Case", 5.99, 398)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)


