# -*- coding: utf-8 -*-
"""
create on 2018-08-19 22:35
author @66492
"""
from wdzj.demo.parser.base import _parse


def parse_num_investor_vs_borrower(datas):
    new_keys = ['day', 'num_investor', 'num_borrower']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_mean_amount_investor_vs_borrower(datas):
    new_keys = ['day', 'mean_amount_investor', 'mean_amount_borrower']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_num_investor_new_vs_old(datas):
    new_keys = ['day', 'num_investor_new', 'num_investor_old']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_amount_investor_new_vs_old(datas):
    new_keys = ['day', 'amount_investor_new', 'amount_investor_old']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys)


def parse_borrow_time_mean_platform_vs_industry(datas):
    new_keys = ['day', 'borrow_time_mean_platform', 'borrow_time_mean_industry']
    return _parse(datas, ['date', 'data1', 'data2'], new_keys, padding=True)
