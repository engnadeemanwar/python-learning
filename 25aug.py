
a = str(input("Enter person name: "))
b = []
even_numbers = []
odd_numbers = []
for i in range(3):
    c = int(input("Enter your 3No one by one rspectively : "))
    b.append(c)
e = sum(b)
print(f"Hello, {a}! Let's explore your favorite numbers")
first = b[0]
second = b[1]
third = b[2]
for b in b:
    if b % 2 == 0:
        even_numbers.append(b)
    else:
        odd_numbers.append(b)
print(f"These are even numbers {even_numbers}")
print(f"These are odd numbers {odd_numbers}")

print(f"The number {first} and its square: ({first}, {first**2})")
print(f"The number {second} and its square: ({second}, {second**2})")
print(f"The number {third} and its square: ({third}, {third**2})")

print(f"Amazing! The sum of your favorite numbers is: {e}")
def is_prime(e):
    if e <= 1:
        return False
    for i in range(2, int(e ** 0.5) + 1):
        if e % i == 0:
            return False
    return True
if is_prime(e):
    print(f"Wow! {e} is a prime number")
else:
    print(f"Alas {e} is not a prime number")