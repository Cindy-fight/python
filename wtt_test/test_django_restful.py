# coding:utf-8
import requests

url = 'http://127.0.0.1:8000/food/'
data = {'data':2}
result = requests.post(url,json=data)
print(result)
print(result.text)
print(result.content)