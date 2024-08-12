'''
Домашняя работа по уроку "Перегрузка операторов."
Цель: применить знания о перегурзке арифметических операторов и операторов сравнения.
'''
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# Поскольку метод __len__ для класса House возвращает значение аттрибута
# number_of_floors, будем использовать его в описании специальных методов:

    def __eq__(self, other):
        if isinstance(other, House): return len(self) == len(other)
        elif isinstance(other, int): return len(self) == other
        else: return False

# Для сокращения записей и наглядности, будем использовать if в одну строку
# Также для сокращения можно описывать один метод через другой применяя проверку
# принадлежности аргументов к типу :

    def __ne__(self, other):
        if isinstance(other, House) or isinstance(other, int): return not self == other
        else: return False

    def __lt__(self, other):
        if isinstance(other, House): return len(self) < len(other)
        elif isinstance(other, int): return len(self) < other
        else: return False

    def __ge__(self, other):
        if isinstance(other, House) or isinstance(other, int): return not self < other
        else: return False

    def __gt__(self, other):
        if isinstance(other, House): return len(self) > len(other)
        elif isinstance(other, int): return len(self) > other
        else: return False

    def __le__(self, other):
        if isinstance(other, House) or isinstance(other, int): return not self > other
        else: return False


    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            print('Второе слагаемое должно быть целым числом')

# Реализуем __radd__ и __iadd__ через add:

    def __radd__(self, value):
        if isinstance(value, int):
            return self + value
        else:
            print('Число должно быть целым')

    def __iadd__(self, value):
        if isinstance(value, int):
            return self + value
        else:
            print('Число должно быть целым')

    def go_to(self, new_floor):
        if int(new_floor) < 1 or int(new_floor) > int(self.number_of_floors):
            print('Такого этажа не существует')
        else:
            for i in range(1, int(new_floor) + 1):
                print(i)

# Другие методы арифметических операторов:
    def __sub__(self, other):
        if isinstance(other, House): return House(self.name, len(self) - len(other))
        elif isinstance(other, int): return House(self.name, len(self) - other)
        else: return None

    def __mul__(self, other):
        if isinstance(other, House): return House(self.name, int(len(self) * len(other)))
        elif isinstance(other, int): return House(self.name, int(len(self) * other))
        else: return None

    def __truediv__(self, other):
        if isinstance(other, House): return House(self.name, int(len(self) / len(other)))
        elif isinstance(other, int): return House(self.name, int(len(self) / other))
        else: return None


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

print(h1 - h2)
print(h1 / h2)
print(h1 * h2)


