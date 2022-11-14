#Q1: convert kilometers to miles

km = float(input("enter the kilometers value: "))
miles = km * (0.621371)
print(km, "km will be", miles, "miles")

#Q1: number positive negitive or zero:

num = float(input("enter your number: "))
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negitive")
else:
    print("the number is Zero")