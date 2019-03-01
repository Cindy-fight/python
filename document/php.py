"""

TIPS 2
str_split($str,$length)  将字符串分割到数组中，默认长度为1，可以自己设长度
is_numeric 检测变量是否是数字或者数字字符串，如果是则返回 TRUE，否则返回 FALSE。
array_shift  将数组第一个单元弹出（出栈）
array_pop   将数组最后一个单元弹出（出栈）
array_push() - 将一个或多个单元压入数组的末尾（入栈）
array_shift() - 将数组开头的单元移出数组
array_unshift() - 在数组开头插入一个或多个单元
array_key_exists — 检查给定的键名或索引是否存在于数组中
isset() - 检测变量是否设置
in_array() - 检查数组中是否存在某个值
property_exists() - 检查对象或类是否具有该属性
strrpos — 计算指定字符串在目标字符串中最后一次出现的位置
bcpow() 左操作数的右操作数次方运算.  echo bcpow('4.2', '3', 2); // 74.08
bcsqrt() - 任意精度数字的二次方根
array_keys() - 返回数组中部分的或所有的键名
array_values() - 返回数组中所有的值
array_key_exists() - 检查给定的键名或索引是否存在于数组中
array_search() - 在数组中搜索给定的值，如果成功则返回相应的键名
str_pad — 使用另一个字符串填充字符串为指定长度
bcmul 两个任意精度数字乘法计算
http_build_query()  生成URL-encode之后的请求字符串

curl_init（）  初始化一个CURL会话
初始化一个新的CURL会话并获取一个网页
$ch = curl_init();                          //创建一个新的CURL资源
curl_setopt($ch,CURLOPT_URL,’http://www.example.com’);
curl_setopt($sh,CURL_HEADER,0);           //设置URL和相应的选项
curl_exec($ch);                          //抓取URL并把它传递给浏览器
curl_close($ch);                         // 关闭CURL资源，并且释放系统资源
curl_getinfo();                           //获取一个CURL连接资源句柄的信息
curl_errno();                             //返回最后一次的错误号，如果没有错误发生则返回0
curl_error();   //返回一个保护当前会话最近一次错误的字符串，如果没有发生任何错误则返回空字符串


simplexml_load_string()             //将XML转为对象
instanceof    (1)判断一个对象是否是某个类的实例；（2）判断一个对象是否实现了某个接口
json_decode($json,bool $assoc)  当$assoc 为TRUE时，将返回数组而非对象
reset()        将数组的内部指针指向第一个单元
current()     返回数组中的当前单元
each()         返回数组中当前的键值对并将数组指针向前移动一步
end()           将数组的内部指针指向最后一个单元
next()           将数组中的内部指针向前移动一位
prev()           将数组的内部指针倒回一位
urlencode()  编码url字符串

authenticate
vt.	证明是真实的、可靠的或有效的; 鉴定，使生效;

getenv(“var”)  获取一个环境变量的值
putenv(“var=value”)  设置一个环境变量的值
mb_detect_encoding()  检测字符的编码
strrchr — 查找指定字符在字符串中的最后一次出现


TIPS

1、可以使用  AUTOINCREMENT  代替  AUTO_INCREMENT
2、schema Caching Duration  构架缓存持续时间
3、[CActiveRecord::getDbConnection()]
4、Named Scopes 命名范围
5、DDL(Data Definition Language)数据库定义语言
6、init初始化  widget 小装置


开机第一步

1、启动APACHE
	sudo apachectle start
2、启动mysql
	进入mysql相应目录下cd /usr/local/bin，./mysql
3、启动 memcache 库
	进入memcache相应目录下 cd /usr/local/bin，memcached -d -p 21214
4、启动gearmand
5、打开相关工作软件  eclipse  workbench



AR下的SQL（YII2.0）

1、find
$post=Post::model()->find($condition,$params);
$post=Post::model()->findByPk($postID,$condition,$params);
$post=Post::model()->findByAttributes($attributes,$condition,$params);
$post=Post::model()->findBySql($sql,$params);

可以使用findall代替find ，例如
$post=Post::model()->findByPk($postID,$condition,$params);
$posts=Post::model()->findAllByPk($postIDs,$condition,$params);

findall查询后如果没有值的话会返回一个空数组 find如果没有值的话会返回null

2、count
$n=Post::model()->count($condition,$params);
$n=Post::model()->countBySql($sql,$params);
$exists=Post::model()->exists($condition,$params);

3、update
Post::model()->updateAll($attributes,$condition,$params);
Post::model()->updateByPk($pk,$attributes,$condition,$params);
Post::model()->updateCounters($counters,$condition,$params);

4、delete
Post::model()->deleteAll($condition,$params);
Post::model()->deleteByPk($pk,$condition,$params);

$posts=Post::model()->published()->recently()->findAll();
Post::model()->published()->recently()->delete();
$posts=Post::model()->published()->recently(3)->findAll();
$contents=Content::model()->findAll();


数据缓存：
1、Yii::app()->cache->set($ID，$value,30);
2、Yii::app()->cache->get($id);
3、Yii::app()->cache->delete($id);  删除一个缓存值
4、Yii:app()->cache->flush($id);  清空所有缓存
5、Yii::app()->cache()->set($id,$value,30,new CFileCacheDependency(’FileName’));  缓存依赖
缓存依赖  缓存会在30秒后过期  也可能因依赖的文件有更新而更快失效
缓存依赖分为 CDbCacheDependency  、 CGlobalCacheDependency
缓存如果不设生存时间，其默认生存时间为一年

执行SQL 语句：
SmsTransaction::model()->getDbConnection()->createCommand($sql)->execute();


"""