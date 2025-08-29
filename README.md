# 🐍 Python OOP Challenge

## 📌 Description
This project demonstrates core **Object-Oriented Programming (OOP)** concepts in Python, including:

- **Classes and Objects**  
- **Constructors (__init__)**  
- **Encapsulation**: Hiding internal details and exposing only what’s necessary.  
- **Inheritance**: Reusing attributes and methods from parent classes.  
- **Polymorphism**: Using the same method name in different classes with different behaviors.  

---

## 🖥️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Feven-Zeray/oop_class_challenge.git
cd oop_class_challenge
Run the Python file containing your classes, for example:

bash
Copy code
python oop_challenge.py
Follow the program prompts to test class behavior, encapsulation, inheritance, or polymorphism.

📂 Example: Encapsulation
python
Copy code
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Output: 150
Attempting print(account.__balance) will raise an error, demonstrating encapsulation.

