#!/usr/bin/env python3

## This is the main file of a bowling game
#
# We call dependencies here and run the main task

import random
import tkinter as tk
from gui import application

if __name__ == '__main__':
    root = tk.Tk()
    application.MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
