import tkinter as tk
import tkinter.ttk as ttk
import APIFunction as APIsetting

class Frames:

     def WindowAPISetting(APIsettingWindow):
          if APIsettingWindow == None or not APIsettingWindow.winfo_exists():
               APIsettingWindow = tk.Toplevel()
               APIsettingWindow.geometry("550x120")
               APIsettingWindow.title(u"API setting")
               APIsettingWindow.attributes("-topmost", True)

               APIKeyLabel = tk.Label(APIsettingWindow, text="DeepL APIキー：")
               APIKeyLabel.place(x=25,y=25)

               APIKeyTxtBox = tk.Entry(APIsettingWindow, width=50)
               APIKeyTxtBox.place(x=120,y=25)

               APIKeyButton = ttk.Button(APIsettingWindow, text="OK", command=lambda: APIsetting.function.register(APIsettingWindow))
               APIKeyButton.place(x=460,y=80)