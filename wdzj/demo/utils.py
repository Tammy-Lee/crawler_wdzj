# -*- coding: utf-8 -*-
"""
create on 2018-08-19 19:22
author @66492
"""
from datetime import datetime
from functools import wraps

import requests
from wdzj.pools import mongo_db


def get_cookie(user_name, password):
    return "__jsluid=482d0e2ce653c9237b8f7d4c12fb40a1; _ga=GA1.2.186160903.1514190360; gr_user_id=459f08d6-2ea7-49a0-ba97-e2979f1f7545; Hm_lvt_9e837711961994d9830dcd3f4b45f0b3=1534664852; WDZJptlbs=1; PHPSESSID=idqgn6qr3apsm70f1shh04slm4; _gid=GA1.2.1470476534.1534664852; route=5c08b075b5ccf04e0476a719a6b3587a; Hm_lvt_eca85ec3b21d171104fdb4859d92db71=1534665655; Hm_lvt_903a56ee9d4e88d46e46f9fe7a16b15d=1534665655; Hm_lvt_66c9fe7b5ee3b042ce561068398f2ed6=1534665655; Z6wq_e6e3_saltkey=kKOFzunZ; Z6wq_e6e3_auth=bb05qu0OrhyXkmP6EjI1QLoKj%2BjSJE%2F0fDbauYbpE4eCUjPNJzQ6pWnWD6RueDRSymkHb2ujt77ulfgIzR%2FYFEv557go; auth_token=f70bSqyoQ8od%2FBaNVTmIXEoyKlJgZbMK43li8ldgQZAF3Vxrt3UI1yswyl5srH6gUkhTdgnjJXjJH3JZc%2FgfTrE2xyCg; uid=1720791; login_channel=1; pc_login=1; Z6wq_e6e3_ulastactivity=ec4aOzthkNdzS%2BaYDmLM2T0BnQMKTHqpoCvMCnc3HRW9cegvh%2Fnc; _pk_ref.1.b30f=%5B%22%22%2C%22%22%2C1534675391%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D-iyPhktoCYbkYxkPFEfI50APa0cmzHZhpdNnxSwlz9f1vzgXJirVIZjecZoTk_8N6tGGkgUxGN61OT9Sy5GqTq%26wd%3D%26eqid%3Dc7f8329700016c21000000025ae1f33f%22%5D; _pk_ses.1.b30f=*; WDZJ_FRONT_SESSION_ID=eaa5029f172b447a9c70f94140056d5314360234116607985; gr_session_id_1931ea22324b4036a653ff1d3a0b4693=de961b85-9b14-42ee-a8c2-24d199e78e30; gr_cs1_de961b85-9b14-42ee-a8c2-24d199e78e30=user_id%3A1720791; gr_session_id_1931ea22324b4036a653ff1d3a0b4693_de961b85-9b14-42ee-a8c2-24d199e78e30=true; Hm_lpvt_eca85ec3b21d171104fdb4859d92db71=1534680807; Hm_lpvt_66c9fe7b5ee3b042ce561068398f2ed6=1534680807; Hm_lpvt_903a56ee9d4e88d46e46f9fe7a16b15d=1534680807; Hm_lpvt_9e837711961994d9830dcd3f4b45f0b3=1534681939; _pk_id.1.b30f=9e0594553e9d6d44.1514190360.4.1534681939.1534675391.; _gat=1"


def make_response(api, with_login=False, with_proxy=False, **kwargs):
    """构造response对象
    通过自定义API结构，构造requests的response
    :param api: dict. API结构
    :param with_login: bool. 是否需要登录
    :param kwargs: dict. API中需要传入的值
        如果method为GET，则根据url传递kwargs中的值，
        如果method为POST，则根据formdata传递kwargs中的值
    :return: `requests.Response`
    """
    url = api['url']
    method = api['method']
    formdata = api.get('formdata', {})
    headers = {}
    proxy = {}
    if method == 'GET':
        url = url.format(**kwargs)
    elif method == 'POST':
        formdata.update(kwargs)
    if with_login:
        user_name = kwargs.pop('user_name', '')
        password = kwargs.pop('password', '')
        headers = {'Cookie': get_cookie(user_name, password)}
    if with_proxy:
        proxy = {'http': 'http://localhost:8123'}
    response = requests.request(method, url=url, data=formdata, headers=headers, proxies=proxy)
    return response


def update_one(data, primary_keys, collection_name, upsert_type="$set"):
    _id = "_".join(data[key] for key in primary_keys)
    rst = mongo_db[collection_name].update_one({'_id': _id}, {upsert_type: data}, upsert=True)
    return rst


def show_running_time(func):
    @wraps(func)
    def _show_time(*args, **kwargs):
        now = datetime.now()
        result = func(*args, **kwargs)
        print(func.__name__, datetime.now() - now)
        return result
    return _show_time
