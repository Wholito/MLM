"""
3. Дан список. Выведите те его элементы, которые встречаются в
списке только один раз. Элементы нужно выводить в том порядке, в
котором они встречаются в списке. Найдите сумму между первым и
последним нулевым элементом. – 2 балла
"""
data = input().split()
lst = []
for x in data:
    try:
        lst.append(int(x))
    except ValueError:
        lst.append(x)

counts = {}
for item in lst:
    counts[item] = counts.get(item, 0) + 1

unique = [item for item in lst if counts[item] == 1]
print(*unique)

zeros = [i for i, v in enumerate(lst) if v == 0]
if len(zeros) >= 2:
    s = sum(lst[zeros[0] + 1:zeros[-1]])
    print(s)
else:
    print(0)
