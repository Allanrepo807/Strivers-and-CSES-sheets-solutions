r = int(input("Enter the number of rows: "))
for i in range(r, 0, -1):
    print(' ' * (r - i), '*' * (2 * i - 1), sep=' ')

