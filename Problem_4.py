#Q1: is a number is odd or even

num = float(input("enter your number:: "))

if num % 2 == 0:
    print("It is an event number")
else:
    print("It is an odd number")

#Q2: check leap year:

year = int(input("enter the year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Q3: find the largest among three number:

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is largest number")
elif (num2 > num1) and (num2 > num3):
    print(num2, "is largest number")
else:
    print(num3, "is largest number")