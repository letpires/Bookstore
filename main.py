if __name__ == "__main__":
    from book import Book
    from customer import Customer
    from bookstore import Bookstore

    # Creating some books
    books = [
        Book("Python Programming", "John Smith", 25, 10),
        Book("Data Science Handbook", "Jane Doe", 30, 5),
        Book("Machine Learning Basics", "Alice Johnson", 20, 8)
    ]

    # Creating a bookstore and adding books to it
    bookstore = Bookstore()
    for book in books:
        bookstore.add_book(book)

    # Displaying available books in the bookstore
    bookstore.display_available_books()

    # Creating a customer
    customer = Customer("Leticia", "leticiapyres@gmail.com")
    customer = Customer("Jean", "jean@gmail.com")
    customer = Customer("Osman", "osman@gmail.com")
    customer = Customer("Arthur", "jean@gmail.com")
    customer = Customer("Elyas", "jean@gmail.com")


    # Adding books to the customer's shopping cart
    customer.add_book_to_cart(books[0])
    customer.add_book_to_cart(books[1])

    # Placing an order
    order = customer.place_order()
    order.display_order_summary()

    # Processing the order in the bookstore
    bookstore.process_order(order)

    # Displaying updated available books
    bookstore.display_available_books()
