# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:22:25 2016

@author: Bhuti
"""

# FizzBuzz - Prints integers form 1 to 100, except for multiples of 3 print
# 'fizz', for multiples of 5 print 'buzz', and multiples of boht print
# 'FizzBuzz'

# def is_multiple_of_3(n):
#    result = n % 3 # % is a modulus operator - return the remainder
#    if result == 0:
#        return True
#    else:
#        return False

def is_multiple(factor, n):
    result = n % factor
    return (result == 0)

#another version
# def multiple_checker(factor):
#    def is_multiple(n):
#        res = n % factor
#        return res
#    return is_multiple

# range goes from 1 to n-1 
integers = range(1,101)
for i in integers:
     if is_multiple(3,i) and is_multiple(5,i):
         print('FizzBuzz')
     elif is_multiple(3,i):
         print('Fizz')
     elif is_multiple(5,i):
         print('Buzz')        
     else:
        print(i)