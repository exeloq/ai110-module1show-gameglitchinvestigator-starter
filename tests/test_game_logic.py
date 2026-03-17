from logic_utils import check_guess, update_score
from streamlit.testing.v1 import AppTest

def test_new_game_button_resets_status():
    # Reproduce the bug: after game ends, clicking New Game should clear the game-over status
    at = AppTest.from_file("app.py")
    at.run()

    # Force the session into a game-over state (simulating a loss)
    at.session_state["status"] = "lost"
    at.run()

    # Click the New Game button (index 1, after Submit Guess)
    at.button[1].click().run()

    # Before the fix, status stayed "lost" so st.stop() immediately blocked the new game
    assert at.session_state["status"] == "playing"

def test_new_game_button_resets_score():
    # Score should reset to 0 when New Game is clicked
    at = AppTest.from_file("app.py")
    at.run()

    # Give the player a non-zero score
    at.session_state["score"] = 50
    at.run()

    # Click New Game
    at.button[1].click().run()

    assert at.session_state["score"] == 0

def test_difficulty_change_resets_score():
    # Score should reset to 0 when difficulty changes
    at = AppTest.from_file("app.py")
    at.run()

    # Give the player a non-zero score on Normal
    at.session_state["score"] = 50
    at.session_state["difficulty"] = "Normal"
    at.run()

    # Change difficulty to Hard via the selectbox (index 0=Easy, 1=Normal, 2=Hard)
    at.selectbox[0].select("Hard").run()

    assert at.session_state["score"] == 0

def test_difficulty_change_new_secret_in_range():
    # Switching to Easy should generate a secret between 1 and 20
    at = AppTest.from_file("app.py")
    at.run()

    at.selectbox[0].select("Easy").run()

    assert 1 <= at.session_state["secret"] <= 20

def test_difficulty_change_resets_attempts():
    # Attempts should reset to 0 when difficulty changes
    at = AppTest.from_file("app.py")
    at.run()

    at.session_state["attempts"] = 4
    at.session_state["difficulty"] = "Normal"
    at.run()

    at.selectbox[0].select("Hard").run()

    assert at.session_state["attempts"] == 0

def test_difficulty_change_resets_status():
    # A game-over status should be cleared when difficulty changes
    at = AppTest.from_file("app.py")
    at.run()

    at.session_state["status"] = "lost"
    at.session_state["difficulty"] = "Normal"
    at.run()

    at.selectbox[0].select("Easy").run()

    assert at.session_state["status"] == "playing"

def test_score_first_attempt_win():
    # Winning on the first attempt should give 100 points
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 100

def test_score_second_attempt_win():
    # Winning on the second attempt should give 90 points
    score = update_score(current_score=0, outcome="Win", attempt_number=2)
    assert score == 90

def test_score_decreases_on_wrong_guess():
    # A wrong guess should subtract 5 from the score
    score = update_score(current_score=100, outcome="Too High", attempt_number=1)
    assert score == 95

def test_score_floors_at_zero():
    # Score should never go below 0
    score = update_score(current_score=3, outcome="Too Low", attempt_number=1)
    assert score == 0

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
    
# FIX: Fixed the pre existing test cases that tested the results of guesses (high/low/correct)