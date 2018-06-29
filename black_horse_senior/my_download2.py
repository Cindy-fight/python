import gevent
import urllib.request
from gevent import monkey


'''

实现多个视频下载
注意：url 可以换为自己需要下载视频、音乐、图片等网址

'''

# 有耗时操作时需要
monkey.patch_all()


def my_download(file_name, url):
    print('GET:%s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as f:
        f.write(data)

    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(my_download, '1.mp4', 'http://oo52bgdsl.bkt.clouddn.com/05day-08-%E3%80%90%E7%90%86%E8%A7%A3%E3%80%91%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E6%80%BB%E7%BB%93%EF%BC%88%E4%B8%80%EF%BC%89.mp4'),
    gevent.spawn(my_download, '2.mp4', 'http://oo52bgdsl.bkt.clouddn.com/05day-03-%E3%80%90%E6%8E%8C%E6%8F%A1%E3%80%91%E6%97%A0%E5%8F%82%E6%95%B0%E6%97%A0%E8%BF%94%E5%9B%9E%E5%80%BC%E5%87%BD%E6%95%B0%E7%9A%84%E5%AE%9A%E4%B9%89%E3%80%81%E8%B0%83%E7%94%A8%28%E4%B8%8B%29.mp4'),
    gevent.spawn(my_download, '4.jpg', 'http://h.hiphotos.baidu.com/zhidao/wh%3D680%2C800/sign=677ee4af02f79052ef4a4f3834c3fbf2/a50f4bfbfbedab644495da7cfc36afc378311ea2.jpg'),
    gevent.spawn(my_download, '5.jpg', 'http://pic2.qiyipic.com/image/20180621/15/b9/v_114345562_m_601_m9.jpg'),

])


# 苦恼：很难获得视频或者音乐的下载地址