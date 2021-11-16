import os
import tkinter as tk

import mainFrames as window
import settingFrames as setting

#global
root = None
APIsettingWindow = None

def main():
     global root

     root = tk.Tk()
     window.rootFrame(root)

     if not os.path.isfile("./api.ini"):
          setting.Frames.WindowAPISetting(APIsettingWindow)

     root.mainloop()

if __name__ == "__main__":
     main()
