binary = int(input("Enter a binary number :"))
decimal = 0
power = 1

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit*power
    power = power*2
    binary = binary // 10

print(decimal)
