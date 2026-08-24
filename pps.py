from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card.")


# Concrete Strategy 2
class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using Debit Card.")


# Concrete Strategy 3
class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using UPI.")


# Concrete Strategy 4
class NetBankingPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using Net Banking.")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Driver Code
print("Payment Methods")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: ₹"))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = DebitCardPayment()
elif choice == 3:
    strategy = UpiPayment()
elif choice == 4:
    strategy = NetBankingPayment()
else:
    print("Invalid choice!")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)