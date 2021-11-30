# Task
'''
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

>>> If the book is returned on or before the expected return date, no fine will be charged (i.e. fine=0) .
>>> If the book is returned after the expected return day but still within the same calendar month and year as the
    expected return date, fine= 15 Hackos x number of days late.
>>> If the book is returned after the expected return month but still within the same calendar year as the expected
    return date, the fine= 500Hackos x number of days late.
>>> If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos
'''

# Sample Input
'''
STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)
'''

# Sample Output
'''
45
'''

# Explanation
'''
Given the following return dates:
Returned: D1=9, M1=6, Y1=2015
Due: D2=6, M2=6, Y2=2015

Because Y2==Y1, it is less than a year late.
Because M2==M1, it is less than a month late.
Because D2<D1, it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be 15 Hackos x (# Days Late). We then print the result of 15 * (D1 - D2) = 15*(9-6) = 45 as our output.
'''

# Code
# Enter your code here. Read input from STDIN.
# Print output to STDOUT
return_date = list(map(int,input().split(' ')))
expected_date = list(map(int,input().split(' ')))

fine = 0

if return_date[2] > expected_date[2]:
    fine = 10000
    
elif return_date[2] == expected_date[2]:

    if return_date[1] > expected_date[1]:
        fine = (return_date[1] - expected_date[1])*500
    
    elif return_date[1] == expected_date[1]:
        if return_date[0] > expected_date[0]:
            fine = (return_date[0] - expected_date[0])*15
    
print(fine)