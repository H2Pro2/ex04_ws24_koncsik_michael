# Author: Koncsik Michael

# YOUR TASK'S: IMPLEMENT THE FOLLOWING FUNCTIONS

def remove_non_alpha(string: str) -> str:
    """ (1 point)
    this function will remove all non-alphanumeric
    character from a string and returns the 'cleaned'
    string.
    e.g.: 'a1bc4d' -> 'abcd'
          'A$tra.' -> 'Atra'
          '3.12'   -> ''

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use list comprehension or ternary operator!
    """
    # TODO

    non_alpha_removed = ""
    for char in string:
        if char.isalpha():
            non_alpha_removed += char
    return non_alpha_removed


def extract_words(lyrics: str) -> list[str]:
    """ (1 points)
    in this function, a string will be transformed
    into a list, where each 'word' of the string is
    part of. the definition of a 'word' will be:
    - only alphanumeric characters (a-z, A-Z, äöüß)
      - HINT: the remove_non_alpha function may help
    - a whitespace character (space, newline, ...)
      separates words from each other
    - an empty string is not a valid word
    - the strings returned are all in lowercase
    e.g.: 'Hello, W0rld!' -> ['hello', 'wrld']
          '12.3 * 3' -> []
          '' -> []

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use list comprehension or ternary operator!
    """
    # TODO
    return []


def uniq(strings: list[str]) -> list[str]:
    """ (1 point)
    this function will return a list with
    all UNIQ strings of the incoming list.
    The original list will not be modified!
    e.g.: ['a', 'b', 'a', 'c'] -> ['a', 'b', 'c']

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use list comprehension or ternary operator!
    """
    # TODO
    return []


def lengths(strings: list[str]) -> list[int]:
    """ (1 point)
    this function will return a list of the lengths
    of the given list of strings. The incoming list
    will NOT be modified!
    e.g.: ['a', 'bc', 'def'] -> [1, 2, 3]
          ['', 'hello', 'world'] -> [5, 5] : empty strings will NOT be counted!
          [] -> []

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use list comprehension or ternary operator!
    """
    # TODO
    return []


def min(numbers: list[int]) -> int:
    """ (1 point)
    this function will return the smallest POSITIVE number
    of a list of numbers. when the list is empty of only
    contains negative numbers, it returns 0
    e.g.: [3, 1, 2] -> 1
          [-1, 1] -> 1
          [] -> 0

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use the build-in 'min' or 'max' functions!
    Do NOT use list comprehension or ternary conditions!
    """
    # TODO
    return 0


def max(numbers: list[int]) -> int:
    """ (1 point)
    this function will return the largest POSITIVE number
    of a list of numbers. when the list is empty of only
    contains negative numbers, it returns 0
    e.g.: [3, 1, 2] -> 3
          [-1, 1] -> 1
          [] -> 0

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use the build-in 'min' or 'max' functions!
    Do NOT use list comprehension or ternary conditions!
    """
    # TODO
    return 0


def counts(numbers: list[int]) -> list[int]:
    """ (1 point)
    this function returns a NEW list with the
    counts of every number between the SMALLEST
    and LARGEST number of the given list. The
    incoming list will NOT be modified!
    e.g.: [1, 2, 4, 1, 4] -> [2, 1, 0, 2]
          [2, 2, 2] -> [3]
          [3, 5, 3, 5, 5] -> [2, 0, 3]

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use the build-in 'min' or 'max' functions!
    Do NOT use list comprehension or ternary conditions!
    """
    # TODO
    return []


def score(lyrics: str) -> float:
    """ (3 points)
    calculate the score of lyrics

    this fictional score will be calculated
    through the following aspects:

    - The sum of the length of all words  (SAW)
    - The sum of the length of all uniq words  (SUW)
    - The sum of the count of the length of all words  (SCAW)
    - The sum of the count of the length of all uniq words (SCUW)

    The formula for the score is:
    (SCAW - SCUW) / (SAW - SUW + 1)

    Use the functions that are available in this file
    to get the values you need to calculate the score.
    Try to not repeat/copy code from other functions,
    in the best case, all you need are the available
    functions and some variables, as well as a simple
    arithmetic calculation at the end.
    To build a sum of a list of numbers, feel free to
    use the 'sum'-function from python, or create your
    own function to do that.

    Do NOT use list comprehension or ternary conditions,
    or any functions that you have to be imported
    """
    # TODO
    return 0.0


# END OF YOUR TASK'S
