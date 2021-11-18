import tkinter as tk
import const

#stub
class function:
     def register(APIsettingWindow, APIKey):
          try:
               with open(const.value.APIPath, mode='x') as f:
                    f.write(APIKey.get())

          except FileExistsError:
               with open(const.value.APIPath, mode='w') as f:
                    f.write(APIKey.get())

          APIsettingWindow.destroy()