"""Validating PESEL number
Write a function called validate_pesel,
which takes a PESEL (Polish personal ID) number as a string,
then checks its correctness and returns:

True, if the PESEL is correct,
False, if the PESEL is incorrect.

PESEL consists of 11 digits, where the last one is the control digit.
To validate a PESEL, you should:

- multiply the first ten digits by the corresponding weight,
- sum the obtained products,
- divide the sum by modulo 10,
- subtract the result from 10, if the result is 10, take 0.

If the result of the above operation is equal to the last digit of the PESEL number,
the entire number is correct.

Weights:
1, 3, 7, 9, 1, 3, 7, 9, 1, 3

Example:
Let's check the PESEL 44051401358.
According to the procedure, we check the first ten digits,
the last one (8) is the control digit.

digits: 4, 4, 0, 5, 1, 4, 0, 1, 3, 5
weights: 1, 3, 7, 9, 1, 3, 7, 9, 1, 3
products: 4, 12, 0, 45, 1, 12, 0, 9, 3, 15
Sum the products: 4 + 12 + 0 + 45 + 1 + 12 + 0 + 9 + 3 + 15 = 101

Divide the sum by modulo 10: 101 % 10 = 1

Subtract the modulo division result from 10: 10 - 1 = 9.

The given control digit in the PESEL is 8, so the PESEL is incorrect."""

from typing import List


def main() -> None:
    """Main function of the module."""

    def validate_pesel(pesel: str) -> bool:
        """Validates PESEL number."""
        try:
            if len(pesel) > 11:
                print("PESEL must be 11 characters long.")
                return False
            control_digit: int = int(pesel[10])
            pesel_digits: List[int] = [int(digit) for digit in pesel[:10]]
            weights: List[int] = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            sum_of_products: int = sum(pesel_digits[n] * weights[n] for n in range(10))
            modulo_result: int = sum_of_products % 10
            result: int = 0 if modulo_result == 0 else 10 - modulo_result
            return result == control_digit
        except IndexError:
            print("PESEL must be 11 characters long.")
            return False
        except ValueError:
            print("PESEL should be a string consisting of 11 digits.")
            return False

    # Checks PESEL provided in the task description.
    print(validate_pesel("44051401358"))
    # Other examples.
    print(validate_pesel("69111512345"))
    print(validate_pesel("69111554321"))
    print(validate_pesel("69111554321123123123"))
    print(validate_pesel("def not a n"))
    print(validate_pesel([]))


if __name__ == "__main__":
    main()
