from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_check_guess_with_string_secret():
    # FIX: Added test for bug when secret is str, using Copilot Agent mode
    # Test that even when secret is passed as string, comparison works correctly
    assert check_guess(5, "10") == ("Too Low", "📉 Go LOWER!")
    assert check_guess(15, "10") == ("Too High", "📈 Go HIGHER!")
    assert check_guess(10, "10") == ("Win", "🎉 Correct!")
