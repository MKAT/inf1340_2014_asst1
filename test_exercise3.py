#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests
    with pytest.raises(TypeError):
        decide_rps(1.0,2.0)
    with pytest.raises(ValueError):
        decide_rps("Lion","Tiger")
        decide_rps("Deer","Rock")

