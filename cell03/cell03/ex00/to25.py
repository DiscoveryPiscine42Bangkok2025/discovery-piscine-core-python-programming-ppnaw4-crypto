A = int(input("Enter a number less than 25 :"))
if A > 25:
    print("Error")
else:
    while A <= 25:
        print("Inside the loop, my variable is " , A)
        A+=1