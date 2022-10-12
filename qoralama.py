# import os
# import pyttsx3

# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# volume = engine.getProperty('volume')
# voices = engine.getProperty('voices') 
# engine.setProperty('rate', 125)
# engine.setProperty('volume',1.0)
# engine.setProperty('voice', voices[0].id)
# engine.say('Kechirasiz men uzbek tilida gapirolmayman')
# engine.runAndWait()
# engine.stop()
# # print('My current speaking rate is ' + str(rate) +str(voices) + str(volume))

import requests
import json

url = "https://play.ht/api/v1/convert"

payload = json.dumps({
  "voice": "uz-UZ-MadinaNeural",  #en-US-MichelleNeural  uz-UZ-SardorNeural
  "content": [
   "Hello My frinedsss",
   "either pass content s an array of strings , or ssml , but not both"
  ],
   "title": "Testing public api convertion"
})
headers = {
  'Authorization': '078c34a0cf7943dfbc75d7fee7c2f446',
  'X-User-ID': 'XNIhhevwbleOsSukPvvcAFYHgG22',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(json.dumps())
