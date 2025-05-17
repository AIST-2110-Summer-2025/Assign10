# `size_finder()` Function

This is a simple "reduce" function that returns a list of all words in a sentence
that have a specified size.

The function must ignore punctuation and place all words from the paragraph
provided as an argument. However, this part is already done for you. You will
have access to a list of `all_words` that contains, well, all of the words in
the paragraph.

What you DO need to do is the following:

  1.  Validate the arguments by raising a ValueError if:
        - paragraph is not an instance of str
        - size is not an instance of int
        - size is not between 1 and 19, inclusive (i.e., > 0 and < 20)
  2.  Create a new empty list of words
  3.  Iterate over all of the words in `all_words` and if the length of a word
      is equal to the `size` parameter, add it to the new list.
  4.  Return the new list of words.

> IMPORTANT: steps 2-4 can be done in a single line using a list comprehension.
> You must *__NOT__* do this. Again, please don't use tools that we haven't
> learned, at least without ALSO doing it the way we learned it using for/in and
> .append().

Test your function by running the script and comparing the values you are
returning with the expected values as indicated in the examples in the `main()`
function.