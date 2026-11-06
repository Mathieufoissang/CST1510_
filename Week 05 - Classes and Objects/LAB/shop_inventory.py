"""Shop Inventory

Create a Product with name, price, and quantity, plus total_value() and
apply_discount(percent), which changes that product's own price. Store 5
products, print the whole inventory value, apply a 10% discount to each, and
print the new prices.
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        self.price *= 1 - percent / 100


products = [
    Product("Notebook", 2.50, 20),
    Product("Pen", 1.20, 50),
    Product("Backpack", 35.00, 8),
    Product("Water bottle", 12.00, 15),
    Product("Calculator", 18.50, 6),
]

inventory_value = sum(product.total_value() for product in products)
print(f"Total inventory value: ${inventory_value:.2f}")

print("\nPrices after a 10% discount:")
for product in products:
    product.apply_discount(10)
    print(f"{product.name}: ${product.price:.2f}")
