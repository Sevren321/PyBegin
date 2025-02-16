# Define book class
class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price}, {self.stock})"

# Function to add books to inventory    
def add_book(inventory, title, author, price, stock):
    book = Book(title, author, price, stock)
    inventory.append(book)
    return inventory

# Function to update stock
def update_stock(inventory, title, new_stock):
    for book in inventory:
        if book.title == title:
            book.stock = new_stock
            return inventory
    print(f"No book found with title: {title}")
    return inventory

# Function to get books by author - List Comprehension 
def get_books_by_author(inventory, author):
    return [book for book in inventory if book.author.lower() == author.lower()]

# Function to calculate total stock value
def total_stock_value(inventory):
    return sum(book.price * book.stock for book in inventory)


# Example usage --------------------------------------------------------
inventory = []
add_book(inventory, "1984", "George Orwell", 10.99, 50)
add_book(inventory, "To Kill a Mockingbird", "Harper Lee", 8.99, 30)
add_book(inventory, "Brave New World", "Aldous Huxley", 9.99, 40)

# Update stock
update_stock(inventory, "1984", 60)

# Get books by author
print(get_books_by_author(inventory, "George Orwell"))

# Calculate total stock value
print(f"Total stock value: ${total_stock_value(inventory):.2f}")