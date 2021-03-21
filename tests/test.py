#!/usr/bin/env python3

from backend import bowling_module
import pytest

bs_simple_example = bowling_module.BowlingScore()
bs_specific_example = bowling_module.BowlingScore()

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

class Test_simple_example:
    """ run through a full game with no spares and no strikes
    """

    @pytest.mark.parametrize("expectedScore", range(1, 21))
    def test_simple_example(self, expectedScore):
        score, frameCount, textOutput = bs_simple_example.calculateScore(1)
        assert score == expectedScore

class Test_specific_example:
    """ test full example
    """

    @pytest.mark.parametrize(
        "input, expectedScore",
        [
            (1, 1),
            (4, 5),
            (4, 9),
            (5, 14),
            (6, 20),
            (4, 24),
            (5, 34),
            (5, 39),
            (10, 59),
            (0, 59),
            (1, 61),
            (7, 68),
            (3, 71),
            (6, 83),
            (4, 87),
            (10, 107),
            (2, 111),
            (8, 127),
            (6, 133),
        ]
    )
    def test_specific_example(self, input, expectedScore):
        score, frameCount, textOutput = bs_specific_example.calculateScore(input)
        assert score == expectedScore

    def test_makeSureGameEnds(self, *args):
        # make sure user cant proceed with further input
        score, frameCount, textOutput = bs_specific_example.calculateScore(6)
        assert score == 133
        assert textOutput == "Game over!"
