#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from bowling_engine import bowling_module

class MainApplication(tk.Frame):
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
        self.scoreLabel = tk.Label(
            self.parent,
            textvariable=self.scoreText
        ).pack()
        self.frameCountLabel = tk.Label(
            self.parent,
            textvariable=self.frameCountText
        ).pack()
        self.entryLabel = tk.Label(
            self.parent,
            text='\nEnter bowling score'
        ).pack()

        self.entry = tk.Entry(self.parent)
        self.entry.pack()
        self.entry.focus_set()

        self.parent.bind("<Return>", self.getInput)
        
        self.button = tk.Button(
            self.parent, 
            text = "Submit", 
            width = 10, 
            command = self.getInput
        )
        self.button.pack()

        self.entryLabel = tk.Label(
            self.parent,
            textvariable=self.textMessage
        ).pack()

    def getInput(self, *args):
        input = self.entry.get()
        self.score, self.frameCount, self.textOutput = self.bs.inputScore(
            int(input)
        )
        self.setScore()
        self.setFrameCount()
        self.textMessage.set('\n' + self.textOutput)
    
    # combine score with description for text output
    def setScore(self, *args):
        self.scoreText.set('Total score: ' + str(self.score))

    # combine frame count with description for text output
    def setFrameCount(self, *args):
        self.frameCountText.set('Frame Count: ' + str(self.frameCount))

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
