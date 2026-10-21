"""
Все задания выполнить с использованием функций и обработкой исключительных
ситуаций при помощи блока try\\except\\finally

4. Напишите программу, демонстрирующую работу try\\except\\finally –
2 балла
"""
def divide(a, b):
    return a / b


def main():
    try:
        a = float(input())
        b = float(input())
        result = divide(a, b)
        print(result)
    except ValueError:
        print("Неверный ввод")
    except ZeroDivisionError:
        print("Деление на ноль")
    finally:
        print("Завершение обработки")


if __name__ == "__main__":
    main()
