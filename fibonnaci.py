def fibonacci(n):
    # Complete this function
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  

n = int(input())
# call the fibonacci function
result=fibonacci(n)
print(result)
