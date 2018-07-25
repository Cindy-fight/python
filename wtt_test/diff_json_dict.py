'''

json 和 python 中字典的区别和联系
1、python dict 字符串用单引号，json强制规定双引号
2、python dict 里可以嵌套tuple，json里只有 arrayjson.dumps({1:2})的结果是{"1":2}，而python中的json模块函数：
   json.dumps((1,2))的结果是[1,2]
3、json key name 必须是字符串，python是hashable， {(1,2):1}在python里是合法的，因为tuple是hashable type；
   {[1,2]:1}在python里TypeError：unhashable "list"
4、json: true false null  ; python: True False None
5、python {"me":"我"}是合法的，json必须是{"me":"\u6211"}
6、python中有专门处理json数据的模块：json
    json.dumps()   dict转json
    json.loads()   json转dict
'''


import json

# dict 转 json
dict = {'took': 23, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 4, 'max_score': 1.0, 'hits': [{'_index': 'articleindex', '_type': 'doctype', '_id': '0', '_score': 1.0, '_source': {'articleid': '2', 'title': 'title', 'content': 'content'}}, {'_index': 'articleindex', '_type': 'doctype', '_id': '2', '_score': 1.0, '_source': {'articleid': '2', 'title': 'wtttest', 'content': 'wtttest'}}, {'_index': 'articleindex', '_type': 'doctype', '_id': '1', '_score': 1.0, '_source': {'articleid': '2', 'title': 'title', 'content': 'content'}}, {'_index': 'articleindex', '_type': 'doctype', '_id': '3', '_score': 1.0, '_source': {'articleid': '2', 'title': 'hello', 'content': 'world'}}]}}

json_str = json.dumps(dict)

print(json_str)


# json 转 dict
json_dict = json.loads(json_str)

print(json_dict)


print(json.dumps((1,2)))    # [1, 2]
