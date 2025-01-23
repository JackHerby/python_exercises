"""
Workshop: LOTTO Simulator.
As you probably know,
LOTTO is a numerical game based on drawing 6 numbers from the range 1 - 49.
The player's task is to correctly guess the drawn numbers.
Guessing 3, 4, 5, or 6 correct numbers is rewarded.

Write a program that:

Asks for the guessed numbers,
and at the same time checks the following conditions:
- whether the entered sequence of characters is a valid number,
- whether the user has not entered this number previously,
- whether the number belongs to the range 1-49.

After entering 6 numbers,
sorts them in ascending order and displays them on the screen.

Randomly draws 6 numbers from the range and displays them on the screen,
informs the player how many numbers they hit.
"""

from random import sample
from typing import List, Set


def get_number() -> int:
    """Gets and validates a number from the user.

    Returns
    -------
    int
        User's chosen number.
    """
    while True:
        try:
            number = int(input("Pick a number: ").strip())
            break
        except ValueError:
            print("Invalid input type!")
    return number


def get_numbers() -> List[int]:
    """Creates a list of 6 numbers picked by the user.
    Checks wether the number has already been picked.
    Sorts the list in ascending order.

    Returns
    -------
    list[int]
        List of six unique numbers.
    """
    numbers: List[int] = []
    while len(numbers) < 6:
        number = get_number()
        if number in numbers:
            print("This number has already been picked, choose another one.")
            continue
        if not 1 <= number <= 50:
            print("The number must be between 1 and 50.")
            continue
        numbers.append(number)
    numbers.sort()
    return numbers


def draw_numbers() -> List[int]:
    """Generates six random unique numbers between 1 and 50 in ascending order.

    Returns
    -------
    list[int]
        List of six random unique numbers.
    """
    numbers = sample(range(1, 50), k=6)
    numbers.sort()
    return numbers


def print_numbers(numbers: List[int]):
    """Displays a list of numbers.

    Parameters
    ----------
    numbers : list[int]
        List of numbers to display.
    """
    print(", ".join([str(number) for number in numbers]))


def main() -> None:
    """Main function."""
    user_numbers: List[int] = get_numbers()
    print("You've chosen: ", end=" ")
    print_numbers(user_numbers)
    drawn_numbers: List[int] = draw_numbers()
    print("The drawn numbers are: ", end=" ")
    print_numbers(drawn_numbers)
    result: Set[int] = set(drawn_numbers).intersection(user_numbers)
    print(f"Number of matches: {len(result)}")
    if len(result) > 0:
        print_numbers(list(result))


if __name__ == "__main__":
    main()
