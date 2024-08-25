def secret_code(num_inf, num_sup):

    interval = []
    secure = 0

    for i in range(num_inf, num_sup+1, 1):
        interval.append(i)

    for j in interval:

        if j%3 == 0:
            secure += j
        
        if j%5 == 0: 
            secure -= j
    
    return secure

num_inf = int(input('Limite inferior do intervalo:'))
num_sup = int(input('Limite superior do intervalo:'))

print(f'O valor total calculado é: {secret_code(num_inf, num_sup)}')


