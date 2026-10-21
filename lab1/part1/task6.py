"""
6. Дан кортеж чисел. Определить количество нулевых элементов. –
1 балл
"""
data = input().split()
t = tuple(int(x) for x in data)
print(t.count(0))
