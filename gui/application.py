#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from backend import bowling_module

class MainApplication(tk.Frame):
    """ Main tkinter class to create window.
    """

    def __init__(self, parent, *args):
        tk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self.frameCount = 1
        self.score = 0
        self.frameCountText = tk.StringVar()
        self.scoreText = tk.StringVar()
        self.textMessage = tk.StringVar()
        self.setScore()
        self.setFrameCount()
        self.bs = bowling_module.BowlingScore()

        self.parent.geometry("300x200")
        self.parent.title("Calculate bowling score")

        self.addWindowElements()


    def addWindowElements(self, *args):
        """ Loads all elements present in application window
        """

        # score
        self.scoreLabel = tk.Label(
            self.parent,
            textvariable=self.scoreText
        ).pack()

        # frame count
        self.frameCountLabel = tk.Label(
            self.parent,
            textvariable=self.frameCountText
        ).pack()

        # text above entry field
        self.entryLabel = tk.Label(
            self.parent,
            text='\nEnter bowling score'
        ).pack()

        # entry field
        self.entry = tk.Entry(self.parent)
        self.entry.pack()
        self.entry.focus_set()

        # allow submission via enter button
        self.parent.bind("<Return>", self.getInput)

        # send button        
        self.button = tk.Button(
            self.parent, 
            text = "Submit", 
            width = 10, 
            command = self.getInput
        )
        self.button.pack()

        # text below entry field; will display comments or error messages
        self.entryLabel = tk.Label(
            self.parent,
            textvariable=self.textMessage
        ).pack()


    def getInput(self, *args):
        """ Get input from Entry element. Value will be sanitized in the
            backend engine. 
        """

        # retrieve input string
        input = self.entry.get()

        # update values in backend engine module
        self.score, self.frameCount, self.textOutput = self.bs.calculateScore(
            input
        )

        # update values in window
        self.setScore()
        self.setFrameCount()
        self.textMessage.set('\n' + self.textOutput)
    

    def setScore(self, *args):
        """ combine score with description for text output
        """

        self.scoreText.set('Total score: ' + str(self.score))


    def setFrameCount(self, *args):
        """ combine frame count with description for text output
        """

        self.frameCountText.set('Frame Count: ' + str(self.frameCount))
