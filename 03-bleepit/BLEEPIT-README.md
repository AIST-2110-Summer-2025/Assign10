# `bleepit()` Function

This is a fun little function that will print some text, but before printing it
will replace any "private" words with asterisks. It also returns the count of
words that were bleeped.

You do not need to do any argument validation for this one. In fact you can
assume that:
  - `text` is a string of space-separated words that contain no punctuation
    * though there may be a mix of upper- and lower-case words in the text
  - `bleeps` is a list of strings
  - all strings in `bleeps` are lowercase

This can actually be done using a fancy "map" pattern. The pseudo-code logic
will be something like the following:
```
split `text` into a list of words (`all_words`)
create an empty list to hold potentially bleeped words (`new_words`)
create a bleep counter

for every word in all_words:
    if the lowercase version of the word is in `bleeps`:
        append asterisks to `new_words`
        increment the bleep counter
    otherwise:
        append the unaltered word to `new_words`

join and print the words in `new_words` separated by a space
return the value of the bleep counter
```

When adding asterisks (*) to the list of new_words, you want to have one * per
letter in the word. This is quite simple using the multiplication operator.

Recall that any string "multiplied" by an integer (y) simply creates a new
string that contains y copies of the original string. So:
```
'*' * 5
```
will result in five asterisks (`*****`). And if you substitute the length of the
word in place of `5` you will end up with the desired number of asterisks.

There are a few examples to work from in the `main()` function, but generally
you should expect it to work as follows:

If you call
```
bleepit("The quick brown fox", ["brown"])
```
you will print:
```
The quick ***** fox
```
and return 1 since you only had to "bleep" on word.

Likewise:
```
bleepit("Beautiful people eat beautiful pastries by the sea", ["beautiful", "sea"])
```
should print:
```
********* people eat ********* pastries by the ***
```
and return 3.

> NOTE: `bleepit_challenge.py` is just that. A challenging version that is 100%
> optional. But if you're finding these a bit too easy, then this version should
> prove a bit more difficult. You'll definitely be using some slicing to make
> this work. No extra credit...just extra fun.