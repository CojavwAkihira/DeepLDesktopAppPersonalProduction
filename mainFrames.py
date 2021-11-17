import tkinter as tk
import tkinter.ttk as ttk
from main import APIsettingWindow
import settingFrames as setting
import const

class rootFrame(tk.Frame):
     def __init__(self,master):
          super().__init__(master)
          self.pack(fill = tk.BOTH, padx=10, pady=10)

          beforeLang = tk.StringVar()
          afterLang = tk.StringVar()

          master.geometry(const.value.rootWindowSize)
          master.title(const.value.rootWindowTitle)

          # Left pain
          rootBeforeTransLabel = tk.Label(master, text=const.value.rootBeforeTransLabel)
          rootBeforeTransLabel.place(x=20,y=10)

          rootBeforeTransLangSelBox = ttk.Combobox(master, height=12, width=12, justify="left", textvariable=beforeLang, values=const.value.beforeLangSelList)
          rootBeforeTransLangSelBox.set(const.value.beforeLangSelList[0])
          rootBeforeTransLangSelBox.place(x=110,y=10)

          rootBeforeTxtBox = tk.Text(master, width=60, height=52)
          rootBeforeTxtBox.place(x=20,y=35)

          # Center pain
          translateButton = ttk.Button(master, text=const.value.translateButtonLabel, command=lambda: print(beforeLang.get() +" "+ afterLang.get()))
          translateButton.place(x=466,y=320)

          # Right pain
          rootAfterTransLabel = tk.Label(master, text=const.value.rootAfterTransLabel)
          rootAfterTransLabel.place(x=575,y=10)

          rootAfterTransLangSelBox = ttk.Combobox(master, height=12, width=14, justify="left", textvariable=afterLang, values=const.value.afterLangSelList)
          rootAfterTransLangSelBox.set(const.value.beforeLangSelList[0])
          rootAfterTransLangSelBox.place(x=665,y=10)

          rootAfterTxtBox = tk.Text(master, width=60, height=52)
          rootAfterTxtBox.place(x=575,y=35)

          APIKeyButton = ttk.Button(master, text=const.value.APIKeyButtonLabel, command=lambda: setting.Frames.WindowAPISetting(APIsettingWindow))
          APIKeyButton.place(x=908,y=728)