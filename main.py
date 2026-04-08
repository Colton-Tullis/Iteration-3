from domain.product import Product
from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository
from services.order_services import OrderServices

def main():
    p_repo = ProductRepository()
    o_repo = OrderRepository()
    service = OrderServices(p_repo, o_repo)

    # Add inventory
    p_repo.add(Product(1, "Mug", 12.50))
    p_repo.add(Product(2, "Scarf", 25.00))

    # Place order
    items = [{"id": 1, "qty": 2}, {"id": 2, "qty": 1}]
    order_id = service.place_order(items)

    if order_id:
        print(f"Order Created: #{order_id}")
        o_repo.get(order_id).print_order()

if __name__ == "__main__":
    main()
