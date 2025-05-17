from typing import List


def size_finder(paragraph: str, size: int) -> List[str]:
    """
    Given a paragraph of text, return a list of all words in the paragraph that
    are exactly `size` characters long.
    """
    # ADD VALIDATION HERE:
    #   raise ValueError if:
    #       - paragraph is not an instance of str
    #       - size is not an instance of int
    #       - size is not > 0 and < 20

    # Remove all punctuation and create a list of all words (you're welcome)
    punc_free_para = paragraph.replace(".", "")
    punc_free_para = punc_free_para.replace("!", "")
    punc_free_para = punc_free_para.replace("?", "")
    punc_free_para = punc_free_para.replace(",", "")
    punc_free_para = punc_free_para.replace(";", "")
    punc_free_para = punc_free_para.replace("-", " ")
    all_words = punc_free_para.split()

    # REPLACE the next line with logic that:
    #   - creates a new list
    #   - adds words from all_words to this list if they are size letters long
    #   - returns the new list

    return all_words


###############################################################################
# main function. Look but no need to touch.
###############################################################################


def main():
    """Main entry point for the program."""

    tale = """
It was the best of times, it was the worst of times, it was the age of wisdom,
it was the age of foolishness, it was the epoch of belief, it was the epoch of
incredulity, it was the season of Light, it was the season of Darkness, it was
the spring of hope, it was the winter of despair, we had everything before us,
we had nothing before us, we were all going direct to Heaven, we were all going
direct the other way — in short, the period was so far like the present period,
that some of its noisiest authorities insisted on its being received, for good
or for evil, in the superlative degree of comparison only.
"""
    tale_of_two_letters = size_finder(tale, 2)
    print(tale_of_two_letters)  # [bunch of 2-letter strings]
    print(len(tale_of_two_letters))  # should be 34
    tale_of_sevens = size_finder(tale, 7)
    print(tale_of_sevens)  # ['despair', 'nothing', 'present']
    print(len(tale_of_sevens))  # 3

    poe = """
Once upon a midnight dreary, as I pondered weak and weary,
Over many a quaint and curious volume of forgotten lore
While I nodded, nearly napping, suddenly there came a tapping,
As of someone gently rapping, rapping at my chamber door. 
"""
    poe_six = size_finder(poe, 6)
    print(poe_six)  # ['dreary', 'quaint', 'volume', 'nodded', 'nearly', 'gently']
    print(len(poe_six))  # should be 6


if __name__ == "__main__":
    main()
