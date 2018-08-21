# -*- coding: utf-8 -*-
"""
create on 2018-08-19 22:34
author @66492
"""
from wdzj.demo.parser.base import _parse


def parse_volume(datas):
    return _parse(datas, ['date', 'data1'], ['day', 'volume'])


def parse_return_rate(datas):
    return _parse(datas, ['date', 'data1'], ['day', 'return_rate'])


def parse_investor_num_rank(datas):
    new_keys = ['day', 'investor_0to1w', 'investor_1to10w', 'investor_10to100w', 'investor_100w_up']
    return _parse(datas['data1'], ['x', 'y1', 'y2', 'y3', 'y4'], new_keys, "x")


def parse_borrower_num_rank(datas):
    new_keys = ['day', 'borrower_0to20w', 'borrower_20to100w', 'borrower_100w_up']
    return _parse(datas['data1'], ['x', 'y5', 'y6', 'y7'], new_keys, "x")


def parse_return_rate_diff(datas):
    new_keys = [
        'day', 'return_rate_diff_0to1m', 'return_rate_diff_1to2m',
        'return_rate_diff_2to3m', 'return_rate_diff_3to6m', 'return_rate_diff_6m_up'
    ]
    return _parse(datas['data1'], ['x', 'y1', 'y2', 'y3', 'y4', 'y5'], new_keys, "x")


def parse_complete_time_diff(datas):
    new_keys = [
        'day', 'complete_time_diff_0to1m', 'complete_time_diff_1to2m',
        'complete_time_diff_2to3m', 'complete_time_diff_3to6m', 'complete_time_diff_6m_up'
    ]
    return _parse(datas['data1'], ['x', 'y6', 'y7', 'y8', 'y9', 'y10'], new_keys, "x")
