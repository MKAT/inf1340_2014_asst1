#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """



    """
    :param mark:
    :return: :raise TypeError:
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        print ("letter")
        if grade in ['A+','A','A-','B+','B','B-','FZ']:
            print("valid input")
            if(grade == "FZ"):
                gpa= 0.0
            elif(grade == "B-"):
                gpa= 2.7
            elif(grade == "B-"):
                gpa= 2.7
            elif(grade == "B"):
                gpa = 3.0
            elif(grade == "B+"):
                gpa = 3.3
            elif(grade == "A-"):
                gpa = 3.7
            elif(grade == "A"):
                gpa = 4.0
            elif(grade == "A+"):
                gpa = 4.0
        else:
            raise ValueError("invalid range")

        # check that the grade is one of the accepted values
        # assign grade to letter_grade
    elif type(grade) is int:
        # check that grade is in the accepted range
        print("mark")
        if(0 <= grade <= 100):
            print("valid input")

            if(0 <= grade < 70):
                gpa = 0.0
            elif(70 <= grade < 73):
                gpa = 2.7
            elif(73 <= grade < 77):
                gpa = 3.0
            elif(77 <= grade < 80):
                gpa = 3.3
            elif(80 <= grade < 85):
                gpa = 3.7
            elif(85 <= grade <= 100):
                gpa = 4.0
        else:
            raise ValueError("invalid range")

        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # what I am working on -----if type(letter_grade)
    # assign the value to gpa
    if letter_grade == "A":
        gpa = 4.0

    return gpa
