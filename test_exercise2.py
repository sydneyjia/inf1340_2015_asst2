#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
     Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("Hello Toronto!", "may", 0, 20) == -1
    assert find("jshdushd", "hd", 30, 100) == -1
    assert find("45637902341", "902", 0, 200) == 5


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
    assert multi_find("How do you do","do", 0, 20) == "4,11"
    assert multi_find("456bfd8imbfd2", "fd", 0, 20) == "4,10"
    assert multi_find("Nice to meet you!", "o", 0, 20) == "6,14"
    assert multi_find("Nice to meet you!", "o", 20, 30) == ""
    assert multi_find("where are you going?", "457", 0, 30) == ""
