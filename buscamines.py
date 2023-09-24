
def solution(matrix):
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    matrix_zeros = [(columns*[0]) for i in range(rows)]
    
    for col in range(columns-1):
        for row in range(rows-1):

            
            if matrix[col][row]:
                
                
                for z in range(col-1, row+2):
                    if z < 0:
                        continue
                    for y in range(col-1, row+2):
                        
                        if y < 0:
                            continue
                        if col == z and row == y:
                            continue
                            
                        matrix_zeros[z][y] = matrix_zeros[z][y] + 1
    return matrix_zeros

paco = solution([[False, False, False],
                [False, True, False]])



# paco = solution([[True, False, False],
#           [False, True, False],
#           [False, False, False]])

print(paco)
