'''

{
    "query":{
        "bool":{
            "filter":[
                {
                    "range":{
                        "timestamp":{
                            "gte":1541347200,
                            "lte":1541433599
                        }
                    }
                },
                {
                    "term":{
                        "appId.keyword":"yyd"
                    }
                }
            ],
            "must_not":[
                {
                    "term":{
                        "type.keyword":{
                            "value":"more"
                        }
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