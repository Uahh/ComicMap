# -*- coding: utf-8 -*-
import time
import json
import config
import sqlite3
from models import functions
from models.model import IP
from flask import Flask
from flask import request
from flask import render_template
from flask_apscheduler import APScheduler


def update_city_json():
    conn = sqlite3.connect(r'data/comic_database.db')
    c = conn.cursor()
    cursor = c.execute("SELECT \"index\", value, city, province, longitude, latitude FROM city")
    ans = {
        "cities": []
    }
    for raw in cursor:
        temp = [raw[0], raw[1], raw[2], raw[3], raw[4], raw[5]]
        ans['cities'].append(temp)

    with open("data/city_table.json", "w", encoding='utf-8') as f:
        json.dump(ans, f, ensure_ascii=False, sort_keys=True, indent=4)
    print(time.asctime(time.localtime(time.time())))
    print("city_table Json文件已更新")


def update_province_json():
    conn = sqlite3.connect(r'data/comic_database.db')
    c = conn.cursor()
    cursor = c.execute("SELECT \"index\", value, city, province, longitude, latitude FROM city")
    temp = {}
    for raw in cursor:
        if raw[3] in temp.keys():
            temp[raw[3]] += raw[1]
        else:
            temp[raw[3]] = 0
    res = []
    for i in temp.keys():
        res.append(
            {
                'name': i,
                'value': temp[i]
            }
        )
    with open("data/province_table.json", "w", encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, sort_keys=True, indent=4)
    print(time.asctime(time.localtime(time.time())))
    print("province_table Json文件已更新")


class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'update_city_json',  # 任务id
            'func': '__main__:update_city_json',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'interval',  # 任务执行类型，定时器
            'seconds': 20  # 任务执行时间，单位秒
        },
        {
            'id': 'update_province_json',
            'func': '__main__:update_province_json',
            'args': None,
            'trigger': 'interval',
            'seconds': 21
        }
    ]


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(config)
app.config.from_object(SchedulerConfig)
print('Waiting......')


# 主要逻辑视图函数
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    city, _ = IP.from_ip_to_city('120.204.100.39')
    if '新疆' in city or '西藏' in city or '宁夏' in city or '内蒙' in city or '广西' in city and '市' in city:
        # print(city)
        if '新疆' in city:
            city = city[0:city.find('新疆') + 2] + '省' + city[city.find('新疆') + 2:]
        if '西藏' in city:
            city = city[0:city.find('西藏') + 2] + '省' + city[city.find('西藏') + 2:]
        if '宁夏' in city:
            city = city[0:city.find('宁夏') + 2] + '省' + city[city.find('宁夏') + 2:]
        if '内蒙' in city:
            city = city[0:city.find('内蒙') + 3] + '省' + city[city.find('内蒙') + 3:]
        if '广西' in city:
            city = city[0:city.find('广西') + 2] + '省' + city[city.find('广西') + 2:]
    if '省' in city or '市' in city or '县' in city or '区' in city:
        if '省' in city and '市' in city:
            begin = city.find('省') + 1
            end = city.find('市') + 1
            city = city[begin:end]
        elif '省' in city and '县' in city:
            begin = city.find('省') + 1
            end = city.find('县') + 1
            city = city[begin:end]
        elif '市' in city and '区' in city:
            begin = 0
            end = city.find('市') + 1
            city = city[begin:end]
    return render_template('board.html', result_json=json.dumps({'a': city}))


@app.route('/get_data', methods=["GET", "POST"])
def get_data():
    with open(r'data/province_table.json', encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return json.dumps(data)


@app.route('/get_city_table', methods=["GET", "POST"])
def get_city_table():
    with open(r'data/city_table.json', encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return data


@app.route('/geo_china_json', methods=["GET", "POST"])
def geo_china_json():
    with open(r'data/chinageo.json', encoding='utf-8') as f:
        test_line = json.load(f)
        f.close()
    return test_line


@app.route('/error')
def error():
    return '404 not found'


if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', debug=False, port=173)
