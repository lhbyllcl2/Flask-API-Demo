# -*- coding:utf-8 -*-
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/login', methods=['POST'])
def login():
    pass
