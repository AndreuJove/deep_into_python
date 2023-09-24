def solution(matrix):
    
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_zeros = [(columns*[0]) for i in range(rows)]
    
    for j, array in enumerate(matrix): # rows 
        for i, value in enumerate(array): # columns
            
            if value:
                print("---")
                print("---")
                print("---")
                print(j,i)
                print("---")
                for num_one in range(i-1, i+2):
                    
                    
                    
                    for num_two in range(j-1, j+2):
                        print([num_two, num_one])

                        if num_two == 1 and num_one == 3:
                            breakpoint()
                        
                        if num_one < 0:
                            continue
                        
                        if num_two < 0:
                            continue
                        
                        if j == num_one and i == num_two:
                            continue
                           
                        try:
                            matrix_zeros[num_two][num_one] = matrix_zeros[num_two][num_one] + 1
                            print(f"Suming: {[num_two, num_one]}")
                            

                            # print(num_two, num_one)
                            
                            # print(matrix_zeros)
                            
                        except:
                            pass
                
                
                
                
                
                
                
    return matrix_zeros



print(solution([[True,False,False,True], 
 [False,False,True,False], 
 [True,True,False,True]]))
