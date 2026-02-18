m = int(input("Enter the number of rows : "))
n = int(input("Enter the number of column :"))

for i in range (m):
    for j in range(n):
        print(i*j,end ="")
    print()