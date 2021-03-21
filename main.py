#!/usr/bin/env python3

import random
import tkinter as tk
from gui import application

if __name__ == '__main__':
    root = tk.Tk()
    application.MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
