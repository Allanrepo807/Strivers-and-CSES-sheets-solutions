n = int(input("Enter the value of n: "))
print("Enter the number squence in space seperated format where number of " \
"digits in sequence is n-1 in the range 1 to n inclusive")
arr = list(map(int,input().split()))
total = n*(1+n)//2
arr_sum = sum(arr)
print("The missing term is:" ,total-arr_sum)

