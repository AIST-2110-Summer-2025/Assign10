from typing import List


def bleepit(text: str, bleeps: List[str]) -> int:
    """
    Print `text` with all instances of any of the words in `bleeps` replaces
    with asterisks. Returns the count of words bleeped.

    CHALLENGE: Preserve punctuation (comma, period, question mark, exclamation
    point, semi-colon). (hint: the punctuation will be the last character of
    word after you do the .split() to turn the words into a list.)
    """
    punctuation = ",.?!;"  # this might help

    # REPLACE BOTH OF THESE LINES BASED ON THE INSTRUCTIONS IN THE README
    print(text)
    return 0


def main():
    """Main entry point for the program."""
    dune = """
I must not fear. Fear is the mind-killer. Fear is the little-death that brings
total obliteration. I will face my fear. I will permit it to pass over me and
through me. And when it has gone past I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain.
"""
    count = bleepit(dune, ["fear", "it", "gone"])
    print(f"{count} words bleeped")
    # I must not ****. **** is the mind-killer. **** is the little-death that
    # brings total obliteration. I will face my ****. I will permit ** to pass
    # over me and through me. And when ** has **** past I will turn the inner
    # eye to see its path. Where the **** has **** there will be nothing. Only I
    # will remain.
    # 9 words bleeped

    castle = """
What they do not comprehend is man's helplessness. I am weak, small, and of no
consequence to the universe.  It does not notice me; I live on unseen.  But why
is that bad?  Isn't it better that way?  Whom the gods notice they destroy.  But
small, and you will escape the jealousy of the great.
"""
    count = bleepit(castle, ["small", "weak", "bad", "not", "me"])
    print(f"{count} words bleeped")
    # What they do *** comprehend is man's helplessness. I am ****, *****, and
    # of no consequence to the universe. It does *** notice **; I live on
    # unseen. But why is that ***? Isn't it better that way? Whom the gods
    # notice they destroy. But *****, and you will escape the jealousy of the
    # great.
    # 7 words bleeped


if __name__ == "__main__":
    main()
