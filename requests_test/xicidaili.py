import requests
proxies = {'http://219.141.153.41:80'}
base_url='http://httpbin.org'
r=requests.get(base_url+'/get',proxies=proxies)
# print(r.status_code)
print(r.text)
