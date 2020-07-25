import json
data = {'id':1,'name':'51zxw','password':'66666'}
print(type(data))

"""
将python数据转换为json数据，使用json_dumps
"""
json_str = json.dumps(data)
print((type(json_str)))
print((json_str))


