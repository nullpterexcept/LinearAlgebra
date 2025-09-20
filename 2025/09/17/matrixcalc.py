import util
from math import isfinite
from tabulate import tabulate

def nonzero_finite_value(value: float):
    if value == 0 or not isfinite(value):
        raise ValueError(f"{value} is not nonzero and finite")

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3 ]

num_rows = len(M)
num_cols = len(M[0])

if util.ask_bool("Do you want to input a custom matrix (y/n)? (n): ", False):
    num_rows = util.ask_int("Number of rows: ", 1, float("inf"), default="3", validators=[nonzero_finite_value])
    num_cols = util.ask_int("Number of columns: ", 1, float("inf"), default="3", validators=[nonzero_finite_value])
    M = [None] * num_rows
    for i in range(num_rows):
        M[i] = util.ask_row("", num_cols, default="0 "*num_cols)

def select_row():
    print(tabulate(M))
    row_index = util.ask_int("Select row: ", 1, num_rows) - 1
    while True:
        print(f"Row operations for row {row_index+1}")
        print(tabulate([M[row_index]]))
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
                k = M[row_index]
                M[row_index] = M[row_swap_index]
                M[row_swap_index] = k
            case 3:
                row_add_index = util.ask_int("Select row to add to this row: ", 1, num_rows, validators=[elementary_no_same_row]) - 1
                for i in range(num_cols):
                    M[row_index][i] += M[row_add_index][i]
            case 4:
                scalar = util.ask_num("Input scalar to multiply by: ", validators=[nonzero_finite_value])
                for i in range(num_cols):
                    M[row_index][i] *= scalar
            case 5:
                row_add_index = util.ask_int("Select row to add to this row: ", 1, num_rows, validators=[elementary_no_same_row]) - 1
                scalar = util.ask_num(f"Input scalar to multiply added row (row {row_add_index+1}) by: ", validators=[nonzero_finite_value])
                for i in range(num_cols):
                    M[row_index][i] += scalar * M[row_add_index][i]
            case 6:
                break
            case 7:
                return
    select_row()

def main():
    print("Matrix calculator")
    print(tabulate(M))
    print("[1] Select row")
    print("[2] ref")
    print("[3] rref")
    print("[4] Exit program")
    op = util.ask_int("Select operation: ", 1, 4)
    match op:
        case 1:
            select_row()
        case 2:
            pass
        case 3:
            pass
        case 4:
            return
    main()
main()