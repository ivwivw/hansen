# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import logging
from typing import List


# used Python 3.8 on Mac Mini with Pycharm evaluation edition.
# read multiple strings from user
# the first pattern 'STTTS'
# the second any length N (N >=1) at least one separated by a comma 1 4 8
# first = input('Please give your input. (consisting of the letters s and t as you like) ' / n)
# second = input('Please give your second input (consisting of numbers separated by a space.: ' / n)

# My notes.
# Hard task for me :-(
# Reason daily working languages C# (compiled language) and javascript (ecma 8).
# Had used 'simple' python code before like in Anaconda and jupiter notebooks,
# Used the line by line evaluations and that a couple years back.


# --- So I had to learn. ---
# learned from youtube (Socratia) and some Python sites and of course stackoverflow.
# the hardest was writing the unittests long time ago I did this.

# The formatting pattern was also not easy for me.
# good think I downloaded Pycharm and not try to do this in Visual studio code.
# finally unit testing starting to bubble.
# The task was hard but very useful and also fun.


def valid_number_of_args(arg_count):
    return arg_count > 2


def validate_number_args(numbers):
    # the arguments
    # skip 0 is self => main.py
    # and skip the second argument as it is the letters pattern
    try:
        for x in numbers:
            y = int(x)
    except ValueError:
        print('Expecting only numbers in the second and thereafter arguments.')
        raise
        exit()


def parse_number_args(input_numbers):
    # the arguments
    # skip 0 is self => main.py
    # and skip the second argument as it is the letters pattern
    pattern: List[int] = []
    for x in input_numbers:
        y = int(x)
        pattern.append(y)
    return pattern


def parse_letters_args(letters):
    # the arguments
    # skip 0 is self => main.py
    # and skip the second argument as it is the letters pattern
    pattern = []

    for x in letters:
        y = str(x)
        pattern.append(y)

    return pattern


def letters_are_valid(letters):
    flag = True

    valid_letter = ['S', 'T']
    for letter in letters:
        if letter not in valid_letter:
            flag = False

    return flag


def end_part(letter1, letter2):
    part: str = ''
    if letter1 == "S":
        part += "Soft"
    if letter1 == "T":
        part += 'Tough'
    if letter2 == "S":
        part += " and Soft."
    if letter2 == "T":
        part += " and Tough."
    return part


def start_part(line_number, st_values, numbers):
    number = numbers[line_number]
    output = ''
    st_values_count = len(st_values)
    # st values elements 1 and 2 are reversed for the end part.
    if number > 2:
        for x in range(number):
            if x < st_values_count:
                if st_values[x] == 'S':
                    output += "Soft, "
                if st_values[x] == 'T':
                    output += "Tough, "
    return output


if __name__ == '__main__':
    """This is the a solution to a programming task put out by Hansencx"""
    # check arguments before starting processing not waisting resources.

    logging.basicConfig(
        level=logging.INFO,
        filename='info.log',
    )

    logging.info("Starting program.")

    args_count = len(sys.argv)
    if not valid_number_of_args(args_count):
        print("Missing at least one argument. Example arguments STS 5 2")
        exit()
    logging.info("Validated number of arguments.")
    letters_arg = str(sys.argv[1])

    if not letters_are_valid(letters_arg):
        print('Letters argument can only have S or T')
        exit()
    logging.info("Validated letters from arguments.")
    numbers_arg = sys.argv[2:]
    # validate all the numbers args checking for letters.
    validate_number_args(numbers_arg)
    logging.info("Validated numbers from arguments.")
    st_pattern = parse_letters_args(letters_arg)
    logging.info("Parsed the STS pattern from first argument.")
    numbers_pattern = parse_number_args(numbers_arg)
    logging.info("Parsed the numbers from the argument(s).")
    # create the end part
    # if there is only one number argument.
    # else we take first and second
    if len(st_pattern) == 1:
        end = end_part(st_pattern[0], st_pattern[0])
    else:
        end = end_part(st_pattern[0], st_pattern[1])
    logging.info("Created the end part.")

    logging.info("Creating the lines for each number.")
    # start building the output
    # g et the SST pattern count
    # the lines we need
    lines = len(numbers_pattern)

    for line in range(lines):
        start = ''
        start = start_part(line, st_pattern, numbers_pattern)

        # print the line
        print(start + end)

    logging.info("All done.")
