from tabulate import tabulate
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")

num_rows = int(input("Number of Rows: "))
num_cols = int(input("Number of Columns: "))

matrix = [[0] * num_cols ] * num_rows

def input_matrix(i):
    while True:
        row_str = input(f"Input row {i} (separated by space): ")
        matrix[i] = [float(n) for n in row_str.split(" ") if n.isdecimal()]
        if len(matrix[i]) == num_cols:
            break
        print(f"Length of input does not match number of columns {num_cols}")
for i in range(num_rows):
  input_matrix(i)

while True:
    print(tabulate(matrix))
    print("[1]: Select row")
    print("[2]: Exit")
    op = int(input())
    if op == 1:
      while True:
        row_i = int(input("Input row index to select: "))
        if row_i < 0 or row_i >= num_rows:
          continue
        print("[1]: Enter new values")
        print()
        match op:
          case 1:
            
    if op == 2:
      break