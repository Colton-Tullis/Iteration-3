from domain.order import Order


class OrderServices:
    def __init__(self, product_repo, order_repo):
        self.product_repo = product_repo
        self.order_repo = order_repo

    def place_order(self, product_requests):
        new_order = Order()

        for request in product_requests:
            p_id = request['id']
            qty = request['qty']

            product = self.product_repo.get(p_id)
            if not product:
                print(f"Error: Product with ID {p_id} not found. Order cancelled.")
                return None

            new_order.add_item(product, qty)

        # Use the repository to persist the order and get an ID
        order_id = self.order_repo.save(new_order)
        return order_id

    def get_order_summary(self, order_id):
        """Retrieves an order and displays its details."""
        order = self.order_repo.get(order_id)
        if order:
            order.print_order()
        else:
            print(f"Order #{order_id} not found.")
        return order
