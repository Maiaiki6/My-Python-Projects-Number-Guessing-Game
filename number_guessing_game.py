import random


def generate_target(low=1, high=100):
    """Generate a random integer between low and high (inclusive)."""
    return random.randint(low, high)


def check_guess(guess: int, target: int) -> str:
    """Return feedback string: 'correct', 'low', or 'high'."""
    if guess == target:
        return "correct"
    if guess < target:
        return "low"
    return "high"


def play(max_attempts: int = 10):
    """Run the interactive number guessing game."""
    target = generate_target(1, 100)
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        try:
            guess_input = input(f"Attempt {attempts}/{max_attempts} - Enter your guess: ")
            guess = int(guess_input.strip())
        except ValueError:
            print("Please enter a valid integer.")
            attempts -= 1
            continue

        feedback = check_guess(guess, target)
        if feedback == "correct":
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            return True
        if feedback == "low":
            print("Too low.")
        else:
            print("Too high.")

    print(f"Sorry — you've used all {max_attempts} attempts. The number was {target}.")
    return False


def self_test():
    """Non-interactive self-test to verify core logic."""
    # deterministic check for check_guess
    assert check_guess(50, 42) == "high"
    assert check_guess(30, 42) == "low"
    assert check_guess(42, 42) == "correct"

    # basic generate_target sanity: should be within bounds
    random.seed(0)
    val = generate_target(1, 100)
    assert 1 <= val <= 100

    print("self-test: OK")


if __name__ == "__main__":
    play()
