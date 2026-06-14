# (B) : Create a library management system:
'''
    1. Members can borrow and return books
    2. Keep track of borrowed books for each member
    3. Calculate fine for overdue books
    4. Generate membership reports
    5. Should work for multiple members simultaneously
        - John borrowed: Python Guide, Clean Code
        - Sarah borrowed: Design Patterns
        - John returns Python Guide but keeps Clean Code
    6. Try solving this problem without OOPS (simple def functions) and with OOPS
'''


# Dictionary to store member books
library_records = {}
book_prices = {
    "Python Guide": 500,
    "Clean Code": 450,
    "Design Patterns": 600,
    "JavaScript Basics": 350
}
daily_fine = 5  # ₹5 per day for overdue books

def add_member(member_name):
    """Add a new member to library"""
    if member_name not in library_records:
        library_records[member_name] = {"books": [], "fine": 0}

def borrow_book(member_name, book_name):
    """Member borrows a book"""
    if member_name not in library_records:
        add_member(member_name)
    library_records[member_name]["books"].append(book_name)
    print(f"{member_name} borrowed: {book_name}")

def return_book(member_name, book_name, days_overdue=0):
    """Member returns a book"""
    if member_name in library_records and book_name in library_records[member_name]:
        library_records[member_name]["books"].remove(book_name)
        fine = days_overdue * daily_fine
        library_records[member_name]["fine"] += fine
        print(f"{member_name} returned: {book_name} | Fine: ₹{fine}")
    else:
        print(f"Book not found in {member_name}'s records")

def generate_report(member_name):
    """Generate membership report"""
    if member_name in library_records:
        print(f"\n{'='*40}")
        print(f"Report for {member_name}:")
        print(f"{'='*40}")
        print(f"Borrowed Books: {', '.join(library_records[member_name]['books']) or 'None'}")
        print(f"Total Fine: ₹{library_records[member_name]['fine']}")
        print(f"{'='*40}")

# Example usage - Procedural approach
print("=== PROCEDURAL APPROACH ===")
add_member("John")
add_member("Sarah")

borrow_book("John", "Python Guide")
borrow_book("John", "Clean Code")
borrow_book("Sarah", "Design Patterns")

return_book("John", "Python Guide", days_overdue=3)
generate_report("John")
generate_report("Sarah")


# Approach 2: With OOP (using Classes)

class Library:
    def __init__(self, daily_fine=5):
        self.books_catalog = {
            "Python Guide": 500,
            "Clean Code": 450,
            "Design Patterns": 600,
            "JavaScript Basics": 350
        }
        self.members = {}
        self.daily_fine = daily_fine

    def add_member(self, member_name):
        """Add a new member to library"""
        if member_name not in self.members:
            self.members[member_name] = {
                "books": [],
                "fine": 0,
                "join_date": "2026-06-14"
            }
            print(f"✓ {member_name} added to library")

    def borrow_book(self, member_name, book_name):
        """Member borrows a book"""
        if member_name not in self.members:
            print(f"Member {member_name} not found. Adding new member...")
            self.add_member(member_name)
        
        if book_name in self.books_catalog:
            self.members[member_name]["books"].append(book_name)
            print(f"✓ {member_name} borrowed: {book_name}")
        else:
            print(f"✗ Book '{book_name}' not in catalog")

    def return_book(self, member_name, book_name, days_overdue=0):
        """Member returns a book"""
        if member_name in self.members:
            if book_name in self.members[member_name]["books"]:
                self.members[member_name]["books"].remove(book_name)
                fine = days_overdue * self.daily_fine
                self.members[member_name]["fine"] += fine
                
                status = f"Fine: ₹{fine}" if fine > 0 else "On time"
                print(f"✓ {member_name} returned: {book_name} | {status}")
            else:
                print(f"✗ Book not found in {member_name}'s borrowed list")
        else:
            print(f"✗ Member {member_name} not found")

    def get_member_info(self, member_name):
        """Get detailed member information"""
        if member_name in self.members:
            member = self.members[member_name]
            print(f"\n{'='*50}")
            print(f"MEMBERSHIP REPORT: {member_name}")
            print(f"{'='*50}")
            print(f"Join Date: {member['join_date']}")
            print(f"Currently Borrowed: {len(member['books'])} book(s)")
            if member['books']:
                for book in member['books']:
                    print(f"  • {book} (₹{self.books_catalog[book]})")
            else:
                print("  • No books borrowed")
            print(f"Total Fine: ₹{member['fine']}")
            print(f"{'='*50}\n")
        else:
            print(f"Member {member_name} not found")

    def get_all_members(self):
        """Display all members and their status"""
        print(f"\n{'='*50}")
        print("ALL MEMBERS")
        print(f"{'='*50}")
        for member_name in self.members:
            member = self.members[member_name]
            print(f"{member_name}: {len(member['books'])} book(s), Fine: ₹{member['fine']}")
        print(f"{'='*50}\n")

# Example usage - OOP approach
print("\n\n=== OOP APPROACH ===")
library = Library(daily_fine=5)

# Add members
library.add_member("John")
library.add_member("Sarah")
library.add_member("Emma")

# Members borrow books
library.borrow_book("John", "Python Guide")
library.borrow_book("John", "Clean Code")
library.borrow_book("Sarah", "Design Patterns")
library.borrow_book("Emma", "JavaScript Basics")

# Generate reports
library.get_member_info("John")
library.get_member_info("Sarah")

# John returns a book (3 days late)
library.return_book("John", "Python Guide", days_overdue=3)

# Emma returns on time
library.return_book("Emma", "JavaScript Basics", days_overdue=0)

# Updated reports
library.get_member_info("John")
library.get_all_members()
