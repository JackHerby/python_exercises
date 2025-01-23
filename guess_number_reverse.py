"""
Let's now reverse the situation from the first task ("Guess the Number Game").
Let the user think of a number in the range of 1-1000, and the computer will try to guess it.
The computer will do this in a maximum of 10 moves (provided the player does not cheat).

The player's task will be to respond with "Too small," "Too big," or "You win."
"""


def get_user_input() -> int:
    """Returns user's feedback on computer's guess.
    Provides optins to choose from: 1, 2, or 3.

    Returns
    -------
    int
        Option's index representing user's choice.
    """
    options = {1: "Too much", 2: "Too little", 3: "That's correct!"}
    print(", ".join(f"{key}, {value}" for key, value in options.items()))
    print()
    while True:
        try:
            answer = int(input("Your answer: "))
            if answer in options:
                break
            else:
                print("Please type 1, 2 or 3")
        except ValueError:
            print("You must type in a number.")
    return answer


def calculate_answer(upper_bound: int, lower_bound: int) -> int:
    """A binary search algorithm to guess the number.

    Parameters
    ----------
    upper_bound : int
        The current upper limit of the search range.
    lower_bound : int
        The current lower limit of the search range.

    Returns
    -------
    int
        Comuter's guess calculated with binary search algorithm.
    """
    return (upper_bound - lower_bound) // 2 + lower_bound


def main() -> None:
    """Executes the number guessing game"""
    print(
        "Think of a number between 1 and  1000. I'll guess it in no more than 10 steps."
    )
    print("Press enter to continue.")
    upper_bound = 1000
    lower_bound = 0
    step = 1
    while step <= 10:
        print()
        guess = calculate_answer(upper_bound, lower_bound)
        print(f"Step: {step}.")
        print(f"My guess: {guess}.")
        user_answer = get_user_input()

        if user_answer == 1:
            upper_bound = guess
        elif user_answer == 2:
            lower_bound = guess
        else:
            print("I win!")

        step += 1
    print("I've failed, you win!")


if __name__ == "__main__":
    main()
