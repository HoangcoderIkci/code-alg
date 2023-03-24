import numpy as np

#matrix = np.random.random([2,6])
matrix = np.array([[0,0,0,1,0,0,1],
                   [0,0,0,1,0,1,2]])
 
vec_hs = []
rank = 0
check = True
i,j = 0,0
row,col = matrix.shape
t = min(row,col) 
while rank < t and j < col:
    check = False
    for i in range(rank,row):
        if matrix[i,j]!=0:
            check = True
            vec_hs.append(j)
            break
    if check:
        matrix[[i,rank]] = matrix[[rank,i]]
        
        matrix[rank] = matrix[rank] / matrix[rank][j]
        
        for k in range(rank+1,row):  #for(int i = rang+1;i<row;i++)
            matrix[k]-= matrix[rank] * matrix[k][j]
        rank+=1
    j+=1

i=0
print(vec_hs)
for k in vec_hs:
    for j in range(0,i):
        matrix[j]-= matrix[i] * matrix[j][k]
    i+=1
print(matrix)
