#Q1: Python program to display the multiplication table:

num = int(input("enter your multiplication number: "))
for x in range(1, 11):
    mul = num * x
    print(num, "x", x, "=", mul)


#Q2: Python program to print the fibonacci serise:
#formula = 0+1=1, 1+2=3, 2+3=5, 3+5=8

a = 0
b = 1
num = int(input("enter a number to fibonacci serise: "))
if num == 1:
    print(b)
else:
    print(a)
    print(b)
    for i in range(1, num+1):
        c = a+b
        a = b
        b = c
        print(c)


#Q2: Python program to check ARMSSTRONG number:
#ex: 142 = (1x1x1) + (4x4x4) + (2x2x2) = ?
#Ex: 56 = (5x5) + (6x6) = ?

num = int(input("Enter your 3 digit number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = cube + sum
    temp = temp // 10  #fd=flor division

if sum == num:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
