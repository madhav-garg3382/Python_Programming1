n = int(input("Enter a number: "))
temp = n
sum1 = 0
while temp > 0:
     digit = temp % 10
     sum1 += digit ** 3
     temp //= 10
if sum1 == n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")         