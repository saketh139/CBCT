import random

def generate_number():
    return str(random.randint(1000, 9999))

def check_guess(secret_number, guess):
    correct_digits = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            correct_digits += 1
    return correct_digits

def main():
    print("Welcome to Mastermind!")
    print("Player 1, please enter your secret 4-digit number.")
    secret_number_p1 = input("Player 1: ")

    while len(secret_number_p1) != 4 or not secret_number_p1.isdigit():
        print("Please enter a valid 4-digit number.")
        secret_number_p1 = input("Player 1: ")

    print("Player 2, try to guess Player 1's number!")
    attempts_p2 = 0

    while True:
        guess_p2 = input("Player 2: ")

        while len(guess_p2) != 4 or not guess_p2.isdigit():
            print("Please enter a valid 4-digit number.")
            guess_p2 = input("Player 2: ")

        attempts_p2 += 1
        correct_digits = check_guess(secret_number_p1, guess_p2)
        if correct_digits == 4:
            print("Congratulations! Player 2 wins!")
            break
        else:
            print("You got", correct_digits, "digits correct. Keep guessing!")

    print("Player 2 took", attempts_p2, "attempts.")

    print("Now, it's Player 2's turn to set the number.")
    secret_number_p2 = input("Player 2: ")

    while len(secret_number_p2) != 4 or not secret_number_p2.isdigit():
        print("Please enter a valid 4-digit number.")
        secret_number_p2 = input("Player 2: ")

    print("Player 1, try to guess Player 2's number!")
    attempts_p1 = 0

    while True:
        guess_p1 = input("Player 1: ")

        while len(guess_p1) != 4 or not guess_p1.isdigit():
            print("Please enter a valid 4-digit number.")
            guess_p1 = input("Player 1: ")

        attempts_p1 += 1
        correct_digits = check_guess(secret_number_p2, guess_p1)
        if correct_digits == 4:
            print("Congratulations! Player 1 wins!")
            break
        else:
            print("You got", correct_digits, "digits correct. Keep guessing!")

    print("Player 1 took", attempts_p1, "attempts.")

    if attempts_p1 < attempts_p2:
        print("Player 1 is crowned Mastermind!")
    elif attempts_p2 < attempts_p1:
        print("Player 2 is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
