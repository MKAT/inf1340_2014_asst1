#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():


    Inputs that are the correct format and length

    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests
    with pytest.raises(TypeError):
        decide_rps(1.0,2.0)
    with pytest.raises(ValueError):
        decide_rps("Lion","Tiger")
        decide_rps("Deer","Rock")

    """
    #Player 1 Win Scenarios

    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Scissors", "Paper") == 1

    #Player 2 Wins Scenarios
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Rock") == 2

    #Other Scenarios are a Tie
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Paper", "Paper") == 0
    """
