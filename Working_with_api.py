import requests
import json
import pprint

baseUrl = "https://api.upcitemdb.com/prod/trial/lookup"

value = {'upc':'012993441012'}

response = requests.get(baseUrl,params=value)

print(response.url)

pp = pprint.PrettyPrinter(indent=2)

content = response.content
data = json.loads(content)

#pp.pprint(data)

item = data['items']

#pp.pprint(item)

itemInfo = item[0]

title = itemInfo['title']
print('Title:',title)

brand = itemInfo['brand']
print('Brand:',brand)

offer_price = itemInfo["offers"][0]["price"]
print('Offer price:',offer_price,end="$")
