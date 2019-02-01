# -*- coding: utf-8 -*-
from flask_jwt import jwt
import datetime
from app.config import config
from flask import request


class Auth(object):
    @staticmethod
    def encode_auth_token(data):
        """
        生成token
        :param data:
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'iss': 'xxxxx',
                'data': data
            }
            return jwt.encode(
                payload,
                config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception:
            return None

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, config.SECRET_KEY, options={'verify_exp': False})
            if 'exp' in payload and 'data' in payload and 'user_id' in payload['data']:
                return payload
            else:
                return 1004
        except jwt.ExpiredSignatureError:
            return 1005  # 过期
        except jwt.InvalidTokenError:
            return 1004  # 无效

    def identify(self):
        """
        权限验证
        :return:
        """
        auth_token = request.headers['X-Token']
        if not auth_token:
            return 1000
        payload = self.decode_auth_token(auth_token)
        if isinstance(payload, int):
            return payload
        user_id = payload['data']['user_id']
        if user_id != 1:  # todo 实际查询mysql
            return 1000
