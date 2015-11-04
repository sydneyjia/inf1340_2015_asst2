#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

def pig_latinify(word):
    """
    Convert English word input and convert into Pig Latin word.
    :param :
    :return: output_word
    :raises:
    """

    vowels = list("aeiouyAEIOUY")
    letter_counter = 0

    if word.isalpha() == False:
        print "Error! Please only enter characters between A-Z."
        return False

    if word[0] in vowels:
        print(word + 'yay')
        return True

    for letter in word:
        if letter in vowels:
            new_word = word[letter_counter:] + word[:letter_counter] + 'ay'
            print(new_word)
            return True

        letter_counter += 1


word_request = True
while word_request:
    input = raw_input("Please enter a word:\n")
    word_request = not pig_latinify(input)
