"""
Задание 3:
1. Реализуйте базовый класс Car.
2. У класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
3. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar;
4. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля;
5. Для классов TownCar и WorkCar переопределите метод show_speed. При
значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости. – 3 балла
"""
class Car:
    def __init__(self, name, color, speed=0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость {self.name}: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, name, color, speed=0):
        super().__init__(name, color, speed, is_police=True)


if __name__ == "__main__":
    cars = [
        TownCar("Седан", "белый", 70),
        SportCar("Купе", "красный", 120),
        WorkCar("Грузовик", "синий", 50),
        PoliceCar("Патруль", "белый", 80),
    ]
    for car in cars:
        car.go()
        car.show_speed()
        car.turn("налево")
        car.stop()
