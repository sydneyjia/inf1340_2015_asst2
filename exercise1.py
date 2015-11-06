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
    Take in word and returns pig latin translation of word
    :param : A string passed as an english word form the test cases
    :return: Pig latin translation of that word
    :raises: Error if an illegal input is passed
    """

    # check to make sure that word is both string and contains letter
    # characters
    if type(word) is str and word.isalpha():
        # define letter_counter loop to work through different letters
        letter_counter = 0
        # switch all letters to lowercase
        word = word.lower()
        #  review all vowels through making a list
        vowels = list("aeiouy")
        # loop through each letter
        for letter in word:
            first_letter = word[0]
            # if  first letter is a vowel, stop and return word plus yay
            if first_letter in vowels:
                return word + "yay"
            # if first letter is not a vowel, go through the remaining letters with letter_counter loop
            elif word[letter_counter] in vowels:
                # once arriving at a vowel, slice letters from before vowel to end of the word
                # add plus "ya" following the added consonant letters
                return word[letter_counter:] + word[:letter_counter] + "ay"
            # if the letter at position is not a vowel, add 1 to letter_counter and recheck
            letter_counter += 1
    else:
           return "Error! Please only enter characters between A-Z. Please enter a word:"

