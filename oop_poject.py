# (A) : Create a backend bill system for building in a coffee shop:
'''
    1. Take order from user and calculate their price
    2. Keep updateing the total price for all product they ordered
    3. Generate bill
    4. Should work for multiple customers simultaneously
        - Alex = Coffee + Cookie
        - Bob  = Cookie
        Alex made a second order for coffee --> Update alex bill with recent coffee
    5. Try solving this problem without OOPS (simple def functions) and with OOPS
'''


# Dictionary to store customer bills
bills = {}

def take_order(customer, items):
    """Take order and update bill"""
    if customer not in bills:
        bills[customer] = []
    bills[customer].extend(items)

def calculate_total(customer):
    """Calculate total bill for a customer"""
    total = sum(menu[item] for item in bills[customer])
    return total

def generate_bill(customer):
    """Generate bill for a customer"""
    print(f"\nBill for {customer}:")
    for item in bills[customer]:
        print(f"- {item} : ₹{menu[item]}")
    print(f"Total: ₹{calculate_total(customer)}")

# Example usage
take_order("Alex", ["coffee", "cookie"])
take_order("Bob", ["cookie"])
take_order("Alex", ["coffee"])  # Alex orders again

generate_bill("Alex")
generate_bill("Bob")

# Approach 2: With OOP (using Classes)

class CoffeeShop:
    def __init__(self):
        self.menu = {
            "coffee": 50,
            "cookie": 30,
            "sandwich": 70
        }
        self.bills = {}

    def take_order(self, customer, items):
        """Take order and update bill"""
        if customer not in self.bills:
            self.bills[customer] = []
        self.bills[customer].extend(items)

    def calculate_total(self, customer):
        """Calculate total bill for a customer"""
        return sum(self.menu[item] for item in self.bills[customer])

    def generate_bill(self, customer):
        """Generate bill for a customer"""
        print(f"\nBill for {customer}:")
        for item in self.bills[customer]:
            print(f"- {item} : ₹{self.menu[item]}")
        print(f"Total: ₹{self.calculate_total(customer)}")

# Example usage
shop = CoffeeShop()
shop.take_order("Alex", ["coffee", "cookie"])
shop.take_order("Bob", ["cookie"])
shop.take_order("Alex", ["coffee"])  # Alex orders again

shop.generate_bill("Alex")
shop.generate_bill("Bob")
