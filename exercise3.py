#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

def union(table1, table2):
    """
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    # create new list in order to store new information for union table
    union_list = []
    #compare two tables and check if columns and schema are equal
    if table1[0] == table2[0]:
        union_list = table1
        for item in table2:
            if not item in union_list:
                union_list.append(item)

    else:
        raise MismatchedAttributesException

  #  union_list = remove_duplicates(union_list)
    return union_list #return new list with unique rows that appear in either table
print union(GRADUATES, MANAGERS)


def intersection(table1, table2):
    """
    Describe your function

    """
    # create new list in order to store new information for intersection table
    intersection_list = []
    # compare two tables and check if columns and schema are equal
    if table1[0] == table2[0]:
        for item in table1:
            if item in table2:
                intersection_list.append(item)

    else:
        raise MismatchedAttributesException

   # intersection_list = remove_duplicates(intersection_list)
    return intersection_list
print intersection(GRADUATES, MANAGERS)


def difference(table1, table2):
    """
    Describe your function

    """
    # create new list in order to store new information for difference table
    difference_list = []
    # compare two tables and check if columns and schema are equal
    if table1[0] == table2[0]:
        for item in table1:
            if item not in table2:
                difference_list.append(item)

    else:
        raise MismatchedAttributesException

 #   difference_list = remove_duplicates(difference_list)
    return difference_list #return new list with rows from first table but not second
print difference(GRADUATES, MANAGERS)


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

