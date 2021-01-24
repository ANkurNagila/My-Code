import json

data = '''
{
  "name" : "Ankur",
  "phone" : {
    "type" : "intl",
    "number" : "+91 9999999999"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
