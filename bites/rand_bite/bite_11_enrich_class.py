class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # length of the object: len(acc) returns the number of transactions
    def __len__(self):
        return len(self._transactions)

    # account comparison: acc1 >,<,>=.<=,== acc2 returns a boolean comparing account balances
    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        return False

    def __ge__(self, other):
        if self.balance >= other.balance:
            return True
        return False

    def __lt__(self, other):
        if self.balance < other.balance:
            return True
        return False

    def __le__(self, other):
        if self.balance <= other.balance:
            return True
        return False

    def __eq__(self, other):
        if self.balance == other.balance:
            return True
        return False

    # indexing: acc[n] shows the nth transaction onaccount (0 based)
    def __getitem__(self, item):
        return self._transactions[item]

    # iteration: list(acc) returns a sequence of account transactions
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self._transactions):
            transaction = self._transactions[self.n]
            self.n += 1
            return transaction
        else:
            raise StopIteration

    # operator overloading: acc + int and acc - int can be used to add/subtract money
    def __add__(self, credit):
        self._transactions.append(int(credit))

    def __sub__(self, debit):
        self._transactions.append(int(debit) * -1)

    # string representation: str(acc) returns NAME account - balance: INT
    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"

if __name__ == '__main__':
    my_account = Account('Paul')
    print(f"nom: {my_account.name}")
    print(f"balance: {my_account.balance}")
    print(f"length: {len(my_account)}")

    print("15 credited")
    my_account + 15
    print(f"new balance: {my_account.balance}")
    print(f"new length: {len(my_account)}")

    print("10 debited")
    my_account - 10
    print(f"new balance: {my_account.balance}")
    print(f"new length: {len(my_account)}")

    print(my_account)
