class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    # Getter Methods
    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder  # Fixed typo here

    def get_balance(self):
        return self._balance


# Example usage
if __name__ == "__main__":
    # Create an account
    my_account = BankAccount(account_number="fje2iop755234",
                             account_holder="Dotty loggs", balance=10.0)

    print("Account Number:", my_account.get_account_number())  # Fixed method call
    print("Account Holder:", my_account.get_account_holder())  # Fixed method call
    print("Balance:", my_account.get_balance())  # Fixed method call
