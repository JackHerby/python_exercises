"""Write a function that calculates a fibonacci sequence."""


def main():
    """Main function of the module."""

    def calc_fibonacci(n: int) -> int:
        """Calculates fibonacci sequence for n."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        return calc_fibonacci(n - 1) + calc_fibonacci(n - 2)

    f = calc_fibonacci(0)
    print(f, end="\n\n")
    f = calc_fibonacci(1)
    print(f, end="\n\n")
    f = calc_fibonacci(7)
    print(f, end="\n\n")
    f = calc_fibonacci(12)
    print(f, end="\n\n")


if __name__ == "__main__":
    main()
