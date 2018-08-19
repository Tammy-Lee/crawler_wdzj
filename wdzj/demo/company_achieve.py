# -*- coding: utf-8 -*-
"""
create on 2018-08-19 21:08
author @66492
"""

from wdzj.demo.utils import make_response, update_one

def one_achieve(company_info, api, primary_keys, parse_func):
    response = make_response(api, wdzjPlatId=company_info["wdzj_plat_id"])
    datas = response.json()
    for item in parse_func(datas):
        item.update(company_info)
        update_one(item, primary_keys, api['collection'])


if __name__ == '__main__':
    from wdzj import apis, config
    from wdzj.pools import mongo_db
    from wdzj.demo.parser.basic import parse_volume, parse_return_rate, parse_investor_num_rank
    from wdzj.demo.parser.basic import parse_borrower_num_rank, parse_return_rate_diff, parse_complete_time_diff
    from wdzj.demo.parser.vs import parse_num_investor_vs_borrower, parse_mean_amount_investor_vs_borrower
    from wdzj.demo.parser.vs import parse_num_investor_new_vs_old, parse_amount_investor_new_vs_old
    from wdzj.demo.parser.vs import parse_borrow_time_mean_platform_vs_industry
    from wdzj.demo.parser.deep import parse_num_borrow_and_mean_borrow_time, parse_num_action_borrower_and_investor
    from wdzj.demo.parser.deep import parse_ratio_ten, parse_ratio_fifty

    company_info = mongo_db[config.COL_COMPANY_LIST].find_one({'wdzj_plat_id': {'$ne': '0'}}, {'_id':0})

    # one_achieve(company_info, apis.API_VOLUME, ['plat_id', 'day'], parse_volume)
    # one_achieve(company_info, apis.API_RETURN_RATE, ['plat_id', 'day'], parse_return_rate)
    # one_achieve(company_info, apis.API_INVESTOR_NUM_RANK, ['plat_id', 'day'], parse_investor_num_rank)
    # one_achieve(company_info, apis.API_BORROWER_NUM_RANK, ['plat_id', 'day'], parse_borrower_num_rank)
    # one_achieve(company_info, apis.API_RETURN_RATE_DIFF, ['plat_id', 'day'], parse_return_rate_diff)
    # one_achieve(company_info, apis.API_COMPLETE_TIME_DIFF, ['plat_id', 'day'], parse_complete_time_diff)
    # one_achieve(company_info, apis.API_NUM_INVESTOR_VS_BORROWER, ['plat_id', 'day'], parse_num_investor_vs_borrower)
    # one_achieve(company_info, apis.API_MEAN_AMOUNT_INVESTOR_VS_BORROWER, ['plat_id', 'day'], parse_mean_amount_investor_vs_borrower)
    # one_achieve(company_info, apis.API_NUM_INVESTOR_NEW_VS_OLD, ['plat_id', 'day'], parse_num_investor_new_vs_old)
    # one_achieve(company_info, apis.API_AMOUNT_INVESTOR_NEW_VS_OLD, ['plat_id', 'day'], parse_amount_investor_new_vs_old)
    # one_achieve(company_info, apis.API_BORROW_TIME_MEAN_PLATFORM_VS_INDUSTRY, ['plat_id', 'day'], parse_borrow_time_mean_platform_vs_industry)
    # one_achieve(company_info, apis.API_NUM_BORROW_AND_MEAN_BORROW_TIME, ['plat_id', 'day'], parse_num_borrow_and_mean_borrow_time)
    # one_achieve(company_info, apis.API_NUM_ACTION_BORROWER_AND_INVESTOR, ['plat_id', 'day'], parse_num_action_borrower_and_investor)
    # one_achieve(company_info, apis.API_RATIO_TEN, ['plat_id', 'day'], parse_ratio_ten)
    one_achieve(company_info, apis.API_RATIO_FIFTY, ['plat_id', 'day'], parse_ratio_fifty)
