"""Write a function that calculates a Fibonacci sequence."""


def calc_fibonacci(n: int) -> int:
    """Calculates Fibonacci sequence for n."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calc_fibonacci(n - 1) + calc_fibonacci(n - 2)


def main() -> None:
    """Main function of the module."""
    result: int = calc_fibonacci(0)
    print(result, end="\n\n")
    result = calc_fibonacci(1)
    print(result, end="\n\n")
    result = calc_fibonacci(7)
    print(result, end="\n\n")
    result = calc_fibonacci(12)
    print(result, end="\n\n")


if __name__ == "__main__":
    main()
