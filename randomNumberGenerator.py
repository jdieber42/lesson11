import random

# hard-code the secret number
secretNumber = random.randint(1,10)
guess = 0

anzahl = 5

successful = False
tries = 0

best_score = 0
with open("bestScore.txt", "r") as best_file:
    best_score = int(best_file.read())

with open("randomNumber.log", "a") as log_file:

    for x in range(anzahl):
        # read the guess from the user
        guess = int(input("Please guess a number between 1 - 10: "))
        log_file.write(f"Start {x} attempt.\t")

        # tries = tries + 1
        tries += 1

        # compare the guess with the secret - "This is wrong!" / "Congratulation, your guess is right!"
        if secretNumber == guess:
            print(f"Congratulation, your guess is right! Its number {guess}.")
            log_file.write(f"Guess right: {guess}\n")

            successful = True

            if tries < best_score:
                print("***** Perfect this was the best score ever. *****")
                with open("bestScore.txt", "w") as best_file:
                    best_file.write(str(tries))
            break;
        elif not(1 <= guess <= 10):
            print(f"Your guess ({guess}) is not in the range!")
            log_file.write(f"Guess: {guess} is not in range.\n")
        elif guess < secretNumber:
            print("Your guess is to small.")
            log_file.write(f"Guess: {guess} too small.\n")
        elif guess > secretNumber:
            print("Your guess is to high.")
            log_file.write(f"Guess: {guess} is not to high.\n")
        else:
            print(f"Your number was '{guess}', this is wrong...")
            log_file.write(f"Guess: {guess} was wrong.\n")
    else:
        print("Leider hast du es nicht geschaft in {} Versuchen die Nummer zu finden.".format(anzahl))
        log_file.write("Max amount of attempts reached.\n")

    log_file.write(" ---------------------------- \n")

with open("randomNumberStat.csv", "a") as stat_file:
    stat_file.write(f"{secretNumber},{tries},{successful}\n")