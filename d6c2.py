num = int(input("Enter a number "))

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    fact = 1
    for i in range (1,num+1):
        fact *= i
print("factorial of",num,"is",fact)