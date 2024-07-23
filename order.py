class Order:
    def __init__(self, shopping_cart, customer):
        self._shopping_cart = shopping_cart
        self._customer = customer
        self._total_price = shopping_cart.calculate_total_price()

    def display_order_summary(self):
        print("Order Summary:")
        for book in self._shopping_cart:
            print(book.display_info())
        print(f"Total Price: ${self._total_price}")
