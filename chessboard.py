"""
Write a function named `chessboard`, that takes an optional parameter `n` with a default value of 8.
The function should return a multi-line chessboard pattern consisting of '#' and ' ' (white space),
where '#' and white space alternate in both rows and columns.
The size of the chessboard should be n by n.
Expected output for:

board = chessboard()
print(board)

is:
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
"""


def chessboard(n: int = 8) -> str:
    """Creates a chessboard pattern."""
    return "\n".join(
        ["".join(["#" if (x + y) % 2 else " " for x in range(n)]) for y in range(n)]
    )


def main() -> None:
    """Main function of the module."""
    board: str = chessboard()
    print(board, end="\n\n")
    board = chessboard(3)
    print(board, end="\n\n")
    board = chessboard(4)
    print(board, end="\n\n")
    board = chessboard(17)
    print(board, end="\n\n")
    board = chessboard(20)
    print(board, end="\n\n")


if __name__ == "__main__":
    main()
