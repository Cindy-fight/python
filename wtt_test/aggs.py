'''


{
    "query":{
        "bool":{
            "filter":[
                {
                    "range":{
                        "timestamp":{
                            "gte":1540742400,
                            "lte":1541433599
                        }
                    }
                },
                {
                    "range":{
                        "action":{
                            "gte":1,
                            "lte":100
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
                "field":"date",
                "order":{
                    "_term":"asc"
                }
            },
            "aggs":{
                "action":{
                    "terms":{
                        "field":"action",
                        "size":100
                    },
                    "aggs":{
                        "distinct_uuid":{
                            "cardinality":{
                                "field":"uuid.keyword"
                            }
                        }
                    }
                }
            }
        }
    }
}




'''