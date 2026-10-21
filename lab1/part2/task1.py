"""
Все задания выполнить с использованием функций и обработкой исключительных
ситуаций при помощи блока try\\except\\finally

1. Написать функцию для вычисления наибольшего общего делителя. –
2 балла
"""
def gcd(a, b):
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    try:
        x = int(input())
        y = int(input())
        print(gcd(x, y))
    except ValueError:
        print(0)
    finally:
        pass
