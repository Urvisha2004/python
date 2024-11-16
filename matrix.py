def input_matrix(Row, Column):

    matrix = []
    
    for row in range(Row):    
        a = []
       
        for column in range(Column):   
            a.append(int(input(f"Enter the value for position ({row}, {column}): ")))
        matrix.append(a)

    return matrix

def print_matrix(matrix):

    Row = len(matrix)
    Column = len(matrix[0])
    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end=" \t")
        print()

def add_matrix(matrix1, matrix2):

    rows = len(matrix1)
    cols = len(matrix1)  
    result_matrix = []

    for row in range(rows):
        result_row = []
        for column in range(cols):
            result_row.append(matrix1[row][column] + matrix2[row][column])
        result_matrix.append(result_row)
    
    return result_matrix

def multiply_matrix(matrix1, matrix2):

    rows = len(matrix1)
    cols = len(matrix1)
    result_matrix = []
    
    for i in range(rows):
        result_row = []
        for j in range(cols):
            sum_product = 0
            for k in range(cols): 
                sum_product = sum_product + matrix1[i][k] * matrix2[k][j]
            result_row.append(sum_product)
        result_matrix.append(result_row)
    
    return result_matrix



