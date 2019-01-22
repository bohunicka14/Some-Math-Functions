## Python 3.7

def multiply_L_U(L, U, input_matrix):
    ## resolve first row of U matrix just by adding values from the first row of input matrix
    for col in range(len(L)):
        U[0][col] = input_matrix[0][col]


    ## compute L and U matrix (inplace)
    for row_l in range(1, len(L)):
        for col_u in range(len(U[0])):
            partial_sum = 0
            l_was_none = False
            divider = 0
            result_col, result_row = -1, -1
            unknown_var_found = False
            for i in range(len(U)):
                if L[row_l][i] is None and not unknown_var_found:
                    divider = U[i][col_u]
                    l_was_none = True
                    result_row = row_l
                    result_col = i
                    unknown_var_found = True
                elif U[i][col_u] is None and not unknown_var_found:
                    divider = L[row_l][i]
                    result_row = i
                    result_col = col_u
                    unknown_var_found = True
                else:
                    try:
                        partial_sum += L[row_l][i] * U[i][col_u]
                    except TypeError:
                        pass

            if result_row != -1 and result_col != -1:
                if l_was_none:
                    L[result_row][result_col] = (input_matrix[row_l][col_u] - partial_sum)/divider
                else:
                    U[result_row][result_col] = (input_matrix[row_l][col_u] - partial_sum)/divider
                

def multiply_matrix_y(matrix, vector):
    result = [None] * len(vector)

    ## set first y value
    result[0] = vector[0]

    for row_matrix in range(1, len(matrix)):
        partial_sum = 0
        divider = 0
        for i in range(len(vector)):
            if result[i] is None and matrix[row_matrix][i] != 0:
                divider = matrix[row_matrix][i]
            else:
                try:
                    partial_sum += matrix[row_matrix][i] * result[i]
                except TypeError:
                    pass
        result[row_matrix] = (vector[row_matrix] - partial_sum)/divider

    return result

def multiply_matrix_x(matrix, vector):
    result = [None] * len(vector)

    for row_matrix in range(len(matrix) - 1, -1, -1):
        partial_sum = 0
        divider = 0
        for i in range(len(vector)):
            if result[i] is None and matrix[row_matrix][i] != 0:
                divider = matrix[row_matrix][i]
            else:
                try:
                    partial_sum += matrix[row_matrix][i] * result[i]
                except TypeError:
                    pass
        result[row_matrix] = (vector[row_matrix] - partial_sum)/divider

    return result

def compute(matrix, vector):
    rows = len(matrix)
    cols = len(matrix[0])

    L = []
    U = []
    for i in range(rows):
        L.append([0]*cols)
        U.append([None]*cols)
    
    ## _______fill L matrix_______
    ## insert ones to diagonal
    for r in range(rows):
        for c in range(cols):
            if r == c:
                L[r][c] = 1

    ## insert Nones to lower half
    for r in range(1, rows):
        for c in range(r):
            L[r][c] = None


    ## _______fill U matrix_______
    ## insert zeros to lower half
    for r in range(1, rows):
        for c in range(r):
            U[r][c] = 0

    ## compute L and U matrix
    multiply_L_U(L, U, matrix)

    ## compute vector y
    y = multiply_matrix_y(L, vector)
    x = multiply_matrix_x(U, y)

    return x

def test():
    ## input 
    matrix = [[1,3,5], [4,0,1], [2,3,1]]
    vector = [7,9,5]

    ## result
    print('RESULT: ', compute(matrix, vector))

test()
    
            
