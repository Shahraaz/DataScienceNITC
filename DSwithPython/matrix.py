A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [3, 4], [5, 6]]

# Shape of matrix
def Shape(A):
    n_row = len(A)
    n_col = len(A[0])
    return n_row, n_col


print(Shape(A))
print(Shape(B))

def get_Row(A,i):
    return A[i]

def get_Col(A,i):
    return [A[j][i] for j in range(0,len(A))]

print(get_Row(A,0))

print(get_Col(A,0))