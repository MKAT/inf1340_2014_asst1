#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string


    if isinstance(upc,str):
        print('Entered code is valid')
    else:
        raise TypeError('Entered code not of type string')

    if (len(upc) != 12):
        raise ValueError('UPC code does not contain 12 digits')
    else:
        digit1 = int(upc[0])
        digit2 = int(upc[1])
        digit3 = int(upc[2])
        digit4 = int(upc[3])
        digit5 = int(upc[4])
        digit6 = int(upc[5])
        digit7 = int(upc[6])
        digit8 = int(upc[7])
        digit9 = int(upc[8])
        digit10 = int(upc[9])
        digit11 = int(upc[10])
        digit12 = int(upc[11])
        odd_position = (digit1 + digit3 + digit5 + digit7 + digit9 + digit11) * 3
        even_position = (digit2 + digit4 + digit6 + digit8 + digit10) + odd_position

        result1 = even_position % 10
        if (result1 % 10) != 0:
            checksum = 10 - result1
        else:
            checksum = result1
        if checksum == digit12:
            return True
        else:
            return False


    # check length of string
    # raise ValueError if not 12

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # return True if they are equal, False otherwise



