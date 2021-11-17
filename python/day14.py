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

    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)