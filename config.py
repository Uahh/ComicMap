# coding:utf-8
import os
# 这些都是数据库信息
HOST = '127.0.0.1'
# 数据库账号密码端口
DATABASE = 'langzi_eyes'
USER = 'root'
PASSWORD = 'root'
PORT = 3306
DRIVER = 'pymysql'

# FLASK 的选项，调试模式和开启多线程,以及安全码
THREADED = True
DEBUG = False
SECRET_KEY = os.urandom(12)

# SQLALchemy 的配置驱动与修改默认连接池与超时
SQLALCHEMY_DATABASE_URI = 'mysql+' + DRIVER + '://' + USER + ':' + PASSWORD + '@' + HOST + ':' + str(PORT) + '/' + DATABASE + '?charset=utf8'
SQLALCHEMY_TRACK_MODIFIACTIONS = False
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = -1
