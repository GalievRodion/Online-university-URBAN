import random
print('Сегодня в классе дежурят ')


def print_paras():
    name = ['Сергей', 'Инна', 'Вячеслав', 'Антон', 'Иван']
    name1 = random.choice(name)
    return name1
    name2 = random.choice(name)
    return name2
name1 = print_paras()
name2 = print_paras()

print(name1, 'и', name2)