# table = int(input("Enter table: "))

# for i in range(1, 11):
#     a = table * i
#     print(f"{table} X {i} = {a}")


marks = float(input("Enter marks percentage: "))

if (90 <= marks <= 100):
    print("\n A+ \n")
elif (80 <= marks < 90):
    print("\n B+ \n")
elif (70 <= marks < 80):
    print("\n C+ \n")
elif (60 <= marks < 70):
    print("\n D+ \n")
elif (50 <= marks < 60):
    print("\n D \n")
elif (50 > marks > -1):
    print("\n FAIL e Twada munda \n")
else:
    print("\n Invalid Percentage \n")
