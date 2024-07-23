from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._shopping_cart = ShoppingCart()

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_shopping_cart(self):
        return self._shopping_cart

    def add_book_to_cart(self, book):
        self._shopping_cart.add_book(book)

    def place_order(self):
        from order import Order
        order = Order(self._shopping_cart, self)
        return order
