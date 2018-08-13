import re
ss = 'edit_article/article_id=3'
ll = re.match(r'^edit_article/article_id=(\d+)$', ss)
print(ll)
print(ll.group(0))
print(ll.group(1))


print()
id = ''
if id.strip() == '':
    print(123)
else:
    print(456)




# for article in articles:

list = []

dict = [{'id': 1, 'title': '麦广公司简介', 'content': '麦广互娱的创立是为了打造广告主和媒体之间的桥梁，在覆盖大量智能手机用 户的基础上，利用自身强大的数据挖掘、分析能力，建立强大的媒体用户数据 库，结合专业的营销策略，从而达到移动营销的效果最大化。', 'image': '123.jpg', 'type': 1, 'recordTime': (2018, 7, 27, 15, 20, 16), 'updateTime': (2018, 7, 27, 15, 20, 16), 'status': 1}]

for id in dict:
    # print(id)
    print(id['title'])


    res = {
        'title':id['title'],
        'content': id['content'],
        'image':id['image'],
    }
    list.append(res)



# item = {
#     # 'title':article.title,
#     # 'type':CommonUtils.get_article_name_by_type(article.type),
#     'type':1,
#     'content':1,
#     'date':1
# }
# list.append(item)

print(list)


print()
print()

import time
t = int(time.time())

print(t)

print(type(t))





