class OrderCalculator:
    def __init__(self, products: list):
        self.products = products

    def total_items(self):
        return sum(p['quantity'] for p in self.products)

    def subtotal(self):
        return sum(p['quantity'] * p['price'] for p in self.products)

    def tax(self):
        return round(self.subtotal() * 0.1, 2)

    def discount(self):
        subtotal = self.subtotal()
        return round(subtotal * 0.05, 2) if subtotal > 1000 else 0.0

    def final_amount(self):
        return round(self.subtotal() + self.tax() - self.discount(), 2)
