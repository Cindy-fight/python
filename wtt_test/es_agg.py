"""

GET diverse_data/diverse_data/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "timestamp": {
              "gte": 1540224000,
              "lte": 1540310399
            }
          }
        },
        {
          "range":{
            "action":{
              "gte":0,
              "lte":100
            }
          }
        }

      ]
    }
  },
  "aggs": {   #文档按照uuid划分
      "uuid":{
        "terms": {
          "field": "uuid.keyword"
        },
        "aggs": { #当前uuid的文档堆再按照action划分
          "action_term":{
            "terms": {
              "field": "action"
            },
            "aggs": { #最小堆计数
              "action_count": {
                "value_count": {
                  "field": "action"
                }
              }
            }
          }
        }
      }
    }
}


"""








"""


"deviceInfo": {
              


              "brand": "OPPO",
              "model": "OPPO R9s",
              "zhiwen":"",
              "os": "Android",
              "osVersion": "6.0.1",
               "latitude": "31.209024",
              "longitude": "121.612495",
              "ip": "192.168.1.113",
              "province":"",
              "city":"",
              渠道号
              登录类型
              "uuid": "067406CE044ECFD2E154B38E97887DFA",  区分设备
              
            },
            
"jump:"{
        "id":
        "url":
}




{"app": 
    {"request": 
        {"baseRequest": 
            {"args": 
                {"appInfo": {"appId": 1, "appName": "bdk", "appPackage": "cn.caima.baoloan", "appVersion": "1.0.1", "md5Version": 1, "partnerType": 3, "type": 3, "version": 0},
                "behavior": {"beginTime": 1540521154350, "customerId": "20181026101300001172", "deviceId": "A3FC5A54-B509-46BA-A12F-7550785E2143", "endTime": 1540521179508, "eventType": "05", "ip": "180.168.36.58", "latitude": "31.20547221010087", "longitude": "121.60180817844477"}, 
                "body": {"eventType": 2, "files": [{"context": "/9j/4AAQSkZJRgABAQAASABIAAD









"""





'''


{
    "query":{
        "bool":{
            "filter":[
                {
                    "range":{
                        "timestamp":{
                            "gte":1541433600,
                            "lte":1541606399
                        }
                    }
                },
                {
                    "term":{
                        "appId.keyword":"yyd"
                    }
                }
            ]
        }
    },
    "aggs":{
        "date":{
            "terms":{
                "field":"date"
            },
            "aggs":{
                "type":{
                    "terms":{
                        "field":"type.keyword",
                        "size":1000
                    },
                    "aggs":{
                        "position":{
                            "terms":{
                                "field":"productList.position"
                            },
                            "aggs":{
                                "productId":{
                                    "terms":{
                                        "field":"productList.productId"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


'''


'''



    import time
    date1 = time.strptime(idNoEndTime,"%Y-%m-%d")
    time1 = time.mktime(date1)
    resDate = time.strftime("%Y-%m-%d", time.localtime(time1))
    body['request']['baseRequest']['args']['body']['idNoEndTime'] = resDate

    print(resDate)
    
    
    


    print(int(time.time()))
    print(time.localtime())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


    # timestamp = Utils.get_unix_time()
    # date = Utils.get_today()
    # print(timestamp)
    # print(date)
    # date1 = Utils.get_day_by_unix(timestamp)
    # print(date1)

    es = Utils.get_es()
    # # query = {
    # #     "query":{
    # #         "match":{
    # #             'uuid.keyword':'18eca434d27e11e88fc1ac87a319d9e4'
    # #         }
    # #     }
    # # }
    # # res = es.search(index='diverse_data', doc_type='diverse_data', body=query)
    # # res = es.delete(index="diverse_data", doc_type="diverse_data")
    # query = {
    #     "query":{
    #         "match_all":{}
    #     }
    # }
    res = es.delete_by_query(index="diverse_data", doc_type="diverse_data", body=query)
    return Utils.json_out(res)


'''






















