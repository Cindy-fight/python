'''

需求：既要把日志输出到控制台，还要写入日志文件


logging.basicConfig函数中，可以指定日志的输出格式format，这个参数可以输出很多有用信息，如

%(levelno)s : 打印日志级别的数值
%(levelname)s : 打印日志级别名称
%(pathname)s : 打印当前执行程序的路径，其实就是 sys.argv[0]
%(filename)s : 打印当前执行程序名
%(funcName)s : 当前日志的当前函数
%(lineno)d : 打印日志的当前行号
%(asctime)s : 打印日志的当前时间
%(thread)d : 打印线程ID
%(threadName)s : 打印线程名称
%(process)d : 打印进程ID
%(message)s : 打印日志信息

'''

import logging


# 第一步  创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)   # Log等级总开关



# 第二步  创建一个handler，用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a+')
fh.setLevel(logging.DEBUG)   # 输出到file的log等级开关



# 第三步  再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)    # 输出到console的log等级开关



# 第四步  定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)



# 第五步  将 logger 添加到 handler 里面
logger.addHandler(fh)
logger.addHandler(ch)


# 日志
logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')

