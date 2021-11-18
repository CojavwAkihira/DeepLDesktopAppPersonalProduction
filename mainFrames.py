import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scroll
from main import APIsettingWindow
import settingFrames as setting
import const
import mainFramesFunc as func

class rootFrame(tk.Frame):
     def __init__(self, master):
          super().__init__(master)
          self.pack(fill = tk.BOTH, pady=5)
          master.resizable(width=False, height=False)

          beforeLang = tk.StringVar()
          afterLang = tk.StringVar()

          master.geometry(const.value.rootWindowSize)
          master.title(const.value.rootWindowTitle)

          self.createTopPain(beforeLang, afterLang)

          self.createCenterPain(beforeLang, afterLang)

          self.createAPIButton()

     def createTopPain(self, beforeLang, afterLang):
          topFrame = tk.Frame(self.master, padx=0, pady=0)
          
          rootBeforeTransLabel = tk.Label(topFrame, text=const.value.rootBeforeTransLabel)
          #rootBeforeTransLabel.place(x=20,y=10)

          rootBeforeTransLangSelBox = ttk.Combobox(topFrame, height=12, width=24, justify="left", textvariable=beforeLang, values=const.value.beforeLangSelList)
          rootBeforeTransLangSelBox.set(const.value.beforeLangSelList[0])
          #rootBeforeTransLangSelBox.place(x=110,y=10)

          rootAfterTransLabel = tk.Label(topFrame, text=const.value.rootAfterTransLabel)
          #rootAfterTransLabel.place(x=575,y=10)

          rootAfterTransLangSelBox = ttk.Combobox(topFrame, height=12, width=24, justify="left", textvariable=afterLang, values=const.value.afterLangSelList)
          rootAfterTransLangSelBox.set(const.value.beforeLangSelList[0])
          #rootAfterTransLangSelBox.place(x=665,y=10)

          rootBeforeTransLabel.pack(side=tk.LEFT, padx=(13,0), pady=0)
          rootBeforeTransLangSelBox.pack(side=tk.LEFT, padx=0, pady=0)

          rootAfterTransLangSelBox.pack(side=tk.RIGHT, padx=(0,195), pady=0)
          rootAfterTransLabel.pack(side=tk.RIGHT)

          topFrame.pack(fill=tk.X)

     def createCenterPain(self, beforeLang, afterLang):
          centerPain = tk.Frame(self.master, pady=10)
          rootBeforeTxtBox = scroll.ScrolledText(centerPain, width=59, height=52)
          #rootBeforeTxtBox.place(x=20,y=40)
          rootBeforeTxtBox.pack(side=tk.LEFT, padx=15, pady=0)

          translateButton = ttk.Button(centerPain, text=const.value.translateButtonLabel, command=lambda: print(func.mainFramesFunc.characterCountCheck()))
          #translateButton.place(x=465,y=320)
          translateButton.pack(side=tk.LEFT, padx=5, pady=0)

          rootAfterTxtBox = scroll.ScrolledText(centerPain, width=59, height=52)
          #rootAfterTxtBox.place(x=575,y=40)
          rootAfterTxtBox.pack(side=tk.RIGHT, padx=15, pady=0)

          centerPain.pack(fill=tk.X)

     def createAPIButton(self):
          APIKeyButtonFrame = tk.Frame(self.master, pady=0)
          APIKeyButton = ttk.Button(APIKeyButtonFrame, text=const.value.APIKeyButtonLabel, command=lambda: setting.Frames.WindowAPISetting(APIsettingWindow))
          #APIKeyButton.place(x=908,y=728)
          APIKeyButton.pack(side=tk.RIGHT, padx=13)

          APIKeyButtonFrame.pack(fill=tk.X)