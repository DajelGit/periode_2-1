def fib(i):
    n1, n2 = 1, 1
    listje = [1, 1]
    while i > 0:
        n1, n2 = n2, n1 + n2
        listje.append(n2)
        i -= 1

    return listje
    
print(fib(20))

