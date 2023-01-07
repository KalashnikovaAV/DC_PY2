import doctest


class Shirt:
    def __init__(self, code_: str, company: str, size_: int):
        if not isinstance(code_, str):
            raise TypeError('Не тот тип для кода. Ожидается str')
        self.code = code_
        if not isinstance(company, str):
            raise TypeError('Не тот тип для компании. Ожидается str')
        self.company = company
        if size_ <= 0:
            raise TypeError('Размера меньше 0 не существует')
        self.size = size_


class Perfume:
    def __init__(self, name: str, notes: int, volume: int):
        if not isinstance(name, str):
            raise TypeError('Не тот тип для названия. Ожидается str')
        self.name = name
        if notes > 1:
            raise ValueError('Количесвто нот не должно превышать 1')
        self.notes = notes
        if not volume > 30:
            raise ValueError('Ожидаемый объем флакона 100')
        self.volume = volume


class Bicycle:
    def __init__(self, type_: str, gender: str, wheels):
        if not isinstance(type_, str):
            raise TypeError('Не тот тип для типа велосипеда. Ожидается str')
        self.type_ = type_
        if not isinstance(gender, str):
            raise TypeError('Не тот тип для обозначения пола. Ожидается str')
        self.gender = gender
        if wheels <= 0:
            raise ValueError('У велосипеда 2 колеса')
        self.wheels = wheels

    def broken(self):
        print('Велосипед не едет')
        self.health = 0


if __name__ == "__main__":
    shirt_1 = Shirt('484647', company="Ивановский текстиль", size_=44)
    shirt_2 = Shirt('484253', company="Nike", size_=40)
    perfume_1 = Perfume('Molecule 02', notes=1, volume=100)
    perfume_2 = Perfume('Molecule 04', notes=1, volume=100)
    bicycle_1 = Bicycle('горный', gender="мужской", wheels=2)
    bicycle_2 = Bicycle('городской', gender="женский", wheels=2)

    doctest.testmod()
    pass
