# Fill in this file with the code from parsing JSON exercise
import json
dosya=open("myfile.json","r")
json_dosya=json.load(dosya)
print("API KEY:",json_dosya["ad"])
print("API KEY:",json_dosya["soyad"])
print("API KEY:",json_dosya["access_token"])
