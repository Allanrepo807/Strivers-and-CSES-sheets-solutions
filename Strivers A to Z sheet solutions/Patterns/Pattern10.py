r = int(input("Enter the number of rows: "))
for i in range(1, r + 1):
    print('*' * i)
    
for i in range(r - 1, 0, -1):
    print('*' * i)