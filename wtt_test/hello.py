rate = '{:.2%}'.format(12 / 130)
print(rate)


import re
res = re.match(r'^20\d{2}-\d{2}-\d{2}$', '2018-09-18')
flag = False
if res:
    flag = True


print(res)
print(flag)

if flag:
    print('OK')
else:
    print('ERROR')


import time
timestamp = int(time.time())
print(timestamp)

dict = {'request': {'timeStamp': 1541073438673, 'request': {'comm': {'channelNo': '0202020002', 'requestCode': 'standard_queryCredit', 'version': '1.0', 'needret': 'yes', 'sendTime': '20181101195718', 'serialNo': '201811011957185179310438352205'}, 'data': {'prodSubNo': '202001', 'serialNo': '2018110115400d747940bec644a180a5608384e63f16'}}}, 'response': {'error_msg': '[0001]交易成功', 'data': '{"result_code":null,"serialNo":null,"creditLimitTotal":null,"creditNo":"C591811010000374231","restartTime":null,"expirationDate":null,"result_msg":null,"status":"03","interestRateInfo":null,"error_code":"0000","error_msg":"[0001]交易成功"}', 'error_code': '0000', 'creditNo': 'C591811010000374231', 'status': '03'}, 'flowNo': 'd30035af-86ff-4b30-abce-55091b50babb'}

data = dict['response']['data']
print(data)
print(type(data))

import json

dict['response']['data'] = json.loads(data)

print(type(dict['response']['data']))

print(dict)

'''

项目名称   项目描述	          负责人   	进度状态	     预计完成时间    已完成模块内容	           未完成模块内容

又一贷    埋点数据统计优化    王婷婷     已优化完成      已完成        产品收益、被拒导流页、更多借款    无
包贷款    埋点数据统计优化    王婷婷     已优化完成      已完成        产品收益、被拒导流页、更多借款    无
日至系统  合作方日志存入失败   王婷婷      已修复        已完成         bug修复                     无

'''
