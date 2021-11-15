# ask
'''
Given a 6x6 2D Array, A:
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
'''

# hourglass
'''
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
'''

# Sample Input
'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''

# Sample Output
'''
19
'''

# Explainatin(hourglass)
'''
A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
'''

# The hourglass with the maximum sum (19) is:
'''
2 4 4
  2
1 2 4
'''

# Code
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    max = -99
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(6):
        for j in range(6):
            if ((i + 2 < 6) and (j + 2 < 6)):
                temp = arr[i][j] + arr[i + 2][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i][
                    j + 2] + arr[i + 2][j + 2]
                if (temp > max):
                    max = temp

    print(max)