num = int (input("Enter the number:"))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    elif (num > 20 and num <= 30):
        print("Number is between 21-30")
    elif (num > 30 and num <= 40):
        print("Number is between 31-40")
    elif (num > 40 and num <= 50):
        print("Number is between 41-50")
    elif (num > 50 and num <= 60):
        print("Number is between 51-60")
    elif (num > 60 and num <= 70):
        print("Number is between 61-70")
    elif (num > 70 and num <= 80):
        print("Number is between 71-80")
    elif (num > 80 and num <= 90):
        print("Number is between 81-90")
    elif (num > 90 and num <= 100):
        print("Number is between 91-100")
    else:
        print("Number is greater than 100")
else:
    print("Number is zero")