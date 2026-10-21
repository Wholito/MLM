"""
Задание 1:
Калькулятор.
Создайте класс, где реализованы функции(методы) математических
операций. А также функция, для ввода данных. – 1 балл
"""
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    def read_and_calculate(self):
        try:
            op = input().strip()
            a = float(input())
            b = float(input())
            if op == "+":
                print(self.add(a, b))
            elif op == "-":
                print(self.sub(a, b))
            elif op == "*":
                print(self.mul(a, b))
            elif op == "/":
                print(self.div(a, b))
        except ValueError:
            print("Ошибка ввода")
        except ZeroDivisionError:
            print("Деление на ноль")


if __name__ == "__main__":
    Calculator().read_and_calculate()
