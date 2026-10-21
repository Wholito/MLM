"""
2. Создать программу, которая будет подсчитывать количество слов
четной и нечетной длины в строке, введённой с клавиатуры. – 2 балла
"""

text = input()
words = text.split()
even_count = 0
odd_count = 0
for word in words:
    if len(word) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count, odd_count)
