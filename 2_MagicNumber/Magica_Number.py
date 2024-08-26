""" 
1. Receber limite inferior e superior do intervalo
2. Criar uma lista com os números inteiros do intervalo
3. Percorrer a lista 
3.1 Se for número primo, continue
3.2 Se for divisível por 4, continue
 """

def prime_number(number):

    candidate = 1
    i = 0

    while number>= candidate:
        
        if number%candidate == 0:
            i += 1
        
        candidate += 1
    
    if i <= 2: 
        return True
    
    else:
        return False
    
def divisible_by_four(number):

    if number%4 == 0:
        return True
    
    else:
        return False

def sum_digits(number):

    somaDigitos = 0
    numberDigits = 1

    while number > numberDigits*10:
        numberDigits *= 10

    while number != 0:
        somaDigitos += number//numberDigits
        number = number%numberDigits
        numberDigits = numberDigits/10
    
    return somaDigitos

def even(candidate_even):

    if candidate_even%2 == 0:
        return False
    else:
        return True

def find_Magic_Number(num_inf, num_sup):

    # As we know, there isn't a number that could be prime and divisible by four, so I'll check just for fun.
    
    for i in range(num_inf, num_sup+1, 1):

        isPrime = prime_number(i)
        isDivisibleBy4 = divisible_by_four(i)
        isSumEvenDigits = even(sum_digits(i))

        print(f'Number: {i}')
        print('Prime:', isPrime)
        print('Divisible by 4:', isDivisibleBy4)
        print('Sum of digits:', isSumEvenDigits,'\n')

        if isPrime and isDivisibleBy4 and isSumEvenDigits:
            return print(f'O número {i} é o Magic Number')  

    return print('Magic Number was not find')
 
num_inf = int(input('Limite inferior do intervalo:'))
num_sup = int(input('Limite superior do intervalo:'))

find_Magic_Number(num_inf, num_sup)
