'''
Домашняя работа по уроку "Различие атрибутов класса и экземпляра.
Берем за основу файл module_5_3 и добавляем код согласно заданию"
'''
class House:
    houses_history = []

    def __new__(cls, *args):#**kwargs не пишем, потому что словарей нет в классе House
        cls.args = args[0]
        cls.houses_history.append(cls.args)
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# Поскольку метод __len__ для класса House возвращает значение атрибута
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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


