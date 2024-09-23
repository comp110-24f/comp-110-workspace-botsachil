__author__: str = "730771296"


def guess_a_number() -> None:
    secret: int = 7
    """the number they need to guess is 7"""

    guess_a_number: str = input("Guess a number:")
    print("Your guess was " + str(int(guess_a_number)))
    """This displays the number you guessed"""
    if int(guess_a_number) == secret:
        print("You got it!")
        """if you guessed the number correct"""
    elif int(guess_a_number) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
        """if your guess was lower than the real number"""
    else:
        print("Your guess was too high! The secret number is " + str(secret))
        """if your guess was higher than the real number"""


if __name__ == "__main__":
    guess_a_number()
