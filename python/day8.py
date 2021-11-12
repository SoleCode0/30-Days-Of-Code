# Task
'''
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
'''

# Sample Input
'''
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
'''

# Sample Output
'''
sam=99912222
Not found
harry=12299933
'''

# CODE
n = int(input())
d = {}
for i in range(n):
    x = input().split()
    d[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else : print("Not found")   
    except: break