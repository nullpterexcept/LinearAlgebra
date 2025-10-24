import util
M = None
if util.ask_bool("Do you want to input a custom matrix (y/n)? (n): ", False):
    num_rows = util.ask_int("Number of rows: ", 1, float("inf"), default="3", validators=[util.nonzero_finite_value])
    num_cols = util.ask_int("Number of columns: ", 1, float("inf"), default="3", validators=[util.nonzero_finite_value])
    M = [None] * num_rows
    for i in range(num_rows):
        M[i] = util.ask_row("", num_cols, default="0 "*num_cols)
else:
    M = util.matrix_from_csv("matrix.txt")

util.gauss_jordan_elimination(M, True)
print("Your row reduced matrix is: ")
util.print_matrix(M)