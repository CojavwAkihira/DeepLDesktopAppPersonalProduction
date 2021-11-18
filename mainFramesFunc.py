import requests
import os

import const

class mainFramesFunc:
     def characterCountCheck():
          with open(const.value.APIPath, mode='r') as f:
               r = requests.post('https://api-free.deepl.com/v2/usage', data={'auth_key': f.read()})
          print(r.status_code)
          print(r.text)
          return r