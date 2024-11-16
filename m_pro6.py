import matrix as m

print("\n 1 Matrix")


Row = int(input("\nenter number of row in matrix 1:- "))
Column = int(input("enter number of column in matrix 1:-"))


matrix1 = m.input_matrix(Row, Column)


print("\n 2 matrix")


Row1 = int(input("\nenter number of row in matrix 2 :-"))
Column1 = int(input("enter number of coumn in matrix 2 :-"))


matrix2 = m.input_matrix(Row1, Column1)


print("\n1. add")
print("2. multiplication")


a = input("\n enter the choice :-")

match a:

    case '1':

        if Row == Row1 and Column == Column1:
        
            add_matrix = m.add_matrix(matrix1, matrix2)

            print("\nreuslt matrix of add:- \n ")
            m.print_matrix(add_matrix)
           

        else:

            print("\n not possible rowand column are not match.")
        
    case '2':

        if Column == Row1:

            mul_matrix = m.multiply_matrix(matrix1, matrix2)

            print("\nresult matrix of multiplication \n ")
            m.print_matrix(mul_matrix)

        else:

            print("\n multiplication is not possible beacase not possible row and column.")
        