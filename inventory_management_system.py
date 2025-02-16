class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price}, {self.stock})"
    
def add_book(inventory, title, author, price, stock):
    book = Book(title, author, price, stock)
    inventory.append(book)
    return inventory
    
def update_stock(inventory, title, new_stock):
    for book in inventory:
        if book.title == title:
            book.stock = new_stock
            return inventory
    print(f"No book found with title: {title}")
    return inventory

def get_books_by_author(inventory, author):
    return [book for book in inventory if book.author.lower() == author.lower()]

def total_stock_value(inventory):
    return sum(book.price * book.stock for book in inventory)