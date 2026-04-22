import random
import pyjokes

def game():
    print("💻 SYSTEM ACCESS GAME")
    print("Guess the secret number (1 to 5)")
    print("You have 3 attempts...\n")

    secret_number = random.randint(1, 5)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input(f"Attempt {4 - attempts}/3 → Enter your guess: "))

            if guess == secret_number:
                print("\n🔓 ACCESS GRANTED...")
                print("☠️ Dark Joke:", pyjokes.get_joke(category='neutral'))
                return
            else:
                attempts -= 1
                print("❌ Wrong guess!")

        except ValueError:
            print("⚠️ Enter a valid number!")

    print(f"\n💀 \t SYSTEM LOCKED! The number was {secret_number}")
    print("No jokes for intruders 🚫")


game()