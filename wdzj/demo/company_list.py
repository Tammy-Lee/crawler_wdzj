# -*- coding: utf-8 -*-
"""
create on 2018-08-19 19:06
author @66492
"""
from wdzj import apis
from wdzj.demo.utils import make_response, update_one


def get_plat_id(company_info):
    if company_info['wdzjPlatId'] != 0:
        return str(company_info['wdzjPlatId'])
    try:
        plat_id = int(company_info['platId'])
        return company_info['platId']
    except ValueError:
        return "0"


def normal_single(date):
    api = apis.API_PLAT_SOURCE
    response = make_response(api, shujuDate=date)
    companies = response.json()
    collection_name = api['collection']
    primary_keys = ['plat_id']
    for company in companies:
        item = {
            'wdzj_plat_id': get_plat_id(company),
            'name': company['platName'],
            'background': company.get("newbackground", None),
            'plat_id': company['platId'],
            'status': 'normal'
        }
        update_one(item, primary_keys, collection_name)


def normal(dates=None, verbose=False):
    default_dates = [
        "2018-01-012018-01-31", "2018-02-012018-02-28", "2018-03-012018-03-31",
        "2018-04-012018-04-30", "2018-05-012018-05-31", "2018-06-012018-06-30",
        "2018-07-012018-07-31", "2018-08-012018-08-31"
    ]
    dates = dates or default_dates
    for date in dates:
        if verbose:
            print(date)
        normal_single(date)


def _get_problem_company_list(api, **kwargs):
    response = make_response(api, with_login=True, **kwargs)
    companies = response.json()["problemList"]
    collection_name = api['collection']
    primary_keys = ["plat_id"]
    for company in companies:
        item = {
            'wdzj_plat_id': get_plat_id(company),
            'name': company['platName'],
            'background': company.get("newbackground", None),
            'plat_id': company['platId'],
            'status': company['type'],
        }
        update_one(item, primary_keys, collection_name)


def shutdown():
    api = apis.API_SHUTDOWN
    kwargs = {'year': ''}
    _get_problem_company_list(api, **kwargs)


def problem():
    api = apis.API_PROBLEM
    kwargs = {'year': ''}
    _get_problem_company_list(api, **kwargs)

if __name__ == '__main__':
    normal(verbose=True)
    shutdown()
    problem()
