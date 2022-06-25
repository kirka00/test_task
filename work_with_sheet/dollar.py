import requests
response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
currencies = []
if response.status_code == 200:
    content = response.json()
    data = [i for i in content['Valute']]
    for i in data:
        values = content['Valute'][i]
        CharCode = values['CharCode']
        Value = values['Value']
        if CharCode == 'USD':
            cur_doollar = Value
