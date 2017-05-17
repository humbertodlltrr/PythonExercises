"""
Author: Humberto Della Torre
My solutions for several Python exercises using recursion.
Exercises obtained from http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

1. Write a Python program to calculate the sum of a list of numbers.

2. Write a Python program to converting an Integer to a string in any base.

3. Write a Python program of recursion list sum.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21

4. Write a Python program to get the factorial of a non-negative integer.

5. Write a Python program to solve the Fibonacci sequence using recursion. 

6. Write a Python program to get the sum of a non-negative integer. 
Test Data: 
sumDigits(345) -> 12
sumDigits(45) -> 9 

7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). 
Test Data: 
sum_series(6) -> 12
sum_series(10) -> 30 

8. Write a Python program to calculate the harmonic sum of n-1. 
Note: The harmonic sum is the sum of reciprocals of the positive integers. 
Example : 
harmonic series

9. Write a Python program to calculate the geometric sum of n-1. 
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms. 
Example : 
harmonic series

10. Write a Python program to calculate the value of 'a' to the power 'b'.
Test Data : 
(power(3,4) -> 81 

11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
"""

#1. Write a Python program to calculate the sum of a list of numbers.
def sum_list(nums):
    if len(nums) >= 2:
        return nums[0] + sum_list(nums[1:])
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0
      
#2. Write a Python program to converting an Integer to a string in any base.
#initial attempt improved with example, base 2-36
def i2s(integer,base):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if integer < base:
        return convert_string[integer]
    else:
        a = integer
        b = 1
        c = 0
        while a >= base:
            a = a//base
            b = b * base
            c += 1
        d = integer-a*b
        e = 0
        while d >= base:
            d = d//base
            e += 1
        return convert_string[a] + "0"*(c-e-1) + i2s(integer-a*b,base)

#based on example
def i2s2(integer,base):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if integer < base:
        return convert_string[integer]
    else:
        return i2s2(integer//base,base) + convert_string[integer%base]

#3. Write a Python program of recursion list sum.
#Test Data: [1, 2, [3,4], [5,6]]
#Expected Result: 21
def rec_list_sum(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        if type(nums[0])==int:
            return nums[0]
        else:
            return rec_list_sum(nums[0])
    else:
        if type(nums[0])==int:
            return nums[0] + rec_list_sum(nums[1:])
        else:
            return rec_list_sum(nums[0]) + rec_list_sum(nums[1:])

#4. Write a Python program to get the factorial of a non-negative integer.
def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)
