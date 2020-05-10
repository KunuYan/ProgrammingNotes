import requests


url = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=46201")

#print(url) - return a json object, but we have to tell python that it is a json
#-> <Response [200]> -wich means the response was received and everything is ok

results = url.json()
#print(results)

for result in results['results']:
    print(result)