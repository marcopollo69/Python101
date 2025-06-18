from numbers import Number

number = 45 #integer
second = 34.98 #Double
greeting = "Good Morning" #String
Is_Python_Interesting = True #Boolean



#Data Structures
fruits = ["apple", "banana", "cherry"] # List
cars = ("Jeep", "BMW", "Tesla", "Toyota") # Tuple
countries = {"Kenya", "Uganda", "Zambia"} # Set
student = {
    "firstname" : "Victory",
    "lastname" : "Brown",
    "age" : 20,
    "nationality" : "Kenyan",
} # Dictionary - key-value pair


print(number)
print(Is_Python_Interesting)
print(fruits)
print(cars)
print(countries)
print(student)
print(student["nationality"])


# Typecasting - Converting one data type to another
print(float(number))
print(int(second))