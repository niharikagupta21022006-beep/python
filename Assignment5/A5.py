num = int(input("Enter a decimal number:"))
binary = 0
place = 1

while num > 0:
    rem = num % 2
    binary = binary + rem * place
    place = place *10
    num = num // 2

print("Binary = ",binary)


