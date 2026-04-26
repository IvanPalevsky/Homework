class Bank:
    def __init__(self):
        self.account = None

    def open(self):
        self.account = 0
        print("Счет открыт")

    def close(self):
        if self.account is not None:
            print("Счет закрыт")
            self.account = None

    def add(self, sum):
        if self.account is None:
            print("Откройте счет")
            return
        if sum > 0:
            self.account += sum
            print(f"Пополнено на {sum}. Баланс: {self.account}")

    def take(self, sum):
        if self.account is None:
            print("Откройте счет")
            return
        if sum > 0 and sum <= self.account:
            self.account -= sum
            print(f"Снято {sum}")

bank1 = Bank()
bank1.open()
bank1.add(100)
bank1.take(50)