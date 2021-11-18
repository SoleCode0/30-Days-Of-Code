# Task
'''
Complete the Difference class by writing the following:
    1. A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
    2. A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable.
'''

# Sample Input
'''
STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]
'''

# Sample Output
'''
4
'''

# Code
class Difference:
    def __init__(self, a):
        self.__elements = a
    # Your Code Below
    def computeDifference(self):
        sorted_el = sorted(self.__elements)
        self.maxDifference = abs(sorted_el[-1] - sorted_el[0])
	# Your Code Above

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maxDifference)