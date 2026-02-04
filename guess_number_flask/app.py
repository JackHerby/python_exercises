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
        Computer's guess calculated with binary search algorithm.
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


@app.route("/game", methods=["GET", "POST"])
def main() -> Response | str:
    """Executes the number guessing game"""
    if request.method == "POST":
        upper_bound = int(request.form["upper_bound"])
        lower_bound = int(request.form["lower_bound"])
        step = int(request.form["step"]) + 1
        guess = calculate_answer(upper_bound, lower_bound)
        user_input = request.form["button"]
        match user_input:
            case "too_much":
                upper_bound = guess
                guess = calculate_answer(upper_bound, lower_bound)
                return render_template(
                    "game.html",
                    upper_bound=upper_bound,
                    lower_bound=lower_bound,
                    step=step,
                    guess=guess,
                )
            case "too_little":
                lower_bound = guess
                guess = calculate_answer(upper_bound, lower_bound)
                return render_template(
                    "game.html",
                    upper_bound=upper_bound,
                    lower_bound=lower_bound,
                    step=step,
                    guess=guess,
                )
            case "guessed":
                step = int(request.form["step"])
                return redirect(url_for("game_over", step=step))
    return render_template(
        "game.html", upper_bound=1000, lower_bound=0, step=1, guess=500
    )


@app.route("/game_over", methods=["GET", "POST"])
def game_over() -> Response | str:
    """End game screen
    Press button to restart the game.
    """
    if request.method == "POST":
        return redirect("/")
    step = int(request.args.get("step") or 0)
    return render_template("game_over.html", step=step)


if __name__ == "__main__":
    app.run()
