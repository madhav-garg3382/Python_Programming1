class ArrayOperations:
    def __init__(self):
        
        self.list1 = [10, 20, 30]
        self.list2 = [2, 4, 6]

    def addition(self):
        return [self.list1[i] + self.list2[i] for i in range(len(self.list1))]

    def subtraction(self):
        return [self.list1[i] - self.list2[i] for i in range(len(self.list1))]

    def multiplication(self):
        return [self.list1[i] * self.list2[i] for i in range(len(self.list1))]

    def division(self):
        return [self.list1[i] / self.list2[i] for i in range(len(self.list1))]

    def transpose(self):
        
        matrix = [self.list1, self.list2]
        transpose_matrix = []

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            transpose_matrix.append(temp)

        return transpose_matrix



obj = ArrayOperations()

print("List 1:", obj.list1)
print("List 2:", obj.list2)

print("\nChoose Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Transpose")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    print("Addition:", obj.addition())

elif choice == 2:
    print("Subtraction:", obj.subtraction())

elif choice == 3:
    print("Multiplication:", obj.multiplication())

elif choice == 4:
    print("Division:", obj.division())

elif choice == 5:
    print("Transpose:")
    for row in obj.transpose():
        print(row)

else:
    print("Invalid Choice")
