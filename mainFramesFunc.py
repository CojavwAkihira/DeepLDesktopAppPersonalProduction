import requests
import json

import APIFunction

import const

class APIFunc:
     def FileLoad():
          print(APIFunction.function.loadAPIKey())
          return APIFunction.function.loadAPIKey()

     def characterCountCheck(APIKey):
          r = requests.post('https://api-free.deepl.com/v2/usage', data={'auth_key': APIKey})

          if r.status_code == 200:
               return r.json()['character_limit']
          else:
               print(r.status_code)
               return False

     def Translate(APIKey, beforeLang, beforeText, AfterLang):
          r = requests.post('https://api-free.deepl.com/v2/translate', data={'auth_key': APIKey, 'text': beforeText, 'source_lang':beforeLang, 'target_lang': AfterLang})

          if r.status_code == 200:
               print(r.json())
               return r.json()['translations'][0]['text']
          else:
               print(r.status_code)
               return False