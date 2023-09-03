
while True:

    a=float(input("enter value for a :"))
    b=float(input("enter value for b :"))

    print("choose 1 for +")
    print("choose 2 for -")
    print("choose 3 for *")
    print("choose 4 for /")

    ch = int(input("Enter choice:"))
    match ch:
        case 1:
            ans=a+b
            print("the sum of a and b is :",ans)
        case 2:
            ans=a-b
            print("the subtraction of a and b is :",ans)
        case 3:
            ans=a*b
            print("the multiplaction of a and b is :",ans)
        case 4:
            ans=a/b
            print("the division of a and b is :",ans)
        case _:
            print("Choose between 1-4")