from domain.order import Order

class OrderRepository:
    def __init__(self):
        self._orders = {}
        self._next_id = 1

    def save(self, order):
        if order.id is None:
            order.id = self._next_id
            self._next_id += 1
        self._orders[order.id] = order
        return order.id

    def get(self, order_id):
        return self._orders.get(order_id)

    def list_all(self):
        return list(self._orders.values())