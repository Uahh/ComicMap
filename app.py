# -*- coding: utf-8 -*-
import config
from models.model import ip
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
    @app.route('/')
    def index():
        temp = ip()
        # city = temp.from_ip_to_city(request.remote_addr)
        city = temp.from_ip_to_city('1.192.119.149')

        return render_template('index.html', user_ip=city[1])

    @app.route('/error/')
    def error():
        return '404 not found'

    app.run(host='0.0.0.0', threaded=True, port=5000)
