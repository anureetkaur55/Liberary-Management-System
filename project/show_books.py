from utils import books

def show():
    print("\n📚 Available Books:\n")

    if not books:
        print("❌ No books available.")
        return

    for book_id, data in books.items():
        status = "Available" if data["available"] else f"Issued to {data['issued_to']}"

        print(f"ID: {book_id}")
        print(f"Title: {data['title']}")
        print(f"Status: {status}")
        print("-" * 30)