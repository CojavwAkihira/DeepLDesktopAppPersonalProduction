import tkinter as tk
import tkinter.ttk as ttk

import settingFramesFunc as func

class Frames:

     def WindowAPISetting(APIsettingWindow):
          # bug: ウィンドウが複数表示可能
          if APIsettingWindow == None or not APIsettingWindow.winfo_exists():
               APIsettingWindow = tk.Toplevel()
               APIsettingWindow.geometry("550x120")
               APIsettingWindow.title(u"API setting")
               APIsettingWindow.attributes("-topmost", True)

               APIKey = tk.StringVar()

               APIKeyLabel = tk.Label(APIsettingWindow, text="DeepL APIキー：")
               APIKeyLabel.place(x=25,y=25)

               APIKeyTxtBox = tk.Entry(APIsettingWindow, width=50, textvariable=APIKey)
               APIKeyTxtBox.place(x=120,y=25)

               APIKeyButton = ttk.Button(APIsettingWindow, text="OK", command=lambda: func.function.register(APIsettingWindow, APIKey))
               APIKeyButton.place(x=460,y=80)
          else:
               pass