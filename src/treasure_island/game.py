"""A small choose-your-own-adventure game."""

from collections.abc import Callable

BANNER = r"""
   ______                                   ____     __             __
  /_  __/_____ ___  ____ ______ __ _______ /  _/___ / /__ ____  ___/ /
   / / / __/ -_) _ `/ _ `(_-</ // / __/ -_)/ // _ `/ / _ `/ _ \/ _  /
  /_/ /_/  \__/\_,_/\_,_/___/\_,_/_/  \__/___/\_,_/_/\_,_/_//_/\_,_/
                          _______
                      ___/       \___
                  ___/   X marks     \___
                 ~~~~~~~~ the spot ~~~~~~~~
"""

Ask = Callable[[str], str]
Say = Callable[[str], None]


def choose(ask: Ask, prompt: str, options: tuple[str, ...]) -> str:
    """Ask until the player types one of the options (case-insensitive)."""
    while True:
        answer = ask(prompt).strip().lower()
        if answer in options:
            return answer


def play(ask: Ask = input, say: Say = print) -> bool:
    """Run the game. Returns True if the player wins."""
    say(BANNER)
    say("Welcome to Treasure Island.")
    say("Your mission is to find the treasure.")

    if choose(ask, 'You\'re at a crossroad. Type "left" or "right": ', ("left", "right")) == "right":
        say("You fell into a hole. Game Over.")
        return False

    if choose(ask, 'You come to a lake. Type "wait" for a boat or "swim" to swim across: ', ("wait", "swim")) == "swim":
        say("You were attacked by angry trout. Game Over.")
        return False

    door = choose(
        ask,
        'You arrive at an island. There are three doors: "red", "yellow" and "blue". Which one? ',
        ("red", "yellow", "blue"),
    )
    if door == "yellow":
        say("You found the treasure. You Win!")
        return True
    if door == "red":
        say("You were burned by fire. Game Over.")
    else:
        say("You were eaten by beasts. Game Over.")
    return False


def main() -> None:
    play()


if __name__ == "__main__":
    main()
