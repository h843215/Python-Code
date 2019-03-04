def transpose(matrix):
    result = []
    n = []
    for i in range(len(matrix[0])):
        for k in range(len(matrix)):
            n.append(matrix[k][i])
        result.append(n)
        n = []
    return result

matrix1 = [[0, 1, 2, 3, 4],[0, 1, 2, 3, 4] ]
print("Transposed:", transpose (matrix1 ))


        
    
