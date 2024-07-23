class ShoppingCart:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def get_books(self):
        return self._books

    def calculate_total_price(self):
        return sum(book.get_price() for book in self._books)

    def __iter__(self):
        return iter(self._books)
