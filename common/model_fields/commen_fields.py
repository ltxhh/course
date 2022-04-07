# -*- codeing = utf-8 -*-
# @Time : 2022/4/6 15:29
# @Author : linyaxuan
# @File : commen_fields.py
# @Software : PyCharm

from flask_restful import fields


def _custom_format(dt, fmt):
    if isinstance(dt, str):
        return dt
    return dt.strftime(fmt)


class CustomDate(fields.DateTime):
    '''
    自定义CustomDate,原有的fileds.DateTime序列化后
    只支持 rfc822,ios8601 格式，新增 strftime 格式
    strftime格式下支持 format 参数，默认为 '%Y-%m-%d %H:%M:%S'
    '''

    def __init__(self, dt_format='rfc822', format=None, **kwargs):
        super(fields.DateTime, self).__init__(**kwargs)
        self.dt_format = dt_format
        self.fmt = format if format else '%Y-%m-%d %H:%M:%S'

    def format(self, value):
        if self.dt_format in ('rfc822', 'iso8601'):
            return super(fields.DateTime.format(value))
        elif self.dt_format == 'strftime':
            return _custom_format(value, self.fmt)
        else:
            raise Exception('Unsupported date format %s' % self.dt_format)


comment_fields = {
    'id': fields.Integer,
    'content': fields.String,
    'uid': fields.Integer,
    'cid': fields.Integer,
    'sid': fields.Integer,
    'reply': fields.Integer,
    'top': fields.Integer,
    'excellent': fields.Integer,
    'favorite': fields.Integer,
    'create_time': CustomDate(dt_format='strftime'),
}
