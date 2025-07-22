# ATM Machine Simulator with OOP and Tkinter (Styled GUI)

import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class Account:
    def __init__(self, username, pin, balance=1000.0):
        self.username = username
        self.pin = pin
        self.balance = balance
        self.history = []

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited Rs. {amount:.2f} on {time.ctime()}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew Rs. {amount:.2f} on {time.ctime()}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history if self.history else ["No transactions yet."]

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f4f7")

        self.account = Account("user1", "1234")
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="ATM Login", font=("Helvetica", 18, "bold"), bg="#f0f4f7").pack(pady=20)
        tk.Label(self.root, text="Enter 4-digit PIN:", bg="#f0f4f7", font=("Helvetica", 12)).pack(pady=5)
        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 12))
        self.pin_entry.pack(pady=5)
        tk.Button(self.root, text="Login", font=("Helvetica", 12), bg="#007acc", fg="white", width=15, command=self.authenticate).pack(pady=10)

    def authenticate(self):
        pin = self.pin_entry.get()
        if self.account.check_pin(pin):
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to ATM", font=("Helvetica", 16, "bold"), bg="#f0f4f7").pack(pady=20)
        btn_config = {"font": ("Helvetica", 12), "bg": "#007acc", "fg": "white", "width": 25, "padx": 5, "pady": 5}

        tk.Button(self.root, text="Check Balance", command=self.check_balance, **btn_config).pack(pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit, **btn_config).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw, **btn_config).pack(pady=5)
        tk.Button(self.root, text="Transaction History", command=self.show_history, **btn_config).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 12), bg="#d9534f", fg="white", width=25).pack(pady=20)

    def check_balance(self):
        balance = self.account.get_balance()
        messagebox.showinfo("Balance", f"Current Balance: Rs. {balance:.2f}")

    def deposit(self):
        try:
            amount = float(simpledialog.askstring("Deposit", "Enter amount to deposit:"))
            if self.account.deposit(amount):
                messagebox.showinfo("Success", "Amount deposited successfully")
            else:
                messagebox.showerror("Error", "Invalid amount")
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid input")

    def withdraw(self):
        try:
            amount = float(simpledialog.askstring("Withdraw", "Enter amount to withdraw:"))
            if self.account.withdraw(amount):
                messagebox.showinfo("Success", "Amount withdrawn successfully")
            else:
                messagebox.showerror("Error", "Insufficient balance or invalid amount")
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid input")

    def show_history(self):
        history = "\n".join(self.account.get_history())
        messagebox.showinfo("Transaction History", history)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the ATM app
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
