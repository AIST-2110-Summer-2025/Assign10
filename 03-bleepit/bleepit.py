from typing import List


def bleepit(text: str, bleeps: List[str]) -> int:
    """
    Print `text` with all instances of any of the words in `bleeps` replaces
    with asterisks. Returns the count of words bleeped.
    """
    # REPLACE BOTH OF THESE LINES BASED ON THE INSTRUCTIONS IN THE README
    print(text)
    return 0


def main():
    """Main entry point for the program."""
    prince = "The most beautiful things in the world cannot be seen or touched they are felt with the heart"
    count = bleepit(prince, ["beautiful", "world"])
    print(f"{count} words bleeped")
    # The most ********* things in the ***** cannot be seen or touched they are felt with the heart
    # 2 words bleeped
    count = bleepit(prince, ["the"])
    print(f"{count} words bleeped")
    # *** most beautiful things in *** world cannot be seen or touched they are felt with *** heart
    # 3 words bleeped

    dune = """
I must not fear
Fear is the mind-killer
Fear is the little-death that brings total obliteration
I will face my fear
I will permit it to pass over me and through me
And when it has gone past I will turn the inner eye to see its path
Where the fear has gone there will be nothing
Only I will remain
"""
    count = bleepit(dune, ["fear", "will", "gone"])
    print(f"{count} words bleeped")
    # I must not **** **** is the mind-killer **** is the little-death that
    # brings total obliteration I **** face my **** I **** permit it to pass
    # over me and through me And when it has **** past I **** turn the inner eye
    # to see its path Where the **** has **** there **** be nothing Only I ****
    # remain
    # 12 words bleeped


if __name__ == "__main__":
    main()
