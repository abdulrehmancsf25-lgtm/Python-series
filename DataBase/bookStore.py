from pymongo import MongoClient
from datetime import datetime
import certifi

# ---------- Database Handler ----------
class Database:
    def __init__(self, uri = "mongodb+srv://abdulrehmancsf25_db_user:KKa94Fbs46pKmUty@abdul-data-base.zsaiqz8.mongodb.net/?appName=Abdul-Data-Base", db_name="bookstore"):
        # 1. Get the path to the trusted certificate bundle
        ca = certifi.where()
        
        # 2. Initialize the client with certificates
        self.client = MongoClient(uri, tlsCAFile=ca)
        
        # 3. Test the connection
        try:
            self.client.admin.command('ping')
            print("✓ Connected to MongoDB successfully!")
        except Exception as e:
            print(f"✗ MongoDB connection error: {e}")
            return

        # 4. Collections
        self.db = self.client[db_name]
        self.books = self.db["books"]
        self.users = self.db["users"]
        self.purchases = self.db["purchases"]
        self.reviews = self.db["reviews"]


# ---------- Entities ----------
class Book:
    def __init__(self, title, author, price, stock, category):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        self.category = category

    def to_dict(self):
        return {"title": self.title, "author": self.author, "price": self.price, 
                "stock": self.stock, "category": self.category}

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {"name": self.name, "email": self.email}

class Purchase:
    def __init__(self, user_email, book_title, quantity, total):
        self.user_email = user_email
        self.book_title = book_title
        self.quantity = quantity
        self.total = total
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {"user_email": self.user_email, "book_title": self.book_title,
                "quantity": self.quantity, "total": self.total, "date": self.date}

class Review:
    def __init__(self, user_email, book_title, rating, comment):
        self.user_email = user_email
        self.book_title = book_title
        self.rating = rating
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {"user_email": self.user_email, "book_title": self.book_title,
                "rating": self.rating, "comment": self.comment, "date": self.date}


# ---------- Store Manager ----------
class BookStore:
    def __init__(self, db):
        self.db = db

    def add_book(self, book):
        self.db.books.insert_one(book.to_dict())
        print(f"✓ Book '{book.title}' added.")

    def add_user(self, user):
        if self.db.users.find_one({"email": user.email}):
            print("User already exists.")
            return
        self.db.users.insert_one(user.to_dict())
        print(f"✓ User '{user.name}' added.")

    def view_menu(self):
        print("\n📚 --- Book Menu (By Category) ---")
        categories = self.db.books.distinct("category")
        for cat in categories:
            print(f"\n[{cat.upper()}]")
            for b in self.db.books.find({"category": cat}):
                status = "In Stock" if b['stock'] > 0 else "Out of Stock"
                print(f"  - {b['title']} by {b['author']} | ₹{b['price']} | {status} ({b['stock']})")

    def buy_book(self, email, title, qty=1):
        user = self.db.users.find_one({"email": email})
        book = self.db.books.find_one({"title": title})
        
        if not user: return print("✗ User not found.")
        if not book: return print("✗ Book not found.")
        
        if book["stock"] <= 0:
            return print(f"✗ Sorry, '{title}' is Out of Stock.")
        if book["stock"] < qty:
            return print(f"✗ Not enough stock. Available: {book['stock']}")

        total = book["price"] * qty
        self.db.books.update_one({"title": title}, {"$inc": {"stock": -qty}})
        self.db.purchases.insert_one(Purchase(email, title, qty, total).to_dict())
        print(f"✓ {user['name']} bought {qty} x '{title}' for ₹{total}")

    def add_review(self, email, title, rating, comment):
        user = self.db.users.find_one({"email": email})
        book = self.db.books.find_one({"title": title})
        if not user or not book:
            return print("✗ User or Book not found.")
        
        self.db.reviews.insert_one(Review(email, title, rating, comment).to_dict())
        print(f"✓ Review added for '{title}'.")

    def view_reviews(self, title):
        print(f"\n⭐ --- Reviews for '{title}' ---")
        reviews = list(self.db.reviews.find({"book_title": title}))
        if not reviews:
            print("No reviews yet.")
            return
        for r in reviews:
            print(f"{r['rating']}/5 ⭐ by {r['user_email']} on {r['date']}: {r['comment']}")

    def view_purchases(self):
        print("\n🧾 --- Purchase History ---")
        for p in self.db.purchases.find():
            print(f"{p['date']} | {p['user_email']} | {p['quantity']} x '{p['book_title']}' → ₹{p['total']}")


# ---------- Demo ----------
if __name__ == "__main__":
    # Initialize DB with your Atlas URI
    store = BookStore(Database())

    # 1. Seed Users
    store.add_user(User("Alice", "alice@mail.com"))
    store.add_user(User("Bob", "bob@mail.com"))

    # 2. Seed Books (3 Categories: Fiction, Technology, Self-Help)
    store.add_book(Book("The Alchemist", "Paulo Coelho", 400, 5, "Fiction"))
    store.add_book(Book("Python Basics", "John Doe", 300, 3, "Technology"))
    store.add_book(Book("Atomic Habits", "James Clear", 250, 0, "Self-Help")) # 0 stock

    # 3. Display Menu grouped by Category
    store.view_menu()

    # 4. Try buying books (One in stock, one out of stock)
    print("\n--- Attempting Purchases ---")
    store.buy_book("alice@mail.com", "Python Basics", 2)  # Success
    store.buy_book("bob@mail.com", "Atomic Habits", 1)     # Fails (Out of stock)

    # 5. Users add Reviews
    print("\n--- Adding Reviews ---")
    store.add_review("alice@mail.com", "Python Basics", 5, "Great for beginners!")
    store.add_review("bob@mail.com", "The Alchemist", 4, "Very inspiring story.")
    
    # 6. View Reviews for a book
    store.view_reviews("Python Basics")