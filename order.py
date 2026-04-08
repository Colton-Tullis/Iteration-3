from domain.order_item import OrderItem

class Order:
    def __init__(self, id=None):
        self.id = id
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def total(self):
        return sum(item.total_price() for item in self.items)

    def print_order(self):
        print(f"Order ID: {self.id}")
        for item in self.items:
            item_total = item.total_price()
            print(f"Item: {item.product.name} x{item.quantity} = ${item_total:.2f}")
        print(f"Total = ${self.total():.2f}") 