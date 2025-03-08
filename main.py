from product import Product
from product_manager import ProductManager


## Create the ProductManager instance

product_manager = ProductManager()

product1 = Product("Phone", 899.99, 56)
product2 = Product("Charger", 9.99, 242)
product3 = Product("Wireless Charger", 19.99, 123)
product4 = Product("Phone Case", 5.99, 432)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)

print("Products in the store:")
product_manager.display_products()

print(f"Total value of products in the store: {product_manager.total_products_value()}£")

product_manager.remove_product("Wireless Charger")
print("Products left in store:")
for product in product_manager.products:
    print(product)
