# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "Машина поехала "
    def stop(self):
        return "Машина остановилась "
    def turn(self, direction):
        return "Автомобиль повернул " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = False):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = False):
        super().__init__(name, speed, color)
        self.family = family

class WorkCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = False):
        super().__init__(name, speed, color)
        self.family = family

class PoliceCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color, True)
        self.family = family

bmw= TownCar('BMW', 60, 'черная')
audi= SportCar('Audi', 80, 'красная')
lada= WorkCar('Lada', 70, 'желтая')
ford= PoliceCar('Ford', 110, 'бело-синий')
print(bmw.name, bmw.color, bmw.speed, bmw.is_police)
print(bmw.go(), bmw.turn('налево'))
print(audi.name, audi.color, audi.speed, audi.is_police)
print(audi.go(), audi.turn('направо'))
print(lada.name, lada.color, lada.speed, lada.is_police)
print(lada.go(), lada.turn('налево'), lada.stop())
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('за Lada'))