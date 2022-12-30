# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan 
# Section: 574
# Assignment: 6-4
# Date: 1 10 22
#
from math import *

num = int(input("Enter a positive integer: \n"))#gets the starting number
print(f"The Juggler sequence starting at {num} is:")
num2 = [num]# begins the list with said input
c = 0#initializes our count at 0
while num != 1:#program runs until we get num to equal 1 
    c +=1
    if num %2 == 0:#checks if its an even number
        num = sqrt(num)
        num = floor(num)
    else:
        num = sqrt(pow(num,3))
        num = floor(num)
    num2.append(num)# adds num to the list
res = str(num2)[1:-1]#removes the brackets from the list

print(res)
print(f"It took {c} iterations to reach 1")

