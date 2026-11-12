# Task 1: Digit Counter 

number = input("Enter an integer: ") 

num_digits = len(number) 

if num_digits == 1:
    print(number,"is a single-digit number")
elif num_digits == 2:
    print(number," is a double-digit number")
elif num_digits == 3:
    print(number," is a triple-digit number")
else:
    print(number," has more than 3 digits")
    
         # Task 2: Odd or Even Checker
num = int(input("Enter a number: "))

if num % 2 == 0: 
    print("The number is EVEN")
else:
    print("The number is ODD")
    
# Task 3: Square or Rectangle Checker

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

if length == breadth:
    print("Dimensions", length, "x", breadth, "form a PERFECT SQUARE")
else:
    print("Dimensions", length, "x", breadth, "form a GENERIC RECTANGLE")
    
  # Task 4: Employee Bonus Calculator

salary = float(input("Enter current salary: "))
years = float(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05   # 5% nikalne ke liye 0.05 se multiply
    print("--- Bonus Details ---")
    print("Current Salary: Rs.", salary)
    print("Years of Service:", years)
    print("Bonus Rate: 5%")
    print("Net Bonus Amount: Rs.", bonus)
else:
    print("No bonus. Years of service", years, "is less than 5 years")  
    
# Task 5: Leap Year Checker

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year", year, "is a LEAP YEAR")
else:
    print("The year", year, "is NOT a LEAP YEAR")