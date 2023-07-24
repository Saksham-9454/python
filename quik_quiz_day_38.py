a = (input("Enter a number between 5 to 9"))
match a:
    case 1:
        if (int(a)<5 or int(a)>9):
            raise ValueError ("Value should be between 5 to 9")
        print("the value of a is",a)
    case quit :
# if (int(a)<5 or int(a)>9):
#     raise ValueError ("Value should be between 5 to 9")
        if (a == "quit"):
            print("This is quit case")