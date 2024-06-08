"""
Write a simple guessing game.
The computer must randomly select a number in the range of 1 to 100.
Then:

Ask the question: "Guess the number: " and get the number from the keyboard.
Check if the input is indeed a number and display the message
"It's not a number!" if there is an error, then return to step 1.
If the number entered by the user is smaller than the randomly selected one,
display the message "Too small!", then return to step 1.
If the number entered by the user is greater than the randomly selected one,
display the message "Too big!", then return to step 1.
If the number entered by the user is equal to the randomly selected one,
display the message "You win!", then end the program.
Example:
Guess the number: hello
It's not a number!
Guess the number: 50
Too small!
Guess the number: 75
Too big!
Guess the number: 63
You win!
"""

from random import randint


def main() -> None:
    """Main function of a module."""

    def get_prompt() -> int:
        """Gets user prompt

        Returns:
        str: user's prompt
        """
        while True:
            try:
                prompt = int(input("Your guess: ").strip())
                if not 1 <= prompt <= 100:
                    print("You must pick a number between 1 and 100!")
                    continue
                break
            except ValueError:
                print("You must type in a number!")
        return prompt

    def guess_number() -> None:
        """Implements guess number game."""
        guess_count = 1
        number_to_guess = randint(1, 100)
        print("Try and guess a random number between 1 and 100.")
        user_prompt = get_prompt()
        while user_prompt != number_to_guess:
            if user_prompt > number_to_guess:
                print("Too much!")
                guess_count += 1
                user_prompt = get_prompt()
            if user_prompt < number_to_guess:
                print("Too little!")
                guess_count += 1
                user_prompt = get_prompt()
        print(f"You win! Number of guesses: {guess_count}")

    guess_number()


if __name__ == "__main__":
    main()
