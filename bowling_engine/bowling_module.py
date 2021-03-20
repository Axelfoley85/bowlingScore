#!/usr/bin/env python3

class BowlingScore():
    def __init__(self):
        self.fc = 1     # frame count
        self.score = 0
        self.ballCount = 1
        self.frames = {}
        for i in range(1, 10):
            self.frames[i] = {}
        self.allowThirdBall = 0
    
    def inputScore(self, input):
        # print(self.frames)
        # print(self.fc)
        # print(self.frames[self.fc])
        self.textOutput = ""
        if self.ballCount == 1:
            self.scoreFirstBall(input)
        elif self.ballCount == 2:
            self.scoreSecondBall(input)
        elif (self.ballCount == 3):
            if (self.allowThirdBall) & (self.fc == 10):
                self.scoreThirdball()

        print(self.frames)
        print("frame count: ", self.fc)
        print("element of frame: ", self.frames[self.fc])
        print("ball count: ", self.ballCount)

        self.ballCount += 1
        return self.score, self.fc, self.textOutput

    def scoreFirstBall(self, input):
        print("=== Scoring first ball ===")
        if input == 10:
            self.frames[self.fc]['type'] = 'strike'
            self.textOutput = 'Strike!'
            self.frames[self.fc][1] = input

            if self.fc <= 9:
                self.fc += 1
                self.ballCount = 0
            else:
                self.allowThirdBall = 1

        else:
            self.frames[self.fc][1] = input
            self.frames[self.fc]['type'] = 'none'
            self.textOutput = 'Normal score'

        self.score += input

    def scoreSecondBall(self, input):
        print("==== Scoring second ball ===")
        ball1 = self.frames[self.fc][1]

        print(self.frames)
        print("frame count: ", self.fc)
        print("element of frame: ", self.frames[self.fc])
        print("ball count: ", self.ballCount)
        if ( ball1 + input ) >= 10:
            self.frames[self.fc]['type'] = 'spare'
            self.textOutput = 'Spare!'
            self.frames[self.fc][2] = input

            if self.fc <= 9:
                self.fc += 1
                self.ballCount = 0
            else:
                self.allowThirdBall = 1

        else:
            self.frames[self.fc]['type'] = 'none'
            self.frames[self.fc][2] = input
            self.fc += 1
            self.ballCount = 0
            self.textOutput = 'Normal score'
        
        self.score += input        

    # Test function for module  
    def _test(self):
        assert throw_ball() >= 0
        assert throw_ball() <= 10

if __name__ == '__main__':
    BowlingScore._test()
