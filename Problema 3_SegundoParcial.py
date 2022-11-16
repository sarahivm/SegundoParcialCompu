x = '-'

M = [[x,1,2,x,x,x,x,x],\
    [x,x,1,5,2,x,x,x],\
    [x,x,x,2,1,4,x,x],\
    [x,x,x,x,3,6,8,x],\
    [x,x,x,x,x,3,7,x],\
    [x,x,x,x,x,x,5,2],\
    [x,x,x,x,x,x,x,6],\
    [x,x,x,x,x,x,x,x]
   ]

letters='12345678'

m = '*'+letters+'\n'
for i in range(len(M)):
    m += letters[i]
    for j in range(len(M)):
        if i != j:
            m += str(M[i][j])
        else:
            m += "*"
    m += '\n'
print("Matriz de conexiones: ")
print(m)

mino = [[0,0,0]]*len(M)
dist = [0]*len(M)
for j in range(1,len(M)):
    posi = []
    for i in range(0,len(M)):
        if M[i][j] != x:
            dis = dist[i] + M[i][j]
            posi.append([dis,letters[i],letters[j]])
   
    mino[j] = min(posi)
    dist[j] = mino[j][0]

lin = mino[-1]
s = '8'
lt = '8'
while lt != '1':
    u = lin[1]
    for v in mino:
        if v[2] == u:
            s = v[2]+'-'+s
            lin = v
    lt = lin[1]
s = '1-'+s

print("Nodes of the shortest route ",s)
print("Distance: ", mino[-1][0]) 
        
    

        
    



