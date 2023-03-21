import numpy as np

matrix = np.random.random([5,6])
 
vec_hs = []
rank = 0
check = True
i,j = 0,0
row,col = matrix.shape
t = min(row,col)
while i < t and j < t:
    check = False
    for i in range(rank,row):
        if matrix[i,j]!=0:
            check = True
            vec_hs.append(i)
            break
    if check:
        temp = matrix[i]
        matrix[i] = matrix[rank]
        matrix[rank] = temp
        
        matrix[rank] /= matrix[rank][j]
        
        for k in range(rank+1,row):  #for(int i = rang+1;i<row;i++)
            matrix[k]-= matrix[rank] * matrix[k][j]
        rank+=1
    i+=1 
    j+=1

i=0
print(vec_hs)
for k in vec_hs:
    for j in range(0,i):
        matrix[j]-= matrix[i] * matrix[j][k]
    i+=1
print(matrix)
        
    
        