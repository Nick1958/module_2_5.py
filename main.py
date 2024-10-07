# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix (n, m, value):  # Объявляем функцию get_matrix с параметрами n, m и value
    matrix = []   # Создаем пустой список matrix внутри функции get_matrix.
    for i in range(n):  # первый цикл for для n строк матрицы
        matrix.append([]) # добавляем пустой список в список matrix.
        for j in range(m):  #  второй цикл for для m столбцов матрицы
            matrix[i].append(value) # пополняем список значениями valuе
    print(matrix)
get_matrix(4, 2, 13)   #  для n=4, m=2, value=13
