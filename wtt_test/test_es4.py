from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['localhost:9200'])
print(es)
index = 'wtt_test_analyzed'
doc_type = 'wtt_test_analyzed'

def print_line():
    print('=' * 60)

doc = [
    {"index":{'_id':1}},
    {'price':10, 'productID':'XHDK-A-1293-#fJ3', 'address':u'上海'},
    {"index":{'_id':2}},
    {'price':20, 'productID':'KDKE-B-9947-#kL5', 'address':u'杭州'},
    {"index":{'_id':3}},
    {'price':30, 'productID':'JODL-X-1937-#pV7', 'address':u'北京'},
    {"index":{'_id':4}},
    {'price':20, 'productID':'KDKE-B-9947-#kL5', 'address':u'杭州'},
    {"index":{'_id':5}},
    {'price':10, 'productID':'QQPX-R-3956-#aD8', 'address':u'上海'},
]

res = es.bulk(index='wtt_test_analyzed', doc_type='wtt_test_analyzed', body=doc)
print(res)
print_line()


'''

select * from wtt_test_analyzed

'''
print('select * from wtt_test_analyzed')
query1 = {
    "query":{
        "match_all":{}
    }
}

res1 = es.search(index=index, doc_type=doc_type, body=query1)
print(json.dumps(res1))
print_line()



'''

select * from wtt_test_analyzed where price=20

'''
print('select * from wtt_test_analyzed where price=20')
query2 = {
    "query":{
        "term":{
                "price":20
            }
    }
}
res2 = es.search(index=index, doc_type=doc_type, body=query2)
print(json.dumps(res2))
print_line()



'''

使用 constant_score 查询以非评分模式来执行 term 查询并以一作为统一评分
select * from wtt_test_analyzed where price=20

'''
query3 = {
    "query":{
        "constant_score":{
            "filter":{
                "term":{
                    "price":20
                }
            }
        }
    }
}
res3 = es.search(index=index, doc_type=doc_type, body=query3)
print(json.dumps(res3))
print_line()


'''

select * from wtt_test_analyzed where address='上海'
address=上海 被分析了  所以查不到address='上海'的数据

'''

query4 = {
    "query":{
        "constant_score":{
            "filter":{
                "term":{
                    "address.keyword":"上海"
                }
            }
        }
    }
}
res4 = es.search(index=index, doc_type=doc_type, body=query4)
print(json.dumps(res4))
print_line()


'''

analyze

'''
query5 = {
    "query":{
        "match":{
            "title":""
        }
    }
}
res5 = es.search(index=index, doc_type=doc_type, body=query5)









