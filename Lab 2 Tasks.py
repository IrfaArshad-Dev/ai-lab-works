#task 1
sap = input("Enter your SAP ID: ")
name = input("Enter your name: ")
print("hey", name, "your sap is", sap)
print('-------------------------------------------')

#task 2
a = 10
b = 20
print("Before swapping: a =", a, ", b =", b)

temp = a
a = b
b = temp
print("After swapping:  a =", a, ", b =", b)
print('-------------------------------------------')

#task 3
Message = " Programming language"
print("r appears", Message.count("r"), "times")
print("a appears", Message.count("a"), "times")
print("m appears", Message.count("m"), "times")
print("n appears", Message.count("n"), "times")
print("u appears", Message.count("u"), "times")
print('-------------------------------------------')

#task 4
salary = 50000
bonus = 5000
deduction = 2000
final_salary = salary
final_salary += bonus
final_salary -= deduction
print("Original salary :", salary)
print("Bonus           :", bonus)
print("Deduction       :", deduction)
print("Final salary    :", final_salary)

#task 5
rolls = [101, 102, 103, 104, 105]
roll = int(input("Enter roll number: "))
if roll in rolls:
    print("Student is enrolled")
else:
    print("Student is not enrolled")
rolls2 = rolls
print("Same list object?", rolls2 is rolls)
