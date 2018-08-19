# -*- coding: utf-8 -*-
"""
create on 2018-08-19 23:50
author @66492
"""
from queue import Queue
from threading import Thread

from wdzj import config, apis
from wdzj.demo.company_achieve import one_achieve
from wdzj.demo.parser.basic import parse_volume, parse_return_rate, parse_investor_num_rank
from wdzj.demo.parser.basic import parse_borrower_num_rank, parse_return_rate_diff, parse_complete_time_diff
from wdzj.demo.parser.vs import parse_num_investor_vs_borrower, parse_mean_amount_investor_vs_borrower
from wdzj.demo.parser.vs import parse_num_investor_new_vs_old, parse_amount_investor_new_vs_old
from wdzj.demo.parser.vs import parse_borrow_time_mean_platform_vs_industry
from wdzj.demo.parser.deep import parse_num_borrow_and_mean_borrow_time, parse_num_action_borrower_and_investor
from wdzj.demo.parser.deep import parse_ratio_ten, parse_ratio_fifty
from wdzj.demo.utils import show_running_time
from wdzj.pools import mongo_db

companies = mongo_db[config.COL_COMPANY_LIST].find({'wdzj_plat_id': {'$ne': '0'}, 'finished': {'$ne': 1}}, {'_id':0})
total_apis = [
    apis.API_VOLUME, apis.API_RETURN_RATE, apis.API_INVESTOR_NUM_RANK, apis.API_BORROWER_NUM_RANK,
    apis.API_RETURN_RATE_DIFF, apis.API_COMPLETE_TIME_DIFF, apis.API_NUM_INVESTOR_VS_BORROWER,
    apis.API_MEAN_AMOUNT_INVESTOR_VS_BORROWER, apis.API_NUM_INVESTOR_NEW_VS_OLD, apis.API_AMOUNT_INVESTOR_NEW_VS_OLD,
    apis.API_BORROW_TIME_MEAN_PLATFORM_VS_INDUSTRY, apis.API_NUM_BORROW_AND_MEAN_BORROW_TIME,
    apis.API_NUM_ACTION_BORROWER_AND_INVESTOR, apis.API_RATIO_TEN, apis.API_RATIO_FIFTY
]
parse_functions = [
    parse_volume, parse_return_rate, parse_investor_num_rank,parse_borrower_num_rank, parse_return_rate_diff,
    parse_complete_time_diff, parse_num_investor_vs_borrower, parse_mean_amount_investor_vs_borrower,
    parse_num_investor_new_vs_old, parse_amount_investor_new_vs_old, parse_borrow_time_mean_platform_vs_industry,
    parse_num_borrow_and_mean_borrow_time, parse_num_action_borrower_and_investor, parse_ratio_ten, parse_ratio_fifty
]
primary_keys = ['plat_id', 'day']


@show_running_time
def all_achieve(company_info):
    for api, parse_func in zip(total_apis, parse_functions):
        try:
            one_achieve(company_info, api, primary_keys, parse_func)
        except KeyError:
            continue
    mongo_db[config.COL_COMPANY_LIST].update_one({'_id': company_info['plat_id']}, {'$set': {'finished': 1}})

queue = Queue()
# for company_info in companies:
#     queue.put(company_info)


class AchieveWorker(Thread):
    def __init__(self, queue):
        super(AchieveWorker, self).__init__()
        self.queue = queue
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            if self.queue.empty():
                break
            task = self.queue.get()
            all_achieve(task)
            self.queue.task_done()

    def stop(self):
        self.thread_stop = True


if __name__ == '__main__':
    # for _ in range(1):
    #     worker = AchieveWorker(queue)
    #     worker.start()
    # queue.join()
    for company_info in companies:
        try:
            all_achieve(company_info)
        except Exception as e:
            print(company_info['plat_id'], e)
            continue
