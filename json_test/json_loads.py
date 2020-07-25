import  json

"""
将json数据转换为python数据，json_loads
"""
# json_str = '{"id":1,"name":"zhangsan","password":"666666"}'
# data = json.loads(json_str)
# print(type(json_str))
# print(type(data))
# print(data)
# print(data["id"])
# print(data["name"])
# """
# 写入json数据到文件
# """
# with open ('data.json', 'w') as f :
#     json.dump(data,f)

"""
读取json数据文件
"""
with open ('data.json', 'r') as f :
    data = json.load(f)
    print(data)