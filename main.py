import os
import tkinter as tk

import mainFrames as window
import settingFrames as setting

import const as const

#global
root = None
APIsettingWindow = None

def main():
     global root
     global APIsettingWindow

     root = tk.Tk()
     window.rootFrame(root)

     if not os.path.isfile(const.value.APIPath):
          setting.Frames.WindowAPISetting(APIsettingWindow)

     root.mainloop()

if __name__ == "__main__":
     main()
