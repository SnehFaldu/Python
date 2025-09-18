class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)
    def display(self):
        print("Book Details:")
        print(f"  Title : {self.title}")
        print(f"  Author: {self.author}")
        print(f"  Price : ₹{self.price:.2f}")
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            print("Invalid discount percent. It must be between 0 and 100.")
            return
        discount_amount = (percent / 100.0) * self.price
        self.price -= discount_amount
        if self.price < 0:
            self.price = 0.0
    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, price={self.price:.2f})"
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 300)
book.display()
book.apply_discount(10)
book.display()