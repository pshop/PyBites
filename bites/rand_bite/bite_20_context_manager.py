class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        self.temp = Account()
        return self.temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if sum(self._transactions + self.temp._transactions) > 0:
            self._transactions += self.temp._transactions

if __name__ == '__main__':
    account = Account()
    with account as acc:
        acc - 5
        acc - 5
    print(f"Credit {account.balance}")