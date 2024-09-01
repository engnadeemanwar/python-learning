a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c : float
option = int(input("\nFor multiplication press 1\nFor addition press 2\nFor subtraction press 3\nFor division press 4\nFor mean press 5 \n\n"))

if option == 1:
    c = a*b
    print("\nThe Multication of the numbers are. ", c, "\n")
elif option == 2:
    c = a+b
    print("\nThe Addition of the numbers are. ", c, "\n")
elif option == 3:
    c = a-b
    print("\nThe subtraction of the numbers are. ", c, "\n")
elif option == 4:
    c = a/b
    print("\nThe Division of the numbers are. ", c, "\n")
elif option == 5: 
    c = (a+b)/2    
    print("\nThe Mean value of the numbers are. ", c, "\n")
else:
    print("\nInvalid Option\n")
