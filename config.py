# coding:utf-8
import os

# FLASK 的选项，调试模式和开启多线程,以及安全码
THREADED = True
DEBUG = False
SECRET_KEY = os.urandom(12)

# SQLALchemy 的配置驱动与修改默认连接池与超时
SQLALCHEMY_TRACK_MODIFIACTIONS = False
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = -1
