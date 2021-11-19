# Task
'''
A Node class is provided for you in the editor. A Node object has an integer data field, , data and a Node instance pointer, next, pointing to another node (i.e.: the next node in the list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer, data, that must be added to the end of the list as a new Node object.

Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node
'''

# Sample Input
'''
The first line contains T, the number of elements to insert.
Each of the next T lines contains an integer to insert at the end of the list.

STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1
'''

# Sample Output
'''
Return a reference to the head node of the linked list.

2 3 4 1
'''

# Explaination
'''
Initial: head->NULL

T0: head -> [data=2 | null]

T1: head -> [data=2 | n1] -> [data=3 | null]

T2: head -> [data=2 | n1] -> [data=3 | n2] -> [data=4 | null]

T3: head -> [data=2 | n1] -> [data=3 | n2] -> [data=4 | n3] -> [data=1 | null]
'''

# Code
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    # Your Code Below
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head
    # Your Code Above
    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  