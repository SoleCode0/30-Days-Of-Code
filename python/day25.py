# Task
'''
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(root(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code.
'''

# Sample Input
'''
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

3
12
5
7
'''

# Sample Output
'''
For each test case, print whether n is Prime or Not prime on a new line.

Not prime
Prime
Prime
'''

# Explanation
'''
Test Case 0: n=12.
12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 4, 6), so we print Not prime on a new line.

Test Case 1: n=5.
5 is only divisible 1 and itself, so we print Prime on a new line.

Test Case 2: n=7.
7 is only divisible 1 and itself, so we print Prime on a new line.
'''

# Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import count, islice

n = int(input())
for i in range(n):
    x, prime = int(input()), True
    sq = int(x**0.5)-1
    if x<2: prime = False
    else:
        for num in islice(count(2), sq):
            if not x%num:
                prime = False
    if prime: print("Prime")
    else: print("Not prime")