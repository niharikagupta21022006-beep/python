# Light = input("Ligit color : ")
# if(Light == "Red"):
#     print("Stop")

# elif(Light == "Yellow"):
#     print("Look")

# elif(Light == "Green"):
#     print("Go")

# else:
#     print("Light is broken")

# food = input("food : ")
# eat = "yes" if food == "cake" else "no"
# print(eat)

sal = float(input("Salary : "))
tax = sal*(0.1,0.2) [sal >50000]
print(tax)








# -----------------------------------------
# 1. Store name, age, height and print them
# -----------------------------------------
name = "Niharika Gupta"
age = 19
height = 5.4

print("Name:", name)
print("Age:", age)
print("Height:", height)


# ---------------------------------------------------
# 2. Demonstrate arithmetic operators
# ---------------------------------------------------
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# ---------------------------------------------------
# 3. List of 5 integers
# ---------------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("Entire list:", num…

# 3. List of 5 integers
# ---------------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("Entire list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# ---------------------------------------------------
# 4. Tuple of three subjects
# ---------------------------------------------------
subjects = ("Maths", "Physics", "Python")

print("Subject 1:", subjects[0])
print("Subject 2:", subjects[1])
print("Subject 3:", subjects[2])


# ---------------------------------------------------
# 5. Dictionary order expressions
# ---------------------------------------------------
words = ['cat', 'car', 'camel', 'cup', 'cap']

print("First word (dictionary order):", min(words))
print("Last word (dictionary order):", max(words))


# ---------------------------------------------------
# 6. Create a set from list
# ---------------------------------------------------
lst = [1, 2, 2, 3, 4, 4, 5]
s = set(lst)

print("Set:", s)


# ---------------------------------------------------
# 7. Length of a string entered by user
# ---------------------------------------------------
string = input("Enter a string: ")
length = 0

for ch in string:
    length += 1

print("Length of string:", length)


# ---------------------------------------------------
# 8. Python algebraic expressions
# ---------------------------------------------------
avg_age = (23 + 19 + 31) / 3
print("Average age:", avg_age)

times = 403 // 73
print("73 goes into 403:", times, "times")

remainder = 403 % 73
print("Remainder:", remainder)

power = 2 ** 10
print("2 to the power 10:", power)

lowest_price = min(34.99, 34.99, 29.95, 31.50)
print("Lowest price:", lowest_price)


# ---------------------------------------------------
# 9. Boolean expressions
# ---------------------------------------------------
print("2 + 2 < 4:", 2 + 2 < 4)
print("7 // 3 == 1 + 1:", 7 // 3 == 1 + 1)
print("3^2 + 4^2 == 25:", 3*2 + 4*2 == 25)
print("Lowest price < 31.50 < 30.00:",
      min(34.99, 34.99, 29.95, 31.50) < 31.50 < 30.00)
print("2 + 4 + 6 > 12:", 2 + 4 + 6 > 12)


# ---------------------------------------------------
# 10. Variable assignment
# ---------------------------------------------------
a = 3
b = 4
c = a + b

print("a =", a)
print("b =", b)
print("c =", c)


# ---------------------------------------------------
# 11. String expressions
# ---------------------------------------------------
s1 = "ant"
s2 = "bat"
s3 = "cod"

print(s1 + " " + s2 + " " + s3)
print((s1 + " ") * 8)
print(s1 + " " + s2 + " " + s2 + " " + s3 + " " + s3)
print((s1 + " " + s2 + " ") * 6)
print((s2 + s3) * 5)
