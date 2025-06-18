# A python program that checks whether a number is even or odd

number = int(input("Enter a number: "))

if number == 0:
    print(number, "is Neutral")
elif number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

    print()

# A python program that checks whether a letter is a vowel or consonant

letter = input("Enter a letter: ").lower()

if letter == 'a' or letter == 'e' or letter== 'i' or letter == 'e' or letter == 'o' or letter == 'u':
    print(letter, "is a vowel")

else:
    print(letter, "is a consonant")


print()

# A python program that returns the perimetr of a rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = (2 * (length + width))

print("The perimeter is:", perimeter)