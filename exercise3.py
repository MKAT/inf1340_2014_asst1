#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock,Paper, Scissors

This module contains one function decide_rps. It takes inputs from two players:player1 and player2 as its parameters.
The input must be "Rock" , "Paper" or "Scissors" . It returns the result of the game.

Example:
    $ python exercise3.py

"""

__author__ = 'Melissa Tomko & Vidhya Arulnathan'
__email__ = "melissa.tomko@mail.utoronto.ca/vidhya.arulnathan@mail.utoronto.ca"

__copyright__ = "2014 Melissa & Vidhya "

__status__ = "Prototype"

# imports one per line




def decide_rps(player1, player2):

    """
    Returns the result of a 'Rock, Paper, Scissors' game

    :param
        player1(string): accepted values are "Rock" , "Paper" , "Scissors"
        player2(string): accepted values are "Rock" , "Paper" , "Scissors"
    :return:
        integer: 1 , if player1 wins
                2, if player2 wins
                0, if it is a tie
    :raises:
        TypeError if parameter is not a string
        ValueError if parameter is out of range
    """
    if isinstance(player1, str):
        print('Entered input is valid')
    else:
        raise TypeError('Entered input not of type string')
    if isinstance(player2, str):
        print('Entered input is valid')
    else:
        raise TypeError('Entered input not of type string')

    if player1 in ["Rock", "Paper", "Scissors"]:
        print("Input is within range")
    else:
        raise ValueError("Entered input not within range")
    if player2 in ["Rock", "Paper", "Scissors"]:
        print("Input is within range")
    else:
        raise ValueError("Entered input not within range")


    rps_dict = {}
    rps_dict[("Paper","Rock")] = 1
    rps_dict[("Rock","Paper")] = 2
    rps_dict[("Scissors","Paper")] = 1
    rps_dict[("Paper","Scissors")] = 2
    rps_dict[("Rock","Scissors")] = 1
    rps_dict[("Scissors","Rock")] = 2
    rps_dict[("Rock","Rock")] = 0
    rps_dict[("Paper","Paper")] = 0
    rps_dict[("Scissors","Scissors")] = 0

    input_result = (player1,player2)

    for key in rps_dict:
        if key == input_result:
            game_result = rps_dict[key]
            return game_result







