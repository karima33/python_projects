#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1
'''Write a program that will find all numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included). The numbers obtained should be printed in a list.'''
# Solution 
numbers = [] 
for nbr in range (2000, 3200):
     if (nbr % 7 == 0) and (nbr % 5 != 0):
        numbers.append(str(nbr))

print(','.join(numbers))


# In[2]:


# Question 2 
'''Write a program that can compute the factorial of a given number. 
 (The factorial of n is the product of all positive integers less than or equal to n.)
 For example: For factorial(5)= 5 x 4 x 3 x 2 x 1 the result is 120 (i.e. factorial (0)=1).'''

# Solution 
#The factorial of a given number
def factorial(number):
      
    if number == 0:
        return 1
     
    return number* factorial(number-1)
  #test
nbr = 5;
print("The factorial of", nbr, "is",
factorial(nbr))


# In[3]:


# Question 3 

'''With a given integer number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
Then, the program should print the dictionary. Suppose the following input is supplied to the program:
8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}  '''

# Solution 

number = int(input("Type a number please : "))

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)


# In[4]:


# Question 4 

'''Given a non-empty string and an integral n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0.
.len(str)-1 inclusive)'''

# Solution 

def missing_char(str, n):
    return str.replace(str[n], "",1)
#test
missing_char('kitten', 0)


# In[5]:


# Question 5 

'''Write a NumPy program to convert a NumPy array into a Python list structure.'''

# Solution 
#NumPy program to convert a NumPy array into a Python list structure.
import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
print(x.tolist())


# In[6]:


# Question 6

'''Write a NumPy program to compute the covariance matrix of two given arrays. '''

# Solution 
#NumPy program to compute the covariance matrix of two given arrays. 
import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("\nOriginal array1:")
print(x)
print("\nOriginal array2:")
print(y)
print("\nCovariance matrix of the said arrays:\n",np.cov(x, y))


# In[7]:


# Question 7

''' Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2 * C * D)/H] 

The following are the fixed values of C and H: C is 50. H is 30. 

D is the variable whose values should be input into your program in a comma-separated sequence. 
(That means D contains more than value) '''

# Solution 

import math

numbers = input("Type the value of D please : ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# In[ ]:




