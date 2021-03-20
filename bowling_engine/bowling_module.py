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
        print(self.frames)
        self.textOutput = ""
        if self.ballCount == 1:
            self.scoreFirstBall(input)
        elif self.ballCount == 2:
            self.scoreSecondBall(input)
        elif (self.ballCount == 3):
            if (self.allowThirdBall) & (self.fc == 10):
                self.scoreThirdball()

        self.ballCount += 1
        return self.score, self.fc, self.textOutput

    def scoreFirstBall(self, input):
        if input == 10:
            self.frames[self.fc]['type'] = 'strike'
            self.textOutput = 'Strike!'

            if self.fc <= 9:
                self.fc += 1
                self.ballCount = 1
            else:
                self.allowThirdBall = 1

        else:
            self.frames[self.fc]['type'] = 'none'
    
        self.frames[self.fc][1] = input
        self.score += input

    def scoreSecondBall(self, input):
        ball1 = self.frames[self.fc][1]
        if ( ball1 + input ) >= 10:
            self.frames[self.fc]['type'] = 'spare'
            self.textOutput = 'Spare!'

            if self.fc <= 9:
                self.fc += 1
                self.ballCount = 1
            else:
                self.allowThirdBall = 1

        else:
            self.frames[self.fc]['type'] = 'none'
            self.fc += 1
            self.ballCount = 1
        
        self.frames[self.fc][2] = input
        self.score += input
        

    # Test function for module  
    def _test(self):
        assert throw_ball() >= 0
        assert throw_ball() <= 10

if __name__ == '__main__':
    BowlingScore._test()
