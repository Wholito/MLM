"""
Все задания выполнить с использованием функций и обработкой исключительных
ситуаций при помощи блока try\\except\\finally

3. Найдите индексы первого вхождения минимального элемента.
Выведите два числа: номер строки и номер столбца, в которых стоит
наибольший элемент в двумерном массиве. – 3 балла
"""
def find_min_indices(matrix):
    min_val = matrix[0][0]
    row, col = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                row, col = i, j
    return row, col


if __name__ == "__main__":
    try:
        n = int(input())
        m = int(input())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        r, c = find_min_indices(matrix)
        print(r, c)
    except (ValueError, IndexError) as e:
        print(e)
    finally:
        pass
