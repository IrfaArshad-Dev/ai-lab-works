#task 1
import numpy as np 
marks=np.array([
    [51,72,23],
    [24,45,76],
    [22,56,43]
    ])
print("marks of student 1 are:",marks[0])
print("marks of student 2 are:",marks[1])
print("marks of student 3 are:",marks[2])
print("------------------------------------")

#task 2 by using array of task 1
print("DIMENSION OF marks",marks.ndim)
print("------------------------------------")

#task 3
num=np.arange(1,20)
print(num)
print("------------------------------------")

#task 4
import numpy as np
a1 = np.array([99, 93, 86])
a2 = np.array([90, 87, 78])
add = a1 + a2
sub = a1 - a2
mul = a1 * a2
print("SUM OF ARRAYS:", add)
print("substraction OF ARRAYS:", sub)
print("Multiplication OF ARRAYS:", mul)
print("------------------------------------")

#task 5
markss=np.array([43,44,65,78,75,99])
print("The sum of the marks is :",np.sum(markss))
avg=sum(markss)/6
print("The Average of the marks is :",avg)
print("Mximum num is:",np.max(markss))
print("Minimum num is:",np.min(markss))
print("------------------------------------")

#task 6
def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check(4))   # Output: Even
print(check(7))   # Output: Odd
print("------------------------------------")

#task 7
student_marks = [99, 93, 86, 90, 87, 78]
def getmarks(marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)
    
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)
getmarks(student_marks)
print("------------------------------------")

#task 8
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
celsius_to_fahrenheit(25)
print("------------------------------------")
