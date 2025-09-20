import util

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3 ]

num_rows = len(M)
num_cols = len(M[0])

if util.ask_bool("Do you want to input a custom matrix (y/n)? (n): ", False):
    num_rows = util.ask_int("Number of rows: ", 1, float("inf"), default="3", validators=[util.nonzero_finite_value])
    num_cols = util.ask_int("Number of columns: ", 1, float("inf"), default="3", validators=[util.nonzero_finite_value])
    M = [None] * num_rows
    for i in range(num_rows):
        M[i] = util.ask_row("", num_cols, default="0 "*num_cols)

def select_row():
    util.print_matrix(M)
    row_index = util.ask_int("Select row: ", 1, num_rows) - 1
    while True:
        print(f"Row operations for row {row_index+1}")
        util.print_matrix([M[row_index]])
        print("[1] Edit")
        print("[2] rowSwap")
        print("[3] row+")
        print("[4] *row")
        print("[5] *row+")
        print("[6] Select another row")
        print("[7] Exit row selection")

        op = util.ask_int("Select operation: ", 1, 7)
        def elementary_no_same_row(value: int):
            if value == row_index+1:
                raise ValueError(f"Cannot use row {value} to perform elementary row operation on the same row")
        match op:
            case 1:
                M[row_index] = util.ask_row("", num_cols, default=" ".join(map(str, M[row_index])))
            case 2:
                row_swap_index = util.ask_int("Select row to swap with: ", 1, num_rows, validators=[elementary_no_same_row]) - 1
                util.rowSwap(M, row_index, row_swap_index)
            case 3:
                row_add_index = util.ask_int("Select row to add to this row: ", 1, num_rows, validators=[elementary_no_same_row]) - 1
                util.rowAdd(M, row_index, row_add_index)
            case 4:
                scalar = util.ask_num("Input scalar to multiply by: ", validators=[util.nonzero_finite_value])
                util.rowMultiply(M, row_index, scalar)
            case 5:
                row_add_index = util.ask_int("Select row to add to this row: ", 1, num_rows, validators=[elementary_no_same_row]) - 1
                scalar = util.ask_num(f"Input scalar to multiply added row (row {row_add_index+1}) by: ", validators=[util.nonzero_finite_value])
                util.rowAddMultiple(M, row_index, row_add_index, scalar)
            case 6:
                break
            case 7:
                return
    select_row()

def main():
    print("Matrix calculator")
    util.print_matrix(M)
    print("[1] Select row")
    print("[2] ref")
    print("[3] rref")
    print("[4] Exit program")
    op = util.ask_int("Select operation: ", 1, 4)
    match op:
        case 1:
            select_row()
        case 2:
            util.gauss_jordan_elimination(M, reduced=False)
        case 3:
            util.gauss_jordan_elimination(M, reduced=True)
        case 4:
            return
    main()
main()