import csv
import threading
import time


class Customer:
    def __init__(self, customer_id, name, account_balance, account_type):
        self.customer_id = customer_id
        self.name = name
        self.account_balance = float(account_balance)
        self.account_type = account_type
        self.transactions = []

    def deposit(self, amount):
        self.account_balance += amount
        self.transactions.append(f"Deposited {amount}. New balance: {self.account_balance:.2f}")
        print(f"{self.name}: Deposited {amount}. New balance: {self.account_balance:.2f}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.transactions.append(f"Withdrew {amount}. New balance: {self.account_balance:.2f}")
            print(f"{self.name}: Withdrew {amount}. New balance: {self.account_balance:.2f}")
        else:
            print(f"{self.name}: Insufficient balance.")

    def view_transactions(self):
        print(f"\nTransaction history for {self.name}:")
        if not self.transactions:
            print("No transactions found.")
        for transaction in self.transactions:
            print(transaction)


class BankingSystem:
    def __init__(self, data_file):
        self.customers = {}
        self.data_file = data_file
        self.lock = threading.Lock()
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    customer_id, name, account_balance = row
                    account_type = "savings" if float(account_balance) > 5000 else "current"
                    self.customers[customer_id] = Customer(customer_id, name, account_balance, account_type)
        except FileNotFoundError:
            print(f"Error: File {self.data_file} not found.")
        except Exception as e:
            print(f"Error reading data file: {e}")

    def save_data(self):
        with open(self.data_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["CustomerID", "Name", "AccountBalance"])
            for customer in self.customers.values():
                writer.writerow([customer.customer_id, customer.name, customer.account_balance])

    def create_account(self):
        customer_id = input("Enter a unique Customer ID: ").strip()
        if customer_id in self.customers:
            print("Customer ID already exists. Try again.")
            return

        name = input("Enter customer name: ").strip()
        try:
            initial_balance = float(input("Enter initial account balance: ").strip())
        except ValueError:
            print("Invalid balance. Please enter a numeric value.")
            return

        account_type = input("Enter account type (savings/current): ").strip().lower()
        if account_type not in ["savings", "current"]:
            print("Invalid account type. Please choose 'savings' or 'current'.")
            return

        self.customers[customer_id] = Customer(customer_id, name, initial_balance, account_type)
        self.save_data()
        print(f"Account for {name} created successfully!")

    def delete_account(self):
        customer_id = input("Enter Customer ID to delete: ").strip()
        if customer_id not in self.customers:
            print("Customer not found.")
            return

        confirmation = input(f"Are you sure you want to delete account {customer_id}? (yes/no): ").strip().lower()
        if confirmation == "yes":
            del self.customers[customer_id]
            self.save_data()
            print(f"Account {customer_id} deleted successfully!")
        else:
            print("Account deletion cancelled.")

    def transfer_funds(self):
        sender_id = input("Enter Sender Customer ID: ").strip()
        if sender_id not in self.customers:
            print("Sender customer not found.")
            return

        receiver_id = input("Enter Receiver Customer ID: ").strip()
        if receiver_id not in self.customers:
            print("Receiver customer not found.")
            return

        try:
            amount = float(input("Enter amount to transfer: ").strip())
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        sender = self.customers[sender_id]
        receiver = self.customers[receiver_id]

        if sender.account_balance >= amount:
            sender.account_balance -= amount
            receiver.account_balance += amount
            sender.transactions.append(f"Transferred {amount} to {receiver.name}. New balance: {sender.account_balance:.2f}")
            receiver.transactions.append(f"Received {amount} from {sender.name}. New balance: {receiver.account_balance:.2f}")
            self.save_data()
            print(f"Successfully transferred {amount} from {sender.name} to {receiver.name}.")
        else:
            print(f"{sender.name} has insufficient balance for this transaction.")

    def search_account_by_name(self):
        name = input("Enter customer name to search: ").strip().lower()
        found = False
        for customer in self.customers.values():
            if customer.name.lower() == name:
                print(f"Customer found: ID = {customer.customer_id}, Name = {customer.name}, Balance = {customer.account_balance:.2f}")
                found = True
        if not found:
            print("No customer found with that name.")

    def run(self):
        while True:
            print("\n======== Banking System ========")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Transactions")
            print("4. Create New Account")
            print("5. Delete Account")
            print("6. Transfer Funds")
            print("7. Search Account by Name")
            print("8. Quit")
            print("================================")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                customer_id = input("Enter Customer ID: ").strip()
                if customer_id not in self.customers:
                    print("Customer not found.")
                else:
                    try:
                        amount = float(input("Enter amount to deposit: ").strip())
                        self.customers[customer_id].deposit(amount)
                        self.save_data()
                    except ValueError:
                        print("Invalid amount. Please enter a numeric value.")
            elif choice == "2":
                customer_id = input("Enter Customer ID: ").strip()
                if customer_id not in self.customers:
                    print("Customer not found.")
                else:
                    try:
                        amount = float(input("Enter amount to withdraw: ").strip())
                        self.customers[customer_id].withdraw(amount)
                        self.save_data()
                    except ValueError:
                        print("Invalid amount. Please enter a numeric value.")
            elif choice == "3":
                customer_id = input("Enter Customer ID: ").strip()
                if customer_id in self.customers:
                    self.customers[customer_id].view_transactions()
                else:
                    print("Customer not found.")
            elif choice == "4":
                self.create_account()
            elif choice == "5":
                self.delete_account()
            elif choice == "6":
                self.transfer_funds()
            elif choice == "7":
                self.search_account_by_name()
            elif choice == "8":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    banking_system = BankingSystem("Data.csv")
    banking_system.run()

          
