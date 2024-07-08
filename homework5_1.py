class House:
    def __init__(self, name, number_of_floors):
        # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка на допустимость этажа
        if 0 < new_floor <= self.number_of_floors:
            # Вывод последовательности чисел от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(f"Едем на этаж {floor}")
        else:
            # Сообщение об ошибке
            print("Такого этажа не существует")

# Пример использования класса
h1 = House('ЖК Эльбрус', 30)

# Вызов метода go_to
h1.go_to(5)
h1.go_to(-1)
