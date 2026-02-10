num = int(input("Enter a number "))
rev = 0
negative = num < 0
num = abs(num)

while num > 0:
  digit = num % 10
  rev = rev*10+digit 
  num = num // 10 
  
if negative:
  rev = -rev
print("Reversed number is", rev)