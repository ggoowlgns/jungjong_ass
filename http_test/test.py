import urllib.request
import requests
import json

data_en = {'pro_name': 'test' ,'pro_count':32}
data_par = json.dumps(data_en).encode("utf-8")
print(data_par)
req =urllib.request.Request(url = "http://127.0.0.1:80/product/put_product",  data = data_par , method='PUT', headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
page = response.read()
print(page)
