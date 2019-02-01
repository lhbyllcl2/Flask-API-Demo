# -*- coding:utf-8 _*-
from flask import Blueprint
from app.api import user


def create_blueprint():
    api_bp = Blueprint('api', __name__)
    user.api.register(api_bp)
    # 注册多个在此添加
    # order.api.register(api_bp)
    return api_bp
