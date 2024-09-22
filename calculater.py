def add(a , b):
    c = a+b
    return print("\nThe Addition of the numbers are. ", c, "\n")

def mul(a , b):
    c = a*b
    return print("\nThe Multication of the numbers are. ", c, "\n")

def sub(a , b):
    c = a-b
    return print("\nThe subtraction of the numbers are. ", c, "\n")

def div(a , b):
    c = a/b
    return print("\nThe Division of the numbers are. ", c, "\n")

def mean(a , b):
    c = (a+b)/2    
    return print("\nThe Mean value of the numbers are. ", c, "\n") 

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
c : float
option = int(input("\nFor multiplication press 1\nFor addition press 2\nFor subtraction press 3\nFor division press 4\nFor mean press 5 \n\n"))

if option == 1:
    mul(a , b)
elif option == 2:
    add(a, b)
elif option == 3:
    sub(a , b)
elif option == 4:
    div(a , b)
elif option == 5:
    mean(a , b) 
else:
    print("\nInvalid Option\n")
