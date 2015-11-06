#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

APPLICANT = [["Name", "Gender", "Age", "School"],
            ["Matt", "Male", 21, "Macmaster University"],
            ["Katie", "Female", 22, "University od Waterloo"],
            ["Clair", "Female", 24, "University of Toronto"],
            ["Stephen", "Male", 23, "University of Ottawa"]]

CANDIDATE = [["Name", "Gender", "Age", "School"],
           ["Ryan", "Male", 19, "SFU"],
           ["Michael", "Male", 22, "Queens University"],
           ["Katie", "Female", 22, "University od Waterloo"],
           ["Stephen", "Male", 23, "University of Ottawa"]]



#####################
# HELPER FUNCTIONS ##
#####################


def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)

###################
# TEST FUNCTIONS ##
###################


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    result_2 =[["Name", "Gender", "Age", "School"],
               ["Matt", "Male", 21, "Macmaster University"],
               ["Clair", "Female", 24, "University of Toronto"],
               ["Ryan", "Male", 19, "SFU"],
               ["Michael", "Male", 22, "Queens University"]]


    assert is_equal(result, difference(GRADUATES, MANAGERS))
    assert is_equal(result_2, difference(APPLICANT,CANDIDATE))

     try:
        assert difference(GRADUATES, APPLICANT)
    except MismatchedAttributesException:
        pass

def test_intersection():
    """
    Test intersection operation.
    """
    intersection_result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    graduates = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

    managers = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

    result_2 =[["Katie", "Female", 22, "University od Waterloo"],
               ["Stephen", "Male", 23, "University of Ottawa"]]

    assert is_equal(intersection_result, intersection(graduates, managers))
    assert is_equal(result_2, intersection(APPLICANT, CANDIDATE))

    try:
        assert intersection(GRADUATES, APPLICANT)
    except MismatchedAttributesException:
        pass



def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    result_2 =[["Name", "Gender", "Age", "School"],
            ["Matt", "Male", 21, "Macmaster University"],
            ["Katie", "Female", 22, "University od Waterloo"],
            ["Clair", "Female", 24, "University of Toronto"],
            ["Stephen", "Male", 23, "University of Ottawa"],
            ["Ryan", "Male", 19, "SFU"],
            ["Michael", "Male", 22, "Queens University"]]
]

    assert is_equal(result, union(GRADUATES, MANAGERS))
    assert is_equal(result_2,union(APPLICANT,CANDIDATE))

    # When schemas in lists do not match
    try:
        assert union(GRADUATES, APPLICANT)
    except MismatchedAttributesException:
        pass