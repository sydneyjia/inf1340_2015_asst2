#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"
    return

def test_advanced():
    assert pig_latinify("Billy") == "illyBay"
    assert pig_latinify("Elly") == "Ellyay"
    assert pig_latinify("asdfghhjkloiytFFFv") == "asdfghhjkloiytFFFvyay"
    assert pig_latinify("phlegm") == "egmphlay"
    return

def test_errors():
    assert pig_latinify(1234) == "Error! Please only enter characters between A-Z. Please enter a word:"
    assert pig_latinify("Elly-May") == "Error! Please only enter characters between A-Z. Please enter a word:"
    assert pig_latinify("Winston Churchill") == "Error! Please only enter characters between A-Z. Please enter a word:"
    assert pig_latinify("Ke$ha") == "Error! Please only enter characters between A-Z. Please enter a word:"
    return




