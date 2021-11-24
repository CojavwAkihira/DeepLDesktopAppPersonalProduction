import requests

import const as const
import APIFunction as func

class function:

     # File
     def register(APIsettingWindow, APIKey):
          if APIKey.get() != "":
               try:
                    with open(const.value.APIPath, mode='x') as f:
                         f.write(APIKey.get())

               except FileExistsError:
                    with open(const.value.APIPath, mode='w') as f:
                         f.write(APIKey.get())

               if APIKey.get() != "":
                    func.APIKey = APIKey.get()
                    result = func.function.apiCheck()

                    if result:
                         APIsettingWindow.destroy()
                    else:
                         # Error Handling
                         print("apiCheck was failed")
               else:
                    #Error Handling
                    print("APIKey is null")
          else:
               #Error Handling
               print("APIKey is null")
