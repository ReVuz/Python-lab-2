# -*- coding: utf-8 -*-
"""python lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qUs9ONUtdY977TwbxNqPlIZtDtmOBls7

# 1. Program to print the average of three numbers
"""

a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
avg=(a+b+c)/3
print("Average of the numbers = ",avg)

"""# 2. Program to print sum and average of three numbers"""

a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
avg=(a+b+c)/3
sum=a+b+c
print("Sum of the numbers = ",sum)
print("Average of the numbers = ",avg)

"""# 3. Program to convert time entered in seconds to hrs mins and secs"""

t=int(input("enter time(in secs) "))
h=t/3600
s=t%3600
m=s/60
print(h," hours",m," minutes ",s," seconds")

"""# 4. Program to print area and perimeter of a triangle"""

a=int(input("Enter side a "))
b=int(input("Enter side b "))
c=int(input("Enter side c "))
s=(a+b+c)/2
area= pow(s*(s-a)*(s-b)*(s-c),0.5)
print("Area of triangle =",area)
print("Perimeter of triangle =",s*2)

"""# 5. Program to print area of circle"""

r=int(input("Enter radius of circle "))
area=3.14*r*r
print("Area of circle =",area)

"""## 6. Program to read two unequal number and interchange them without using a third variable"""

a=int(input("Enter a number "))
b=int(input("Enter another number "))
print("Before swapping : \na= ",a,"b= ",b)
a=a+b
b=a-b
a=a-b
print("After swapping : \na= ",a,"b= ",b)

"""## 7. Program to print sum,difference,product,quotient and remainder of two unequal numbers"""

a=int(input("Enter a number "))
b=int(input("Enter another number "))
print("sum= ",a+b,"\ndifference= ",a-b,"\nproduct= ",a*b,"\nquotient= ",a/b,"\nremainder= ",a%b)

"""# 8. Program to input number of days and display into years,months and days"""

d=int(input("Enter number of days "))
print("years= ",d/365,"\nmonths= ",(d%365)/12,"\ndays= ",((d%365)%12)/30)