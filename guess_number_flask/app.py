from flask import Flask, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

app = Flask(__name__)


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


@app.route("/", methods=["GET", "POST"])
def home() -> Response | str:
    """Renders welcome Message
    The OK button redirects user to the game route
    """
    if request.method == "POST":
        return redirect("game")
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run()
