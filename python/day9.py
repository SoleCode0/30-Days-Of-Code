# Task
'''
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.
'''

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    for i in range (1, n):
        n= n*i
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    # call for factorial function
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()