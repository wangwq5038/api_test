import json
import requests
base_url='http://httpbin.org'
r = requests.get(base_url + '/stream/10', stream=True)
# 流式请求
# 如果响应内容没有设置编码，则默认设置为 utf-8 if r.encoding is None:
r.encoding = 'utf-8'
for line in r.iter_lines(decode_unicode=True):
    if line:
        data=json.loads(line)
        print(data['id'])