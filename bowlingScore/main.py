#!/usr/bin/env python3

import random
import tkinter as tk
from gui import application

if __name__ == '__main__':
    # initialize tkinter window module
    root = tk.Tk()

    # start application
    application.MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
