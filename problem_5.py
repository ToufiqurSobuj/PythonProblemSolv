#Q1: Prime number:

# num = int(input("enter the number: "))
# if num == 1:
#     print("It is not a prime number.")
# for x in range(2, num):
#     if num % x == 0:
#         print(num, "It is not a prime number.")
#         break
# else:
#     print(num, "It is a prime number.")



#Q2: Random number:

import random
num = random.randint(0, 10)
print(num)

#Q2: print all prime number in an interval:

lower = int(input("enter lower number: "))
upper = int(input("enter upper number: "))
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # print(num, "It is not a prime number")
                break
        else:
            print(num, "It is a prime number")