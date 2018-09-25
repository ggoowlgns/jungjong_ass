import urllib.request
import requests

data_en = {'pro_name': 'test' ,'pro_count':32}
data_par = urllib.parse.urlencode(data_en).encode("utf-8")
print(data_par)
#requests.put("http://220.67.124.128:800/student/out",data = data_en)
req =urllib.request.Request(url = "http://127.0.0.1:8000/product/put_product",  data = data_par , method='PUT')
response = urllib.request.urlopen(req)
page = response.read()
print(page)
