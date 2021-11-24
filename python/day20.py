# Task
'''
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:
    
    1. Array is sorted in numSwaps swaps.
    where numSwaps is the number of swaps that took place.
    
    2. First Element: firstElement
    where firstElement is the first element in the sorted array.
    
    3. Last Element: lastElement
    wherelastElement  is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.
'''

# Example
'''
a = [4, 3, 1, 2]

original a: 4 3 1 2
round 1  a: 3 1 2 4 swaps this round: 3
round 2  a: 1 2 3 4 swaps this round: 2
round 3  a: 1 2 3 4 swaps this round: 0

In the first round, the 4 is swapped at each of the 3 comparisons, ending in the last position. In the second round, the 3 is swapped at 2 of the 3 comparisons. Finally, in the third round, no swaps are made so the iterations stop. The output is the following:

Array is sorted in 5 swaps.
First Element: 1
Last Element: 4
'''

# Sample Input
'''
3
3 2 1
'''

# Sample Output
'''
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
'''

# Explaination
'''
The array a = [3,2,1] is not sorted, so we perform the following 3 swaps. Each line shows a after each single element is swapped.

[3,2,1] -> [2,3,1]
[2,3,1] -> [2,1,3]
[2,1,3] -> [1,2,3]

After 3 swaps, the array is sorted.
'''

# Code
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0
for i in range(n):
    currentSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numSwaps += 1
            currentSwaps += 1

    if currentSwaps == 0:
        break

print('Array is sorted in ' + str(numSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))