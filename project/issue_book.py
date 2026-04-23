from utils import books
import datetime

def issue():
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("❌ Book not found!")
        return

    if not books[book_id]["available"]:
        print("⚠️ Book already issued!")
        return

    name = input("Enter Student Name: ")
    days = int(input("Enter number of days: "))

    books[book_id]["available"] = False
    books[book_id]["issued_to"] = name
    books[book_id]["issue_date"] = datetime.date.today()
    books[book_id]["days"] = days

    print("\n📌 Fine Rules:")
    print("Week 1: ₹10/day")
    print("Week 2: ₹20/day")
    print("Week 3: ₹30/day ...\n")

    print(f"✅ Book issued to {name}")