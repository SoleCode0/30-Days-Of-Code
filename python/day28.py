# Task
'''
Consider a database table, Emails, which has the attributes First Name and Email ID. Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.
'''

# Sample Input
'''
The first line contains an integer, N, total number of rows in the table.
Each of the N subsequent lines contains 2 space-separated strings denoting a person's first name and email ID, respectively.

6

riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
'''

# Sample Output
'''
Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

julia
julia
riya
samantha
tanya
'''

# Code

#!/bin/python3
import re

N = int(input())

pattern = r"@gmail\.com$"
regex = re.compile(pattern)
firstNames = []
    
for N_itr in range(N):
    first_multiple_input = input().split()
    firstName = first_multiple_input[0]
    emailID = first_multiple_input[1]
        
    if regex.search(emailID):
        firstNames.append(firstName)
    
firstNames.sort()

for name in firstNames:
    print(name)