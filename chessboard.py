"""
Write a fucntion named `chessboard`, that takes an optional parameter `n` with a default vaule of 8.
The function should return a multi-line chessboard pattern consisting of '#' and ' ' (whitespace),
where '#' and whitespace alternate in both rows and columns.
The size of the chessboard should be n by n.
Expected output for:
```
c = chessboard()
print(c)
```
is:
```
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # # 
```
"""


def main() -> None:
    """Main funcion of the module"""

    def chessboard(n=8) -> str:
        """Creates a chessboard pattern."""
        return "\n".join(
            ["".join(["#" if (x + y) % 2 else " " for x in range(n)]) for y in range(n)]
        )

    c = chessboard()
    print(c, end="\n\n")
    c = chessboard(3)
    print(c, end="\n\n")
    c = chessboard(4)
    print(c, end="\n\n")
    c = chessboard(17)
    print(c, end="\n\n")
    c = chessboard(20)
    print(c, end="\n\n")


if __name__ == "__main__":
    main()
