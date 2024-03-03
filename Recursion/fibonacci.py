def fibonacci(n,fib=[0,1]):

    if n<=len(fib):
        return fib[:n]
    
    fib.append(fib[-1]+fib[-2])

    return fibonacci(n,fib)


print(fibonacci(3))