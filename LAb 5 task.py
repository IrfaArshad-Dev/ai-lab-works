#task 1#
tools=["canva","figma","gemini","cahtgpt","Claude"]
for i in tools:
    print(i)
print("-----------------------------------------")

#task 2
language=input ("enter tah languages:")   
for i in language:
    print(i)
print("-----------------------------------------")

#task 3
courses = ["ai", "os", "dsa", "db", "machine learning", "deep learning"]
search = input("Enter an item to search: ")
for i in courses:
    if i == search:
        print("Found")
        break
else:
    print("Not found")
print("-----------------------------------------")
    
#task 4
attributes=["fast","accurate","Relaiable"]
app=["CHATGPT","CLAUDE","GEMINI"]
for i in attributes:
    for j in app:
        print(i,j)  
print("-----------------------------------------")

#task 5    
models=["ai","deepseek","studely"]
scores=[55,78,90]
total=0
print("models with scores:")
print(models,":",scores)
for i in scores:
    total+=i
avg=total/3
print("THE TOTAL SCORES ARE",total)
print("THE AVERAAGE IS :",avg) 
   