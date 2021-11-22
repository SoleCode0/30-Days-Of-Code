# Task
'''
Write the following declarations and implementations:

Two instance variables: one for your stack, and one for your queue.
A void pushCharacter(char ch) method that pushes a character onto a stack.
A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
'''

# Sample Input
'''
racecar
'''

# Sample Output
'''
The word, racecar, is a palindrome.
'''

# Explaination
'''
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards.
'''

# Code
import sys

class Solution:
    # Your Code Below
    def __init__(self):
        self.mystack = list()
        self.myqueue = list()
        return(None)

    def pushCharacter(self, char):
        self.mystack.append(char)

    def popCharacter(self):
        return(self.mystack.pop(-1))

    def enqueueCharacter(self, char):
        self.myqueue.append(char)

    def dequeueCharacter(self):
        return(self.myqueue.pop(0))
    # Your Code Above
# Below Code is Pre-written by Hackerrank
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    