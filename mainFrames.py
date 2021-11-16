import tkinter as tk
import settingFrames as setting

class rootFrame(tk.Frame):
     def __init__(self,master):
          super().__init__(master)
          self.pack(fill = tk.BOTH, padx=5, pady=10)

          master.geometry("1024x768")
          master.title(u"(Experiment by Akimoch) DeepL Translate Desktop version FreeAPI version")

          rootBeforeTransLabel = tk.Label(master, text="翻訳前")
          rootBeforeTransLabel.place(x=20,y=10)

          rootTxtBox = tk.Text(master, width=40, height=25)
          rootTxtBox.place(x=20,y=35)