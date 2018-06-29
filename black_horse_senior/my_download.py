import gevent
import urllib.request
from gevent import monkey


'''

并发下载器原理

'''

# 有耗时操作时需要
monkey.patch_all()


def my_download(url):
    print('GET:%s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(my_download, 'http://www.baidu.com/'),
    gevent.spawn(my_download, 'http://www.itcast.cn/'),
    gevent.spawn(my_download, 'http://www.itheima.com/'),
])
