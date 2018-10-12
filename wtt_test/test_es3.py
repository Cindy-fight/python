import elasticsearch

es = elasticsearch.Elasticsearch(['localhost:9200'])

print(es)


# body = {"price":10000,"color":"red","make":"honda","sold":'2014-10-28'}
# res = es.index(index="cars", doc_type="transactions", body=body)
# print(res)

es_get = es.get(index="cars", doc_type="transactions",id='ohTiZmYBw6ELWvf0meXG')
print(es_get)