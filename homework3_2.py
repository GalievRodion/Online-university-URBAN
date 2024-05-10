#Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=2, b=3, c=4)
print_params(b = 25)
print_params(c = [1,2,3])

#Распаковка параметров:
values_list = [True, 2, "str"]
values_disk = {'a': 2.3, 'b': "int", 'c': 4}

print_params(*values_list)
print_params(**values_disk)

#Распаковка + отдельные параметры:
values_list_2 = ['строка', False]
print_params(*values_list_2, 42)
