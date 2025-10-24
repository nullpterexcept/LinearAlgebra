from util import matrix_from_csv

def is_ref(M):
    rows = len(M)
    cols = len(M[0])
    for i in range(cols):
        for j in range(i+1, rows):
            if M[j][i] != 0:
                return False
    return True

M = matrix_from_csv("matrix.txt")
print(is_ref(M))