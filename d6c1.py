num = int(input("Enter a number "))
count = 0

num = abs(num)

if num == 0:
  count = 1
else:
  while num > 0:
    num =num // 10
    count +=1

    print("Total digits: ", count)