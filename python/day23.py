# Task
'''
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

HINT: You'll find a queue helpful in completing this challenge.

Function Description

>>  Complete the levelOrder function in the editor below.

>>  levelOrder has the following parameter:
    - Node pointer root: a reference to the root of the tree
'''

# Sample Input
'''
The locked stub code in your editor reads the following inputs and assembles them into a BST:
The first line contains an integer, T(the number of test cases).
The T subsequent lines each contain an integer, data, denoting the value of an element that must be added to the BST.

6
3
5
4
7
2
1
'''

# Sample Output
'''
Print the data value of each node in the tree's level-order traversal as a single line of N space-separated integers.

3 2 5 1 4 7 
'''

# Code
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    
    # Your Code Below
    from collections import deque
    def levelOrder(self,root):
        
        queue = self.deque([root]) if root else self.deque()
        while queue:
            node = queue.popleft()
            print(node.data, end=' ')

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    #Your Code Above
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
