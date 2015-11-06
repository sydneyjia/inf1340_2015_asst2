#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string,substring,start,end):
    """
    Describe your function: This function aims to find a certain substring from the whole string.
                            If the substring is found,the sequence number will be provided;
                            If the substring is not found within the string, -1 will be raised.

    :param :input_string and substring are strings; start and end are integer numbers
    :return:i(index)
    :raises:-1(when no matching substring is found)

    """

    input_string_length = len(input_string)     # Count the length of the input string and assign it to a new variable
    target_length = len(substring)

    if target_length > input_string_length:     # Test the validity of the input strings and integers
        return -1
    if start > input_string_length:
        return -1
    if start >=end:
        return -1

    # Slice the complete string with equal intervals(the length of the substring) and use for loop to run through the whole string
    for i in range(start,end):
        if(input_string[i:i+target_length]==substring):
            return i                                       # If the substring is found, return the value of i to the function
    else:
        return -1                                          # If the substring is not found, raise -1



def multi_find(input_string, substring, start, end):
    """
    Describe your function: This function displayed each occurrence of a certain substring by the sequence number

    :param :input_string and substring are strings; start and end are integer numbers
    :return:k(a list of number indicating each occurrence of the substring)
    :raises:""(when no matching substring is found)

    """
    input_string_length = len(input_string)
    target_length = len(substring)

    if target_length > input_string_length:
        return ""
    if start > input_string_length:
        return ""

    i =start
    k =""
    for i in range(start,end-target_length+1):                  #Add for loop to walk through all slices of the string
        if input_string[i:i+target_length]==substring:
            k=k+str(i)+","                                      #Stire the serial number of all matching substring occurred in the input string.
            i+=1
    j=len(k)
    k =k[:j-1]                                                  #Delete the extra comma at the end of the string
    return k

#find()
#multi_find()


