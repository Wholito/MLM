"""
Все задания выполнить с использованием функций и обработкой исключительных
ситуаций при помощи блока try\\except\\finally

2. Напишите функцию, которая будет принимать один аргумент. Если в
функцию передаётся словарь, Найдите три ключа с самыми маленькими
значениями .
Если список, то удалить все нулевые элементы, найти произведение
между первым и вторым положительными элементами.
Число – определить количество разрядов.
Строка –определить сколько раз в строке встречается каждый символ,
вывести в виде словаря.
Сделать проверку со всеми этими случаями. – 4 балла
"""
def process(arg):
    if isinstance(arg, dict):
        sorted_items = sorted(arg.items(), key=lambda x: x[1])
        keys = [k for k, v in sorted_items[:3]]
        print(keys)
    elif isinstance(arg, list):
        cleaned = [x for x in arg if x != 0]
        positives = [x for x in cleaned if isinstance(x, (int, float)) and x > 0]
        if len(positives) >= 2:
            print(positives[0] * positives[1])
        else:
            print(0)
    elif isinstance(arg, int):
        print(len(str(abs(arg))) if arg != 0 else 1)
    elif isinstance(arg, str):
        d = {}
        for ch in arg:
            d[ch] = d.get(ch, 0) + 1
        print(d)
    else:
        raise TypeError("unsupported type")


def demo():
    process({"a": 50, "b": 5, "c": 56, "d": 4, "e": 58, "f": 20})
    process([1, 0, 2, 0, 3, -1, 4, 5])
    process(12345)
    process("hello")


if __name__ == "__main__":
    try:
        demo()
    except Exception as e:
        print(e)
    finally:
        pass
