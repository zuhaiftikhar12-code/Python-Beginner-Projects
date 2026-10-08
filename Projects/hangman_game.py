import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {
    0: (
        "   ------ ",
        "   |    |",
        "   |    ",
        "   | ",
        "   | ",
        "   | ",
        "---------",
    ),
    1: (
        "   ------ ",
        "   |    |",
        "   |    o",
        "   | ",
        "   | ",
        "   | ",
        "---------",
    ),
    2: (
        "   ------ ",
        "   |    |",
        "   |    o",
        "   |    |",
        "   | ",
        "   | ",
        "---------",
    ),
    3: (
        "   ------ ",
        "   |    |",
        "   |    o",
        "   |   /|",
        "   | ",
        "   | ",
        "---------",
    ),
    4: (
        "   ------ ",
        "   |    |",
        "   |    o",
        "   |   /|\\",
        "   | ",
        "   | ",
        "---------",
    ),
    5: (
        "   ------ ",
        "   |    |",
        "   |    o",
        "   |   /|\\",
        "   |   /  ",
        "   | ",
        "---------",
    ),
    6: (
        "   ------ ",
        "   |    |",
        "   |    o",
        "   |   /|\\",
        "   |   / \\ ",
        "   | ",
        "---------",
    ),
}


def display_man(wrong_guesses):
    print("*********")
    for l in hangman_art[wrong_guesses]:
        print(l)
    print("*********")


def display_answer(answer):
    print(f"The answer is {answer}")


def display_hint(hint):
    print("----------------")
    print("hint: "," ".join(hint))
    print("----------------")


def main():
    print("======================================================")
    print("            🎮 Welcome To Hangman Game  👾   ")
    print("======================================================")
    while True:
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True
        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            guess = input("Enter a Guess: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input")
                continue

            if guess in guessed_letters:
                print(f"{guess} is already guessed")
                continue

            guessed_letters.add(guess)
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_hint(hint)
                print("You Win! 🎉🎉🎉")
                display_answer(answer)
                break
            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                print("You Lose. Game Over! 😕")
                display_answer(answer)
                break
        choice = input("Do you want to play again (Y/N): ").upper()
        if choice not in "Y":
            break
    print("======================================================")
    print("              Thanks For Playing Game ⭐")
    print("======================================================")


if __name__ == "__main__":
    main()
