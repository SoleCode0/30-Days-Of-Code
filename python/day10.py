# Task
'''
Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
'''

# Sample Input/Output
'''
input_1>>  5
output_1>> 1

input_2>>  13
output_2>> 2
'''

# Code
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    numbers = str(bin(n)[2:]).split('0')
    lenghts = [len(num) for num in numbers]
    print(max(lenghts))