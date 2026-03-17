# FIX: Refactored each logic util from app.py into this file using Claude's "readme" (CLAUDE.md) function


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50 # The number ranges between normal and hard modes are swapped
        # FIX: Normal now returns 1-50 and Hard returns 1-100, making Hard the wider and harder range as we wanted
    if difficulty == "Hard":
        return 1, 100
    return 1, 100
    # FIX: implemented get_range_for_difficulty, moved from app.py into logic_utils.py where it belongs


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None
    # FIX: implemented parse_guess, moved from app.py into logic_utils.py


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret: # The hint points the player in the wrong direction
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
        # FIX: when guess > secret the hint correctly says "Go LOWER", and when guess < secret it says "Go HIGHER"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    # FIX: implemented check_guess, moved from app.py into logic_utils.py where it belongs


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number-1) # If the user were to win on the first attempt, since we increment count before this, it will calculate as if we are on the secon attempt. We should change it to minus 1.
        # FIX: changed (attempt_number + 1) to (attempt_number - 1) so a first-attempt win gives 100 points, second gives 90, etc.
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        current_score -= 5
        if current_score <= 0:
            current_score = 0
        return current_score

    if outcome == "Too Low":
        current_score -= 5
        if current_score <= 0:
            current_score = 0
        return current_score

    return current_score
    # FIX: implemented update_score, moved from app.py into logic_utils.py where it belongs
