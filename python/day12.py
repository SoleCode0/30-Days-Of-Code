# Task
'''
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, firstName.
A string, lastName.
An integer, idNumber.
An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
__________________________
| LETTER |     AVERAGE    |
|    O   |  90 <= a <= 100|
|    E   |  80 <= a <= 90 |
|    A   |  70 <= a <= 80 |
|    P   |  55 <= a <= 70 |
|    D   |  40 <= a <= 55 |
|    T   |        a < 40  |
|________|________________|
'''

# Sample Input
'''
Heraldo Memelli 8135627
2
100 80
'''

# Sample Output
'''
Name: Memelli, Heraldo
ID: 8135627
Grade: O
'''

# Code
# class Person pre-written by Hackerrank
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

# Constructor: your code
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores

    def calculate(self):
        total = 0

        for testScore in self.testScores:
            total += testScore

        avg = total / len(self.testScores)

        if 90 <= avg <= 100:
            return 'O'
        if 80 <= avg < 90:
            return 'E'
        if 70 <= avg < 80:
            return 'A'
        if 55 <= avg < 70:
            return 'P'
        if 40 <= avg < 55:
            return 'D'
        return 'T' 

# Driver Code, pre-written by Hackerrank
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())