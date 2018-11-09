import elasticsearch
import json

es = elasticsearch.Elasticsearch(['localhost:9200'])

print(es)


# body = {"price":10000,"color":"red","make":"honda","sold":'2014-10-28'}
# res = es.index(index="cars", doc_type="transactions", body=body)
# print(res)


es_get = es.get(index="cars", doc_type="transactions",id='ohTiZmYBw6ELWvf0meXG')
print(es_get)

# es_get = es.get(index="cars", doc_type="transactions",id='ohTiZmYBw6ELWvf0meXG')
# print(es_get)


# doc2 = [
#     {"index": {}},
#     {"price": 10000, "color": "red", "make": "honda", "sold": "2014-10-28"},
#     {"index": {}},
#     {"price": 20000, "color": "red", "make": "honda", "sold": "2014-11-05"},
#     {"index": {}},
#     {"price": 30000, "color": "green", "make": "ford", "sold": "2014-05-18"},
#     {"index": {}},
#     {"price": 15000, "color": "pink", "make": "toyota", "sold": "2016-07-02"},
#     {"index": {}},
#     {"price": 12000, "color": "green", "make": "toyota", "sold": "2014-08-19"},
#     {"index": {}},
#     {"price": 18000, "color": "pink", "make": "honda", "sold": "2016-11-05"},
#     {"index": {}},
#     {"price": 80000, "color": "red", "make": "bmw", "sold": "2014-01-01"},
#     {"index": {}},
#     {"price": 25000, "color": "blue", "make": "ford", "sold": "2014-02-12"},
# ]
#
# res2 = es.bulk(index='cars',doc_type='transactions',body=doc2)
# print(res2)
print('='*50)


# query = {'query': {'match_all':{}}}
# res3 = es.search(index='cars',doc_type='transactions',body=query)
# print(json.dumps(res3))
# print('='*50)


query2 = {
    "size":0,
    "aggs":{
        "popular_colors":{
            "terms":{
                "field":"color.keyword",
            }
        }
    }
}

# res4 = es.search(index='cars',doc_type='transactions',body=query2)
# print(res4)


print('*' * 50)

es2 = elasticsearch.Elasticsearch(['es.maimob.net:80'])
query_2   = {
            "size" : 0,
            "aggs" : {
                "distinct_domain" : {
                    "terms" : { "field" : "domain.keyword",
                    "size": 1000
                    }
                }
            }
        }




ret = es2.search(index='app_log', doc_type='app_log', body=query_2)
print(json.dumps(ret))
