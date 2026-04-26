class Soda:
    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add is not None:
            return f'Газировка с добавкой {self.add}'
        else:
            return 'Обычная газировка'

soda1 = Soda()
print(soda1.show_my_drink())