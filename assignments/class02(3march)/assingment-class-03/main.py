# 1.
# Introduction to Control Flow
# Control flow refers to the order in which statements are executed in a program.
#  In Python, decision-making is achieved using if, elif,
#  and else statements, along with comparison and logical operators.

#2.
#comparsion opreators
#Comparison operators are used to compare values and return True or False. 
# Here are the most common ones:

#== (equal to)
#!=  (not equal to)
#>   (greater than)
#<   (less than)
#>= (greater than or equal to)
#<= (less than or equal to)

# code exampel
x :int =30
y : int =20

print(x==y)
print (x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#-3
#logical operator
#Logical operators combine multiple conditions:

#and (True if both conditions are True)
#or (True if at least one condition is True)
#not (reverses the result of a condition)

age:int= 25
is_student:bool=True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")

#    4. The if Statement
"""" postive")
elif:The if statement is used to execute a block of code only if a condition is True."""""
num:int =10
if num> 0:
print("number is
