#!/usr/bin/env python3

import tkinter as tk
from bowlingScore.gui import app

if __name__ == '__main__':
    # initialize tkinter window module
    root = tk.Tk()

    # start application
    app.MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
