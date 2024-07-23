class Book:
    def __init__(self, title, author, price, quantity):
        self._title = title
        self._author = author
        self._price = price
        self._quantity = quantity

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def display_info(self):
        return f"{self._title} by {self._author} - ${self._price} ({self._quantity} available)"
