import requests

import const as const

class function:

     APIKey = ""

     def loadAPIKey():
          try:
               with open(const.value.APIPath, mode='r') as f:
                    APIKey = f.read()

          except FileNotFoundError:
               return False

          if APIKey == "":
               return False
          else:
               return APIKey

     # API
     def apiCheck():
          global APIKey
          APIKey = function.loadAPIKey()
          r = function.characterCountCheck()
          if r.status_code == 200:
               return True
          else:
               return False

     def characterCountCheck():
          global APIKey
          r = requests.post('https://api-free.deepl.com/v2/usage', data={'auth_key': APIKey})
          print(r.json())
          return r

     def Translate():
          pass