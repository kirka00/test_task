import requests
import xmltodict
import json
'''res = requests.get('http://stripmag.ru/datafeed/p5s_full_stock.xml')
print(res.text)'''


data = requests.get('http://stripmag.ru/datafeed/p5s_full_stock.xml')
xpars = xmltodict.parse(data.text)

with open('data.json', 'w') as outfile:
    json.dump(xpars, outfile)
