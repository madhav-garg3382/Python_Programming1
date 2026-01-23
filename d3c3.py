nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

nums = list(set(nums))
nums.sort()

print("largest number is:", nums[-2])