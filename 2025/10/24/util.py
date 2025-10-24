import csv
import readline
from math import isfinite
from fractions import Fraction
from typing import Callable, TypeVar

RealNumber = TypeVar("RealNumber", float, Fraction)
NUMBER_PARSER: Callable[[str], RealNumber] = Fraction

def matrix_from_csv(file_name: str) -> list[list[RealNumber]]:
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        return [[NUMBER_PARSER(num) for num in line] for line in reader]

def ask_int(prompt: str, minimum: int | float, maximum: int | float, default: str = "", validators=[]) -> int:
    def hook():
        readline.insert_text(default.strip())
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    while True:
        try:
            value = int(input(prompt).strip())
            if value < minimum or value > maximum:
                raise ValueError(f"{value} is not within range [{minimum}, {maximum}]")
            for validator in validators:
                validator(value)
            return value
        except ValueError as e:
            print(e)
        finally:
            readline.set_pre_input_hook(None)

def ask_row(prompt: str, num_cols: int, default: str = "", validators=[]) -> list[RealNumber]:
    def hook():
        readline.insert_text(default.strip())
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    while True:
        try:
            row_str = input(prompt).strip()
            row = [NUMBER_PARSER(n) for n in row_str.split(" ")]
            if len(row) != num_cols:
                raise ValueError(f"Length of input {len(row)} does not match number of columns {num_cols}")
            for validator in validators:
                validator(value)
            return row
        except ValueError as e:
            print(e)
        finally:
            readline.set_pre_input_hook(None)
            
def ask_bool(prompt: str, default: bool) -> bool:
    bool_str = input(prompt).lower()
    if bool_str in ["t", "true", "y", "yes"]:
        return True
    elif bool_str in ["f", "false", "n", "no"]:
        return False
    return 

def nonzero_finite_value(value: RealNumber):
    if value == 0 or not isfinite(value):
        raise ValueError(f"{value} is not nonzero and finite")

def rowSwap(M: list[list[RealNumber]], row_index: int, row_swap_index: int):
    k = M[row_index]
    M[row_index] = M[row_swap_index]
    M[row_swap_index] = k

def rowAdd(M: list[list[RealNumber]], row_index: int, row_add_index: int):
    for i in range(len(M[row_index])):
        M[row_index][i] += M[row_add_index][i]
        
def rowMultiply(M: list[list[RealNumber]], row_index: int, scalar: RealNumber):
    nonzero_finite_value(scalar)
    for i in range(len(M[row_index])):
        M[row_index][i] *= scalar

def rowAddMultiple(M: list[list[RealNumber]], row_index: int, row_add_index: int, scalar: RealNumber):
    nonzero_finite_value(scalar)
    for i in range(len(M[row_index])):
        M[row_index][i] += scalar * M[row_add_index][i]
        
# This function exists purely for avoiding floating point rounding errors
def rowDivide(M: list[list[RealNumber]], row_index: int, scalar: RealNumber):
    nonzero_finite_value(scalar)
    for i in range(len(M[row_index])):
        M[row_index][i] /= scalar
        
def gauss_jordan_elimination(M: list[list[RealNumber]], reduced: bool = True):
    x = 0
    y = 0
    num_rows = len(M)
    num_cols = len(M[0])
    while x < num_rows and y < num_cols:
        if M[x][y] == 0:
            for i in range(x+1, num_rows):
                if M[i][y] != 0:
                    rowSwap(M, x, i)
                    break
        if M[x][y] == 0:
            y += 1
            continue
        rowDivide(M, x, M[x][y])
        for i in range(0 if reduced else x+1, num_rows):
            if i == x:
                continue
            if M[i][y] != 0:
                rowAddMultiple(M, i, x, -M[i][y])
        x += 1
        y += 1
        
try:
    from tabulate import tabulate
except:
    pass
def print_matrix(M: list[list[RealNumber]]):
    print(tabulate([[format(frac) for frac in row] for row in M]))