import util

M1 = util.matrix_from_csv("matrix1.txt")
M2 = util.matrix_from_csv("matrix2.txt")

util.gauss_jordan_elimination(M1, True)
util.gauss_jordan_elimination(M2, True)

#util.print_matrix(M1)
#util.print_matrix(M2)
print(f"Row equivalency: {M1 == M2}")