from urllib import request
import json
import uuid

def get_province_city_by_ip(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    result = request.urlopen(url)
    content = result.read()
    return json.loads(content)


test = get_province_city_by_ip('118.31.249.12')
print(test)




mgid = '6ec28662-85b7-11e8-a8e3-00163e0f7e2e'
# mgid = str(uuid.uuid1())
mgid = str(uuid.uuid1()).replace('-','')

print(mgid)


# curl -X GET "localhost:9200/cars/transactions/_search" -H 'Content-Type: application/json' -d'

query = {
    "size" : 0,
    "query" : {
        "match_all" : {}
    },
    "aggs" : {
        "colors" : {
            "terms" : {
              "field" : "color"
            }
        }
    }
}


query1 = {
  "aggs" : {
    "actors" : {
      "terms" : {
         "field" : "actors",
         "size" :  10
      },
      "aggs" : {
        "costars" : {
          "terms" : {
            "field" : "actors",
            "size" :  5
          }
        }
      }
    }
  }
}




query2 = {
  "aggs" : {
    "actors" : {
      "terms" : {
         "field" :        "actors",
         "size" :         10,
         "collect_mode" : "breadth_first"
      },
      "aggs" : {
        "costars" : {
          "terms" : {
            "field" : "actors",
            "size" :  5
          }
        }
      }
    }
  }
}




