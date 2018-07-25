# import sys
#
# print(sys.version_info)
#
# if (2, 7) <= sys.version_info < (3, 2):
#     print('OK')
#
#
# print()




from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'])

print(es)


'''

elasticsearch 操作分为两大类：
1、单一操作
2、批量操作

'''


# articles = {"articleid":"2","title":"hello","content":"world"}
articles = {"title":"title","content":"content"}
# res = es.index(index="articleindex", doc_type="doctype", id=3, body=articles)
# print(res)
# print()

# # es.create(index="articleindex", doc_type="doctype", id=0, body=articles, ignore=409)
# result = es.get(index="articleindex", doc_type="doctype", id=3)
# print(result)

# print('Hello')



'''

单一操作


'''

# 插入
index_res = es.index(index='indexName', doc_type='typeName', id = None, body = articles)


# 删除
delete_res = es.delete(index='indexName', doc_type='typeName', id='idValue')


# 更新
update_res = es.update(index='indexName', doc_type='typeName', id='idValue', body={'待更新字段'})


# 查找
select_res = es.get(index='indexName', doc_type='typeName', id='idValue')





body = {
    "name":         "Rose",
    "age":          24,
    "confirmed":    True,
    "join_date":    "2015-06-01",
    "home": {
        "lat":      51.5,
        "lon":      0.1
    },
    "accounts": [
        {
            "type": "dancer",
            "id":   "1"
        },
        {
            "type": "writing",
            "id":   "2"
        }
    ]
}

# index1 = es.index(index='test', doc_type='document', body=body)
# print(index1)


'''

批量操作
批量查找：es.search
批量删除：es.delete_by_query
批量更新：es.update_by_query

'''


# 批量查找
query = {'query': {'match_all':{}}}     # 查找所有文档
query1 = {'query': {'term':{'name':'Rose'}}}    # 查找name为Rose的所有文档
query2 = {'query': {'range':{'age':{'gt':11}}}}  #查找年龄大于11 的所有文档


# 批量查找执行程序
allDoc = es.search(index='articleindex', doc_type='doctype', body=query)
print(allDoc)
print()


allDoc_test = es.search(index='test', doc_type='document', body=query)
print(allDoc_test)



# 批量删除
deleteQuery1 = {'query':{'match':{'sex':'female'}}}    # 删除性别为女性的所有文档
deleteQuery2 = {'query':{'range':{'age':{'lt':11}}}}   # 删除年龄小于11的所有文档

deleteQuery = {'query':{'match':{'title':'title'}}}   # 删除标题为title 的所有文档

# 批量删除执行程序
deleteRes = es.delete_by_query(index='articleindex', doc_type='doctype', body=deleteQuery)

print(deleteRes)



# 批量更新
updateQuery = {}

# 批量删除执行程序
updateRes = es.update_by_query(index='articleindex', doc_type='doctype', body=updateQuery)








