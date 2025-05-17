# `get_valid_input()` Function

This function is similar to a number of prior assignments in that you are
effectively creating a "special" version of the `input()` function. This one
will validate that the user has entered a value that is one of a specified
number of valid options before returning the user's choice.

The basic logic is simple (get input, if input in valid_vals return input,
otherwise try again). But because this must be case insensitive BOTH for the
user input and for the list of valid values, there's a little bit of extra
effort required.

Specifically, you must use the "map" pattern to create a copy of the
`valid_vals` list that contains lower-case versions of each of the valid values.
In other words, if the valid vals are:
```
["John", "Paul", "George", "Ringo"]
```
then you must create a copy that contains:
```
["john", "paul", "george", "ringo"]
```

> IMPORTANT: You must *__NOT__* use a list comprehension for this. Use the tools
> that we know, i.e. a for/in loop and the `.append()` method. If you use a list
> comprehension it will indicate that you used AI (or didn't read the
> instructions) and thus you will get no credit for this exercise. If you want
> to show off your Python chops, feel free to type in and then comment out a
> list comprehension. ;)

The pseudo-code logic for this function is as follows:
```
create new list
iterate over valid_vals:
    append the lowercase version of each value to the new list

loop forever:
    get user input using the prompt parameter
    strip and lowercase the user input
    if user input is in the lowercase list of valid vals:
        return the user input
    otherwise:
        print "INVALID INPUT"
```
The value returned should be all lowercase and stripped of any leading or
trailing whitespace characters.

Run the script from the command line to test it out with the Beatles and color
choices provided in the `main()` function. Then run the unit tests to insure
that you have passed all of the "edge" cases and are ready to submit.
