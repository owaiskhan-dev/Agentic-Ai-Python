
                #   Topic 1: VARIABLES (5 Assignments)

# Assignment 1: Simple Calculator
X = 10 + 5
Y = 10 - 5
Z = 10 * 5
Q = 10 / 5
print( X, Y, Z, Q)

# Assignment 2: Personal Info Card
name = "Muhammad Owais Khan"
age = 20
hobbie  = " I Love Coding"
print("Hey, I'm",name , "I Am",age, "Year old.",hobbie)

# Assignment 3: Temperature Converter
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Assignment 4: Area of Rectangle
Length = 5
Width = 10
Area = Length * Width
print(Area)

# Assignment 5: Salary Increment
Old_Salary = 50000
Person10 = Old_Salary * 10 / 100
print(Old_Salary)
New_Salary = Old_Salary + Person10
print(New_Salary)


                #  Topic 2: TUPLES (5 Assignments)

# Assignment 1: Favorite Fruits
Fruits= ("Apple", "Mango", "Banana", "Nashpati", "Melon")
print(Fruits)         
print(Fruits[0])       
print(Fruits[4])
print(len(Fruits))

# Assignment 2: Tuple of Marks
marks = (78, 82, 90, 67, 88)
print(min(marks))
print(max(marks))

# Assignment 3: Tuple Slicing
num =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num[0:3])
print(num[7:])
print(num[3:7])

# Assignment 4: Tuple Indexing
cities=("Karachi", "Islamabad", "Lahore", "Sargodha")
print(cities[2])
print(cities[-1])

# Assignment 5: Count & Find in Tuple
color = ('red', 'blue', 'red', 'green', 'red')
print(color.count("red"))
print(color.index("red"))


                #  Topic 3: LISTS (5 Assignments)
# Assignment 1: Student Names
student =["Babar", "Abdullah", "Zeshan", "Akbar", "Husain"]
student.append("Owais")
student.remove("Babar")
print(student)

# Assignment 2: Shopping List
grocery= ['salt', 'white salt', 'black paper', 'souce', 'sugar','atta']
grocery[1] ="milk"
print(grocery)
print(len(grocery))

# Assignment 3: Sorting Practice
num = [ 22, 77, 34, 35, 46, 22, 98, 10, 32]
print(num)
num.sort()
print(num)

# Assignment 4: Favorite Movies
movies =["Pathan", "Jawaan", "Khiladi", "The Last Ride"]
print(movies[0:2])
print(movies[-1])
print(len(movies),movies)

# Assignment 5: Sum of Numbers
nums=[5, 10, 15, 20]
print(sum(nums))
x = sum(nums)
y = len(nums)
Average = x / y
print(Average)


            #   🔢 Topic 4: SETS (5 Assignments)
# Assignment 1: Unique Numbers
nums = {1, 2, 2, 3, 4, 4, 5}
unique_nums = set(nums)
print(unique_nums)

# Assignment 2: Set Operations
A= {1, 2, 3, 4}
B= {3, 4, 5, 6}
U = A.union(B)
print(U)
A= {1, 2, 3, 4}
B= {3, 4, 5, 6}
N = A.intersection(B)
print(N)
A= {1, 2, 3, 4}
B= {3, 4, 5, 6}
D = A.difference(B)
print(D)

# Assignment 3: Adding & Removing
nums = {2, 4, 6}
nums.add(8)
nums.remove(4)
print(nums)

# Assignment 4: Membership Check
nums ={ 1, 2, 3, 4, 6, 7, 8, 9, 10}
if 5 in nums:
 print(True)
else:
 print(False)

# Assignment 5: Convert List to Set
nums =[1, 2, 2, 3, 4, 4, 5]
nums=set([1, 2, 2, 3, 4, 4, 5])
print(nums)
print(type(nums))



            # Topic 5: DICTIONARIES (5 Assignments)
#  Assignment 1: Student Info
student = {
 "name":"Owais Khan",
 "age": 20,
 "grade":"A"
}
print(student["name"],"is",student["age"],"Years old and Got Grade",student["grade"])

# Assignment 2: Update Dictionary
car = {"brand": "Toyota", "year": 2020}
car["color"]= "red"
car.update({"year":2022})
print(car)

# Assignment 3: Loop Through Dictionary
countries = {
    "Pakistan": "Islamabad",
    "Turkey": "Ankara",
    "Japan": "Tokyo"
}
for key, value in countries.items():
     print(key,value)

# Assignment 4: Dictionary of Price
price = {
  "Apple": 1.5,
  "Banana": 2.5,
  "Mango": 0.75
}
for key, value in price.items():
     print(key)
     print( value)

# Assignment 5: Nasted Dictionary   
students = {
  "Ali": {"age": 18, "grade": "A"},
  "Sara": {"age": 19, "grade": "B"}
}
for key, value in students.items():
    print(key),print(value)

   
