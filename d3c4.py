s = input("Enter sentence: ")
words = s.split()

result = []
for w in words:
    result.append(w[::-1])
print(" ".join(result))
    