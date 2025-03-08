from product import Product
from product_manager import ProductManager
from cart import Cart
import random


## Create the ProductManager instance

product_manager = ProductManager()

product1 = Product("Phone", 899.99, 56)
product2 = Product("Charger", 9.99, 242)
product3 = Product("Wireless Charger", 19.99, 123)
product4 = Product("Phone Case", 5.99, 432)

product_manager.products.append(product1)
product_manager.products.append(product2)
product_manager.products.append(product3)
product_manager.products.append(product4)

print("Products in the store:")
product_manager.display_products()

print(f"Total value of products in the store: {product_manager.total_products_value()}£")

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