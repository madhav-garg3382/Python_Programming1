def secret():
    print("🥚 You found the hidden Python egg!")

choice = input("Enter secret code: ")

if choice == "python":
    secret()
else:
    print("Nothing here 👀")
