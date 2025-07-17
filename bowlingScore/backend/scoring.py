#!/usr/bin/env python3

from logging import info, error, getLogger, debug
import logging
import sys
from numpy.core.defchararray import isnumeric
logging.basicConfig(level = logging.INFO)

logger = getLogger(__name__)


class BowlingScore():
    """ Object that holds bowling score and calculates score update with new
        input.
    """

    def __init__(self):
        self.fc = 1     # frame count
        self.score = 0
        self.ballCount = 1

        # keeps track of individual score values, only for debugging
        self.frames = {}
        self.bonus = []
        self.gameOver = 0
        for i in range(1, 11):
            self.frames[i] = {}
        self.allowThirdBall = 0


    def calculateScore(self, input):
        """ Checks for sane input value and delegates
            score calculations depending on frame and ball count
            to regarding functions

            parameters:
            1. input (int): input value of single bowling shot 

            returns:
            1. score (int): udpated score value
            2. fc (int): frame counter
            3. textOutput (string): text or message that will show up in 
                window application
        """

        # don't change any values if the game is over
        if (self.gameOver):
            return self.score, self.fc, self.textOutput


        # Make sure the application does not get interrupted in falty input
        # values.
        try:
            if (int(input) < 0) or (int(input) > 10):
                error('Error, 1 < input < 10')
                self.textOutput = 'Error, 1 < score < 10'

                return self.score, self.fc, self.textOutput
        except:
            error('Something went wrong!')
            self.textOutput = 'Something went wrong'

            return self.score, self.fc, self.textOutput
        
        # do the actual calculations in this function
        self.distinguishFrameCase(input)
        
        # if any functions attempts to initiate frame 11 close the game and
        # reset frame counter
        if (self.fc >= 11):
            self.gameOver = 1
            self.textOutput = 'Game over!'
            self.fc = 10

        return self.score, self.fc, self.textOutput


    def distinguishFrameCase(self, input):
        """ This function decides depending on ball and frame counter and 
            which calculations needs to happen
        """

        input = int(input)
        noErrors = 1

        self.calculateBonus(input)

        self.textOutput = ""                # reset text for gui
        if self.ballCount == 1:
            self.scoreFirstBall(input)

        elif self.ballCount == 2:
            noErrors = self.scoreSecondBall(input)

        elif (self.ballCount == 3):
            if (self.allowThirdBall) & (self.fc == 10):
                self.scoreThirdball(input)

        print(self.frames)

        if (noErrors):
            self.ballCount += 1


    def scoreStrike(self, input):
        self.frames[self.fc]['type'] = 'strike'
        self.textOutput = 'Strike!'
        self.frames[self.fc][1] = input


    def scoreFirstBall(self, input):
        print("=== Scoring first ball ===")

        # strike?
        if input == 10:
            self.scoreStrike(input)

            if self.fc <= 9:
                self.fc += 1
                self.ballCount = 0
                self.bonus.append('nextTwo')

            # activate bonus ball on strike in frame ten
            else:
                self.allowThirdBall = 1

        # default case
        else:
            self.frames[self.fc][1] = input
            self.frames[self.fc]['type'] = 'none'
            self.textOutput = 'Normal score'

        self.score += input


    def scoreSecondBall(self, input):
        print("=== Scoring second ball ===")
        ball1 = self.frames[self.fc][1]

        # combined score too high?
        if (( ball1 + input ) > 10) & (self.fc <= 9):
            error('Score to high!')
            self.textOutput = 'Score to high! Try again!'
            return 0

        else:

            # is this a spare?
            if ( ball1 + input ) == 10:
                self.frames[self.fc]['type'] = 'spare'
                self.textOutput = 'Spare!'
                self.frames[self.fc][2] = input

                if self.fc <= 9:
                    self.fc += 1
                    self.ballCount = 0
                    self.bonus.append('nextOne')

                # activate the bonus ball in frame ten, when scoring a spare
                else:
                    self.allowThirdBall = 1
            
            # special case: two strikes in a row in 10th frame
            elif (self.fc == 10) & (input == 10):
                self.scoreStrike(input)

            # default case
            else:
                self.frames[self.fc]['type'] = 'none'
                self.frames[self.fc][2] = input
                self.fc += 1
                self.ballCount = 0
                self.textOutput = 'Normal score'
            
            self.score += input

            return 1


    def scoreThirdball(self, input):
        """ This is the bonus ball we get on spare or strike in the tenth
            frame
        """

        print("=== Scoring third ball ===")
        self.frames[self.fc][3] = input
        self.fc += 1
        self.ballCount = 0
        self.score += input


    def calculateBonus(self, input):
        # case: two consecutive strikes
        if len(self.bonus) == 2:
            self.score += 2 * input
            self.bonus = ['nextOne']

        # case: strike or spare in past frame
        elif len(self.bonus) == 1:
            self.score += input
            if self.bonus[0] == 'nextOne':
                self.bonus = []
            elif self.bonus[0] == 'nextTwo':
                self.bonus = ['nextOne']
            else:
                sys.exit("Unknown value in bonus array", self.bonus[0])

        # make sure we wont miss unknown/unintended cases
        elif len(self.bonus) > 2:
            sys.exit("Unknown use case on bonus array", self.bonus)
