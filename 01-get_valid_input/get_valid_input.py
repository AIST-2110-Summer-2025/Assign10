from typing import List


def get_valid_input(prompt: str, valid_vals: List[str]) -> str:
    """
    Ask the user to input a value using the prompt parameter. Validate that the
    value is one of the items in the valid_vals list per the instructions in the
    README and return the user's choice.

    Note the use of more advanced type hints on this one.
        - prompt: str           prompt should be a string
        - valid_vals: List[str] valid_vals should be a list containing strings

    To use the `List` hint, you needed to import it from the typing module.
    """
    return input(prompt)  # REPLACE ME!!!


###############################################################################
# main function. Look but no need to touch.
###############################################################################


def main():
    """Main entry point for the program."""
    beatle = get_valid_input("Favorite Beatle: ", ["John", "Paul", "George", "Ringo"])
    print(f"Your favorite Beatle is {beatle.title()}")
    color = get_valid_input("Favorite color: ", ["red", "YELLOW", "BlUe", "GReeN"])
    print(f"Your favorite color is {color}")


if __name__ == "__main__":
    main()
