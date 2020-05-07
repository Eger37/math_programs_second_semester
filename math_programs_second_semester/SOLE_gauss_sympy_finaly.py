from sympy import symbols, S, var, solve


# systems of linear equations
def gauss_def_first(matrix_def):
    column_count = 0
    limiter = len(matrix_def[0])
    if len(matrix_def) < limiter:
        limiter = len(matrix_def)
    while column_count != limiter:
        raw_count = 1 + column_count
        while raw_count != len(matrix_def):
            a = S(matrix_def[column_count][column_count])
            if a == 0:
                matrix_def[column_count], matrix_def[column_count + 1] = matrix_def[column_count + 1], matrix_def[
                    column_count]
                a = S(matrix_def[column_count][column_count])
            b = S(matrix_def[raw_count][column_count])
            if b == 0:
                raw_count += 1
                continue
            coefficient = b / a
            element_count = 0
            new_raw = []
            for element in matrix_def[column_count]:
                new_element = S(matrix_def[raw_count][element_count] - element * coefficient)
                # print(new_element)
                new_raw.append(new_element)
                element_count += 1
            matrix_def[raw_count] = new_raw
            raw_count += 1
            # print(matrix_def)
        column_count += 1
    return matrix_def


def input_sole():
    while True:
        int(input('введите количество уравнений: '))
        num_of_rows_1 = int(input('введите количество уравнений: '))
        num_of_columns_1 = int(input('введите количество переменных: '))
        if num_of_rows_1 < num_of_columns_1:
            print("Система либо несовместна, либо имеет бесконечно много решений, введите другую")
            continue
        print('Ввод коэфициентов основной матрицы: \n')
        matrix_def = input_matrix(num_of_columns_1, num_of_rows_1)
        print('Ввод свободных членов системы: \n')
        free_members_def = input_free_members(num_of_columns_1)
        return matrix_def, free_members_def


def input_matrix(number_of_columns=3, number_of_rows=3):
    i_def = 0
    matrix_def = []
    while i_def != number_of_rows:
        j_def = 0
        row = []
        while j_def != number_of_columns:
            row.append(float(input('значение элемента {} ряда, {} столбца: '.format(i_def + 1, j_def + 1))))
            j_def += 1
        matrix_def.append(row)
        i_def += 1
    return matrix_def


def input_free_members(number_of_columns=3):
    i_def = 0
    free_members_def = []
    while i_def != number_of_columns:
        free_members_def.append(float(input('значение элемента {} ряда, столбца: '.format(i_def + 1))))
        i_def += 1
    return free_members_def


while True:
    # if input('Нажмите "Enter" (введите пустую строку \'\') для решения '
    #          'СЛАУ, которые уже имеются в программе: ') != '':
    #     # Ручной ввод
    #     matrix, free_members = input_sole()
    # else:

    # Тестовая матрица:
    # True
    # free_members = [12, -10, 6]
    # matrix = [[1, 3, -6],
    #           [3, 2, 5],
    #           [2, 5, -3]]
    # True
    # free_members = [4, 7, 12]
    # matrix = [[2, -1, 1],
    #           [1, 3, -1],
    #           [3, -1, 4], ]
    # True
    # free_members = [12, 6, 7]
    # matrix = [[1, 3, -6],
    #           [3, 2, 5],
    #           [3, 2, 5], ]
    # True
    # free_members = [0, 14, 16]
    # matrix = [[5, -1, 3],
    #           [1, 2, 3],
    #           [4, 3, 2], ]
    # True
    # free_members = [0, 0, 0]
    # matrix = [[3, 2, -1],
    #           [1, 2, 9],
    #           [1, 1, 2], ]
    # True
    # free_members = [1, -33, -6, 10]
    # matrix = [[0, 2, 1, 5],
    #           [4, -10, -4, 3],
    #           [9, 2, -2, 5],
    #           [2, 1, 2, 4], ]
    # 9) True
    # free_members = [1, -33, -6, 10]
    # matrix = [[2, 2, 1, 5],
    #           [4, -10, -4, 3],
    #           [9, 2, -2, 5],
    #           [2, 1, 2, 4], ]

    # 10) True
    free_members = [4, 7, 12]
    matrix = [[2, -1, 1],
              [3, 2, -1],
              [3, -1, 4], ]

    # True
    # free_members = [12, 6, 7]
    # matrix = [[1, 3, 2],
    #           [4, 5, 7],
    #           [9, 6, 8]]

    x = var(f'x:{len(matrix[0])}', real=True)

    for fm in range(0, len(matrix)):
        matrix[fm].append(free_members[fm])
    print('так выглядит расширенная матрица вашей системы:')
    for line in matrix:
        print(line)
    matrix = gauss_def_first(matrix)
    # matrix = gauss_def_second(matrix)
    if matrix[-1][-2] == 0:
        if matrix[-1][-1] != 0:
            print("Система несовместима, введите другую")
            break
        del matrix[-1]

    print('так выглядит треугольная расширенная матрица вашей системы:')
    for line in matrix:
        print(line)

    if len(matrix) < len(matrix[0]) - 1:
        print("Система имеет бесконечно много решений: ")
    else:
        print("Ответ: ")
    values_of_x = {}
    i_of_line = 0
    for line in matrix:
        exp = 0
        for i in range(0, len(line) - 1):
            xn = x[i]
            xc = S(line[i])
            exp += xn * xc
        exp -= S(line[-1])
        y = solve(exp, symbols(f'x{i_of_line}', real=True))
        values_of_x[f'x{i_of_line}'] = y[0]
        # print(exp)
        # print(values_of_x)
        i_of_line += 1
    for j in range(len(matrix) - 1, 0, -1):
        for i in range(len(matrix) - 2, -1, -1):
            new_value = values_of_x.get(f'x{i}').subs(x[j], values_of_x.get(f'x{j}'))
            values_of_x[f'x{i}'] = new_value
    print(values_of_x)
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
