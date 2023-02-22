def multiplica_matriz(a, b):
   
    if len(a[0]) != len(b):
        return None
    
    resultado = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    
    for i in range(len(a)):
        
        for j in range(len(b[0])):

            for k in range(len(a[0])):
                
                resultado[i][j] += a[i][k] * b[k][j]
    
    return resultado