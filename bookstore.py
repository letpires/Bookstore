class Bookstore:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def get_books(self):
        return self._books

    def display_available_books(self):
        print("Available Books:")
        for book in self._books:
            print(book.display_info())

    def process_order(self, order):
        for book in order._shopping_cart:
            if book in self._books:
                if book.get_quantity() > 0:
                    book._quantity -= 1
                else:
                    print(f"Sorry, {book.get_title()} is out of stock!")
            else:
                print(f"Sorry, {book.get_title()} is not available in our bookstore!")

        print(f"Order placed successfully by {order._customer.get_name()}!")
