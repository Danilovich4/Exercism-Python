def steps(number):
    
    contador = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:   
        while number > 1:
            #Par
            if number % 2 == 0:
                number = number // 2
            #Impar
            else:
                number = 3*number+1
            contador += 1

    return contador
    
            
