from product import Product
from product_manager import ProductManager
from cart import Cart
import random


## Create the ProductManager instance

product_manager = ProductManager()

product1 = Product("Laptop", 899.99, 56)
product2 = Product("Charger", 9.99, 212)
product3 = Product("Wireless Charger", 22.99, 123)
product4 = Product("Phone Case", 5.99, 398)

product_manager.products.append(product1)
product_manager.products.append(product2)
product_manager.products.append(product3)
product_manager.products.append(product4)



product_manager.remove_product("Wireless Charger")
print("\nProducts left in store:")
for product in product_manager.products:
    print(product)


cart = Cart()

added_cart_products = random.sample(product_manager.products, 3)

for product in added_cart_products:
    cart.add_item(product, 1)

# print("Products in cart:")
print(cart.display_cart())
print(cart.calculate_cart_values())