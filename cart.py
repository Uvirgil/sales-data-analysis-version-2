
class Cart:
    def __init__(self):
        self.items_in_cart = []
        
    def add_item(self, product, quantity):
        if quantity <= product.quantity:
            self.items_in_cart.append({"Product": product, "Quantity": quantity})
            product.update_quantity(-quantity)
        else:
            return f"Sorry, we don't have enough {product.name}. We only have {product.quantity} in stock."
            
    def calculate_cart_values(self):
        total_value = 0
        for item in self.items_in_cart:
            total_value += item["Product"].price * item["Quantity"]
        return f"Total cart value is: {total_value:.2f} £"
        
    def display_cart(self):
        if not self.items_in_cart:
            return "Your cart is empty."
        else:
            cart_content = "\nItems in your cart: "
            for item in self.items_in_cart:
                product_name = item['Product'].name
                quantity = item['Quantity']
                total_price = item['Product'].price * quantity
                cart_content += f"\n{product_name} - {quantity} pcs - price for this product(s): {total_price:.2f} £"
            return cart_content
