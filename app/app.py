# -*- coding:utf-8 _*-
from flask import Flask
from flask_cors import *


# 蓝图注册
def register_blueprints(app):
    from app.api import create_blueprint
    app.register_blueprint(create_blueprint(), url_prefix='/api')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.config')
    # 解决跨域问题
    CORS(app, max_age=3600, supports_credentials=True)
    register_blueprints(app)
    return app
