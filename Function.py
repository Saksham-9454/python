def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if(a>b):
        print("First Number is greater")
    else:
        print("Second Number is greater")

def issmaller(a,b):
    pass

a= int(input("Enter the number:"))
b= int(input("Enter the second number:"))
isgreater(a,b)
calculateGmean(a,b)