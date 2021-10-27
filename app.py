# -*- coding: utf-8 -*-
import json
import config
from models.model import IP
from flask import Flask
from flask import request
from flask import render_template


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(config)
    return app


if __name__ == '__main__':
    app = create_app()
    print('Waiting......')

    # 主要逻辑视图函数
    @app.route('/', methods=["GET", "POST"])
    @app.route('/index', methods=["GET", "POST"])
    def index():
        # city, _ = IP.from_ip_to_city(request.remote_addr)
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
        return render_template('board.html', result_json=json.dumps({'a': IP.city_gps[city]}))

    @app.route('/get_json', methods=["GET", "POST"])
    def get_json():
        with open(r'data/test.json', encoding='utf-8') as f:
            test_gps = json.load(f)
            f.close()
        return test_gps

    @app.route('/error/')
    def error():
        return '404 not found'

    app.run(host='0.0.0.0', debug=True, port=173)
