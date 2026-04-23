from utils import books

def add():
    book_id = input("Enter Book ID: ")
    
    if book_id in books:
        print("⚠️ Book already exists!")
        return

    title = input("Enter Book Name: ").upper()

    books[book_id] = {
        "title": title,
        "available": True,
        "issued_to": None,
        "issue_date": None,
        "days": 0
    }

    print(f"✅ Book '{title}' added successfully!")