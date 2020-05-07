from sympy import symbols, S, var, solve


def new_determinant(matrix_def):
    if len(matrix_def) <= 2:
        if len(matrix_def) == 1:
            return matrix_def[0][0]
        return matrix_def[0][0] * matrix_def[1][1] - matrix_def[1][0] * matrix_def[0][1]
    len_matrix = len(matrix_def)
    determinant = 0
    count_first_row = 0
    while count_first_row != len_matrix:
        multiplier = (-1) ** count_first_row
        matrix_copy = matrix_def.copy()
        matrix_second_copy = []
        del matrix_copy[0]  # удаление первого ряда из матрицы
        for row in matrix_copy:
            row_copy = row.copy()
            del row_copy[count_first_row]  # удаление count_first_row элемента из ряда
            matrix_second_copy.append(row_copy)  # получение уменьшеной матрицы для минора
        sub_det = new_determinant(matrix_second_copy)
        term = (multiplier * matrix_def[0][count_first_row] * sub_det)
        determinant += term
        count_first_row += 1
    return determinant


def input_sole():
    while True:
        int(input('введите количество уравнений: '))
        num_of_rows_1 = int(input('введите количество уравнений: '))
        num_of_columns_1 = int(input('введите количество переменных: '))
        if num_of_rows_1 != num_of_columns_1:
            print("Не удаётся решить систему методом Крамера, введите другую")
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


def matrix_multiplication(matrix_1, matrix_2):
    new_matrix = []
    number_of_columns_2 = len(matrix_2[0])
    for n in matrix_1:  # переход по рядам первой матрицы
        new_row = []
        col_count = -1  # счётчик столбцов
        while col_count != (number_of_columns_2 - 1):
            col_count += 1
            b = -1  # счётчик столбцов
            z = 0  # элемент новой матрицы
            for m in n:
                b += 1
                n_2 = matrix_2[b]
                m_2 = n_2[col_count]
                new_m = m * m_2
                z += new_m
            new_row.append(z)
        new_matrix.append(new_row)
    return new_matrix


while True:
    if input('Нажмите "Enter" (введите пустую строку \'\') для решения '
             'СЛАУ, которые уже имеются в программе: ') != '':
        # Ручной ввод
        matrix, free_members = input_sole()
    else:

        # Тестовая матрица:
        # 3.1) True
        # free_members = [22, -9, 10]
        # matrix = [[3, 4, 5],
        #           [1, -3, -6],
        #           [2, 4, -4]]
        # 3.3) True
        # free_members = [14, 11, 11]
        # matrix = [[2, -1, 1],
        #           [3, 4, -2],
        #           [3, -2, 4]]
        # 3.5) True
        # free_members = [7, 1, 6]
        # matrix = [[2, 1, 3],
        #           [2, 3, 1],
        #           [3, 2, 1]]
        # 3.6) True
        # free_members = [-4, 11, -7]
        # matrix = [[2, -1, 3],
        #           [1, 3, -1],
        #           [1, -2, 2]]
        # 3.8) True
        free_members = [-2, 1, 1]
        matrix = [[1, 1, -1],
                  [4, -3, 1],
                  [2, 1, 5]]
        # 1.9) True
        # free_members = [17, 16, 7]
        # matrix = [[1, 3, 4],
        #           [2, -3, 5],
        #           [3, 4, -1]]

    new_free_members = []
    for i in free_members:
        i = [i]
        new_free_members.append(i)

    main_det = new_determinant(matrix)
    print(main_det)
    if main_det == 0:
        print('Эта система линейных уравнений не решается методом обратной матрицы')
        pass
    inverse_matrix = []
    for l in matrix:
        inverse_matrix.append(l[:])
    for i in range(0, len(free_members)):
        for j in range(0, len(free_members)):
            temporary_matrix = []
            for l in matrix:
                temporary_matrix.append(l[:])
            del temporary_matrix[i]
            for g in range(0, len(temporary_matrix)):
                del temporary_matrix[g][j]
            algebraic_complement = ((-1) ** (i + j)) * new_determinant(temporary_matrix)
            # print(algebraic_complement)
            inverse_matrix[j][i] = S(algebraic_complement) / S(main_det)
    # print(inverse_matrix)
    a = matrix_multiplication(inverse_matrix, new_free_members)
    # print(a)
    for i in range(0, len(a)):
        print(f'X{i + 1} = {a[i][0]}')

    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
