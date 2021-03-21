#!/usr/bin/env python3

from backend import bowling_module
from logging import info, error, getLogger, debug
import logging
logging.basicConfig(level = logging.INFO)
import pytest

logger = getLogger(__name__)
bs_simple = bowling_module.BowlingScore()
bs_strike = bowling_module.BowlingScore()

class Test_single_scores:
    """ test output values depending on input
    """

    def test_simpleExample(self, *args):
        """ test basic example
        """

        bs_tmp = bowling_module.BowlingScore()
        score, frameCount, textOutput = bs_tmp.calculateScore(5)

        assert score == 5
        assert frameCount == 1
        assert textOutput == 'Normal score'

    def test_strike(self, *args):
        """ test strike
        """

        bs_tmp = bowling_module.BowlingScore()
        score, frameCount, textOutput = bs_tmp.calculateScore(10)

        assert score == 10
        assert frameCount == 2
        assert textOutput == 'Strike!'


class Test_spare:
    """ test spare event
    """

    def test_spare(self, *args):
        bs_tmp = bowling_module.BowlingScore()

        score, frameCount, textOutput = bs_tmp.calculateScore(1)
        assert score == 1
        assert frameCount == 1
        assert textOutput == 'Normal score'

        score, frameCount, textOutput = bs_tmp.calculateScore(9)
        assert score == 10
        assert frameCount == 2
        assert textOutput == 'Spare!'

class Test_error:
    """ test different error cases
    """

    def test_sum_error(self, *args):
        bs_tmp = bowling_module.BowlingScore()

        score, frameCount, textOutput = bs_tmp.calculateScore(5)
        assert score == 5
        assert frameCount == 1
        assert textOutput == 'Normal score'

        score, frameCount, textOutput = bs_tmp.calculateScore(6)
        assert score == 5
        assert frameCount == 1
        assert textOutput == 'Score to high! Try again!'
    
    def test_wrong_input(self, *args):
        bs_tmp = bowling_module.BowlingScore()
        score, frameCount, textOutput = bs_tmp.calculateScore(-1)

        assert frameCount == 1
        assert textOutput == 'Error, 1 < score < 10'
        assert score == 0
    
    def test_string_error(self, *args):
        bs_tmp = bowling_module.BowlingScore()

        # with pytest.raises(Exception):
        score, frameCount, textOutput = bs_tmp.calculateScore('foo')

        assert score == 0
        assert frameCount == 1

        # and continues healthy after wrong input
        score, frameCount, textOutput = bs_tmp.calculateScore(3)

        assert score == 3
        assert frameCount == 1

class Test_simple_full_example:
    """ run through a full game with no spares and no strikes
    """

    def test(self, *args):
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 1
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 2
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 3
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 4
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 5
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 6
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 7
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 8
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 9
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 10
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 11
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 12
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 13
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 14
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 15
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 16
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 17
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 18
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 19
        score, frameCount, textOutput = bs_simple.calculateScore(1)
        assert score == 20

class Test_example:
    """ test full example
    """

    def test(self, *args):
        score, frameCount, textOutput = bs_strike.calculateScore(1)
        assert score == 1
        score, frameCount, textOutput = bs_strike.calculateScore(4)
        assert score == 5

        score, frameCount, textOutput = bs_strike.calculateScore(4)
        assert score == 9
        score, frameCount, textOutput = bs_strike.calculateScore(5)
        assert score == 14

        # spare
        score, frameCount, textOutput = bs_strike.calculateScore(6)
        assert score == 20
        score, frameCount, textOutput = bs_strike.calculateScore(4)
        assert score == 24

        # spare
        score, frameCount, textOutput = bs_strike.calculateScore(5)
        assert score == 34
        score, frameCount, textOutput = bs_strike.calculateScore(5)
        assert score == 39

        # strike
        score, frameCount, textOutput = bs_strike.calculateScore(10)
        assert score == 59

        score, frameCount, textOutput = bs_strike.calculateScore(0)
        assert score == 59
        score, frameCount, textOutput = bs_strike.calculateScore(1)
        assert score == 61

        # spare
        score, frameCount, textOutput = bs_strike.calculateScore(7)
        assert score == 68
        score, frameCount, textOutput = bs_strike.calculateScore(3)
        assert score == 71

        # spare
        score, frameCount, textOutput = bs_strike.calculateScore(6)
        assert score == 83
        score, frameCount, textOutput = bs_strike.calculateScore(4)
        assert score == 87

        # strike
        score, frameCount, textOutput = bs_strike.calculateScore(10)
        assert score == 107

        # spare
        score, frameCount, textOutput = bs_strike.calculateScore(2)
        assert score == 111
        score, frameCount, textOutput = bs_strike.calculateScore(8)
        assert score == 127
        score, frameCount, textOutput = bs_strike.calculateScore(6)
        assert score == 133

        # finally make sure game ends
        assert textOutput == "Game over!"

        # make sure user cant proceed with further input
        score, frameCount, textOutput = bs_strike.calculateScore(6)
        assert score == 133
        assert textOutput == "Game over!"