# -*- coding: utf-8 -*-
"""
create on 2018-08-19 22:34
author @66492
"""
def _parse(datas, org_keys, new_keys, date_key="date", padding=False, padding_value=None):
    if padding:
        max_len = len(datas[date_key])
        datas = {key: (datas[key] + (max_len - len(datas[key])) * [padding_value]) for key in org_keys}
    group_data = zip(*[datas[key] for key in org_keys])
    for data in group_data:
        item = {}
        for i, v in enumerate(data):
            item[new_keys[i]] = v
        yield item
