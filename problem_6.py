#Q1: celsius to fahrenheit:

celsius = int(input("enter temperature in celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print("The convert value is", fahrenheit, "fahrenheit")

#Q2: kelvin to fahrenheit:

k = int(input("enter temperature in k: "))
f = ((k-273.15)*9/5+32)
print("The convert value is", f, "fahrenheit")

#Q3: Factorial

num = int(input("enter a factorial number: "))
fact = 1
if num < 0:
    print("this number not exist factorial number")
if num == 0:
    print("0 number factorial is 1")
if num > 0:
    for i in range(1, num+1):
        fact = fact * i
print("the factorial of the given number is", fact)