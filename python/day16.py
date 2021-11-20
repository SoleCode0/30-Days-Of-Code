# Task
'''
Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a 0 score.
'''

# Sample Input
'''
Input 1>> 3
Input 2>> za
'''

# Sample Output
'''
Output 1>> 3
Output 2>> Bad String
'''

# Explaination
'''
Sample Case 0 contains an integer, so it should not raise an exception when we attempt to convert it to an integer. Thus, we print the 3.
Sample Case 1 does not contain any integers, so an attempt to convert it to an integer will raise an exception. Thus, our exception handler prints Bad String.
'''

# Code
#!/bin/python3
import sys

S = input().strip()
# Your Code Below
try: 
    print (int(S))
except ValueError: 
    print ("Bad String")
# Your Code Above