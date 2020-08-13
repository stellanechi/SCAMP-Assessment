def fibbionacci_sequence (n):
    if n <1 :
        return ("invalid entry")
    #retuen 0 if n is greather than l
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else :
        return fibbionacci_sequence(n-1) + fibbionacci_sequence(n-2)
    
print (fibbionacci_sequence(9))
