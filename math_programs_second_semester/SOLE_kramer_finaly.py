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


while True:
    if input('Нажмите "Enter" (введите пустую строку \'\') для решения '
             'СЛАУ, которые уже имеются в программе: ') != '':
        # Ручной ввод
        matrix, free_members = input_sole()
    else:

        # Тестовая матрица:
        # 9) True
        # free_members = [164, -96, -32]
        # matrix = [[5, -4, -10],
        #           [-1, 9, 7],
        #           [7, 3, 9]]
        # 4) True
        free_members = [-63, 33, 19]
        matrix = [[-11, 6, -11],
                  [6, 9, -4],
                  [9, 4, 7]]
        # 5) True
        # free_members = [79, 21, 74]
        # matrix = [[8, -8, -3],
        #           [2, 0, -3],
        #           [8, -11, 1]]
        # 8) True
        # free_members = [9, -2, 24]
        # matrix = [[2, -7, 5],
        #           [1, 5, -5],
        #           [4, -2, 7]]
        # 9) True
        # free_members = [17, 16, 7]
        # matrix = [[1, 3, 4],
        #           [2, -3, 5],
        #           [3, 4, -1]]
        # True
        # free_members = [12, 6, 7]
        # matrix = [[1, 3, 2],
        #           [4, 5, 7],
        #           [9, 6, 8]]
    sw1 = False
    sw2 = True
    main_det = new_determinant(matrix)
    # print(f'Детерменант вашей матрицы: {main_det}')
    if main_det == 0:
        sw1 = True
    result = []
    for i in range(0, len(free_members)):
        new_matrix = []
        for l in matrix:
            new_matrix.append(l[:])
        for j in range(0, len(free_members)):
            new_matrix[j][i] = free_members[j]

        x_det = new_determinant(new_matrix)
        if x_det != 0:
            sw2 = False
        if sw1 and not sw2:
            print("Система линейных уравнений решений не имеет")
            break
        if sw1:
            continue
        result.append(S(x_det) / S(main_det))
    if sw1 and sw2:
        print('Система линейных уравнений имеет бесчисленное множество решений')
    if result:
        # print(result)
        for i in range(0, len(result)):
            print(f'X{i + 1} = {result[i]}')
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
