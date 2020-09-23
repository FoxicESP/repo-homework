# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
#Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"profit": profit, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_full_profit). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + self.surname + self.position
    def get_full_profit(self):
        self.__income = {'основной зароботок =': self.profit, 'Премия =': self.bonus}
        return self.__income

manager = Position('Ольга ', 'Иванова ', '- Дизайнер', 80000, 15000)
print(manager.get_full_name(), manager.get_full_profit())