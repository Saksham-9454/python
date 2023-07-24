def fabonacchi(n):
    if (n == 0 ):
        return 0
    elif(n==1):
        return 1
    else:
        return fabonacchi(n-1) + fabonacchi (n-2) 

n = int(input("Enter the number for fabonacchi"))
print (fabonacchi(n))