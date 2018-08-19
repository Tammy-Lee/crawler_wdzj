# -*- coding: utf-8 -*-
"""
create on 2018-08-19 23:15
author @66492
"""
from wdzj.demo.parser.base import _parse


def parse_num_borrow_and_mean_borrow_time(datas):
    new_keys = ['day', 'num_borrow', 'mean_borrow_time']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_num_action_borrower_and_investor(datas):
    new_keys = ['day', 'num_action_borrower', 'num_action_investor']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_ratio_ten(datas):
    new_keys = ['day', 'top_ten_investor_to_receice', 'top_ten_borrower_to_repay']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_ratio_fifty(datas):
    new_keys = ['day', 'top_fifty_investor_to_receice', 'top_fifty_borrower_to_repay']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)
