from elasticsearch import Elasticsearch
import json

'''

bulk 方法 批量操作
不仅可以一次性批量执行插入，删除；还可以再一次请求中，既可以插入、又可以删除和更新操作。
注意：任何一种操作都有固定的文档格式，只有完全符合该格式要求，才可执行成功。

'''

es = Elasticsearch(['localhost:9200'])
print(es)

# 批量插入
doc1 = [
    {"index":{}},
    {'name':'jackaaa', 'age':'20', 'sex':'male', 'address':u'上海'},
    {"index":{}},
    {'name':'jackbbb', 'age':'22', 'sex':'female', 'address':u'上海'},
    {"index":{}},
    {'name':'jackccc', 'age':'23', 'sex':'male', 'address':u'杭州'},
    {"index":{}},
    {'name':'jackddd', 'age':'24', 'sex':'female', 'address':u'北京'},
]

doc1_res = es.bulk(index='doc_test', doc_type='document', body=doc1)
# print(doc1_res)

doc1_json = json.dumps(doc1_res)
# print(doc1_json)



# 同时插入 更新  删除

'''

doc = [
    {'index':{'_index':'indexName', '_type':'typeName', '_id':'idValue'}},
    {'name':'Rose','sex':'female', 'age':'18'},
    {'delete':{'_index':'indexName', '_type':'typeName', '_id':'idValue'}},
    {'create':{'_index':'indexName', '_type':'typeName', '_id':'idValue'}},
    {'name':'lucy', 'sex':'female', 'age':30},
    {'update':{'_index':'indexName', '_type':'typeName', '_id':'idValue'}},
    {'doc':{'age':100}},
]


create 与 index的区别：
1、create必须提供id，否则报400错误； 如使用的id已经存在，则会报409错误，所以在create失败时，看错误逐步解决
2、index的id 可以为None


'''

doc2 = [
    {'index':{'_index':'doc_test', '_type':'document', '_id':None}},
    {'name':'Rose','sex':'female', 'age':'18'},
    {'delete':{'_index':'doc_test', '_type':'document', '_id':'V4KftmQBkWPZOkqiogUE'}},
    {'create':{'_index':'doc_test', '_type':'document', '_id':666}},
    {'name':'lucy', 'sex':'female', 'age':30},
    {'update':{'_index':'doc_test', '_type':'document', '_id':'VoKftmQBkWPZOkqiogUE'}},
    {'doc':{'age':100}},
]


doc2_res = es.bulk(index='doc_test', doc_type='document', body=doc2)

print(doc2_res)
print()
print(json.dumps(doc2_res))



query = {'query': {'match_all':{}}}
doc_content = es.search(index='doc_test', doc_type='document', body=query)

# print(doc_content)
# print()
# print(json.dumps(doc_content))

