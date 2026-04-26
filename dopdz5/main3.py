from random import randint, choice
names = ['ivan', 'john', 'michael']
surnames = ['black', 'white', 'snow']

def full_name(names, surnames):
    name = choice(names)
    surname = choice(surnames)
    fullname = name + ' ' + surname
    account = randint(15000, 35000)
    last_fullname = {'fullname': str(fullname), 'account': f'${account}'}
    return last_fullname


def house():
    houses = []
    for _ in range(50, 100):
        house = {'price': f'${randint(10000, 30000)}', 'square': f'{randint(10, 90)}m2' }
        houses.append(house)
    return houses

def filter(houses, last_fullname):
    result = []
    int_account = int(last_fullname['account'][1:])
    for i in houses:
        if int_account > int(i['price'][1:]):
            result.append(i)
    return sorted(result, key=lambda i: int(i['square'][:-2]), reverse=True)

print(filter(house(), full_name(names, surnames)))



