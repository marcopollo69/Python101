#program 1

age = int(input("How old are you? :"))

if age > 18 :
    print("You are a voter")
else:
    print("You are not a voter")


#program 2

temperature = float(input("Enter room temperature e.g 28.5 :"))

if temperature > 25 :
    print("Its Too Hot!")

elif temperature < 25.0:
    print("Its Too Cold!")
else:
    print("Normal Temperature.")

#program 3

first = int(input("Enter first number :"))
second = int(input("Enter second number :"))
third = int(input("Enter third number :"))

if first>second and first>third:
    print(first, "is the largest number")
elif second>first and second>third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")