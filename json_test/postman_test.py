# # 获取返回的响应值转化为json格式
# var jsonData = pm.response.json()
# # 获取返回值中的userid
# userid = jsonData.json['userid']
# # 控制台日志查看
# conlose.log(userid)
# # 将获取的变量设置全局变量
# pm.globals.set("userid":userid)


import requests

url = "postman-echo.com/get?param1=51zxw&param2=6666"

payload  = {}
headers = {
  'Cookie': 'sails.sid=s%3AqNbJhxxv8HGdN85V6Q8k3XZD4F6TRDDK.04wawc%2BpdxqcNguhoEjurjwmDCEH%2BP86BK646QQNS8k'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))