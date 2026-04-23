from utils import books, calculate_fine

def return_book():
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("❌ Book not found!")
        return

    if books[book_id]["available"]:
        print("⚠️ Book was not issued.")
        return

    fine = calculate_fine(
        books[book_id]["issue_date"],
        books[book_id]["days"]
    )

    print(f"\nIssued to: {books[book_id]['issued_to']}")

    if fine > 0:
        print(f"💸 Fine to pay: ₹{fine}")
    else:
        print("✅ Returned on time. No fine!")

    books[book_id]["available"] = True
    books[book_id]["issued_to"] = None
    books[book_id]["issue_date"] = None
    books[book_id]["days"] = 0

    print("📚 Book returned successfully!")