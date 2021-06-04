secret_number = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_number = int(input("Guess any number: "))
    guess_count += 1
    if guess_number == secret_number:
        print("You won!")
        break
