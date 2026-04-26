class Restorant:
    def __init__(self):
        self.menu = []

    def add(self, dish):
        if dish not in self.menu:
            self.menu.append(dish)
            print(f'{dish} добавлено')

    def remove(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f'{dish} удалено')

    def order(self, ordered):
        print('Ваш заказ:')
        for dish in ordered:
            if dish in self.menu:
                print(dish)

rest = Restorant()
rest.add('chicken')
rest.add('juice')
rest.remove('chicken')
rest.order('chicken')