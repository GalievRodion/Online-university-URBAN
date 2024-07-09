class House:
    def __init__(self, name, number_of_floors):
        # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): # __lt__(<)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other): # __le__(<=)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):  # __gt__(>)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # __ge__(>=)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # __ne__(!=)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

#__radd__(self, value), __iadd__(self, value) -
#работают так же как и __add__ (возвращают результат его вызова)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вызов метода str
print(h1)
print(h2)
# Вызов метода __len__
#print(len(h1))
#print(len(h2))

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)
print(h1 == h2)

print(h1 == h2) #Вызов метода __eq__
print(h1 < h2) #Вызов метода __lt__
print(h1 <= h2) #Вызов метода __le__
print(h1 > h2) #Вызов метода __gt__
print(h1 >= h2) #Вызов метода __ge__
print(h1 != h2) #Вызов метода __ne__