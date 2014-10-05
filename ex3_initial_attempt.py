__author__ = 'Melissa'
# write dictionary #!/usr/bin/env python3

# contencious debate of whether paper beats rock--covers, or rock beats paper--rock holds down paper


#cases where Player 1 wins--noted with a 1
#picks scissors against paper
#picks paper against rock
#picks rock against scissors

#cases where Player 2 wins--noted with a 2
#picks scissors against rock
#picks paper against rock
#picks rock against scissors

#combinations that produce a tie
# rock rock
#paper paper
#scissors Scissors
"""
player2_decisions = {  #wins
                       ("Paper", "Scissors"): 2,
                       ("Rock", "Paper"): 2,
                       ("Scissors", "Rock"): 2,
                       #losses
                       ("Scissors", "Paper"): 1,
                       ("Rock", "Scissors"): 1,
                       ("Paper", "Rock"): 1,
                       #ties
                       ("Scissors", "Scissors"): 0,
                       ("Rock", "Rock"): 0,
                       ("Paper", "Paper"): 0
                       }
"""

def decide_rps(player1, player2):

    if type(player1) is str:
        if player1 in ["Rock", "Paper", "Scissors"]:
            print("valid input")
        else:
            raise ValueError ("invalid input")

    if type(player2) is str:
        if player2 in ["Rock", "Paper", "Scissors"]:
            print("valid input")
        else:
             raise ValueError ("invalid input")

        if type(player1)(player2) is not str:
            return ("invalid input")


rps_dictionary = {  #wins for player 1 represented with a 1--also means a loss for player 2
                    ("Scissors", "Paper"): 1,
                    ("Rock", "Scissors"): 1,
                    ("Paper", "Rock"): 1,
                    #wins for player 2 represented with a 2--also means a loss for player 1
                    ("Paper", "Scissors"): 2,
                    ("Rock", "Paper"): 2,
                    ("Scissors", "Rock"): 2,
                    #ties
                    ("Scissors", "Scissors"): 0,
                    ("Rock", "Rock"): 0,
                    ("Paper", "Paper"): 0
                }

#Invalid responses

#line 60 Errors will occur if the input is not a string



"""
#define the function of determining who won
def decide_rps (player1, player2):
    return 1
print ("Scissors", "Rock")

player2_rps_decisions = { ()}
"paper, scisors": 2,

wins?

the win functions
decide_rps_dict = {p1: "scissor1" }
"""

