# -*- coding: utf-8 -*-
"""
create on 2018-08-21 23:32
author @66492
"""
from wdzj.apis import API_COMPANY_STATUS
from wdzj.demo.utils import make_response, update_one, show_running_time
from wdzj.demo.parser.status import parse_status

def map_status(type):
    status_map = {
        "e1": "normal",
        "e2": "停业或转型",
        "e3": "问题平台"
    }
    return status_map.get(type, None)


@show_running_time
def one_page(type, page):
    response = make_response(API_COMPANY_STATUS, timeout=None, type=type, page=page)
    html = response.content.decode("utf-8")
    data = parse_status(html)
    for item in data:
        item["status"] = map_status(type)
        # print(item)
        update_one(item, ["wdzj_plat_id"], API_COMPANY_STATUS["collection"])


def all_page():
    pages = [("e2", 97), ("e3", 93)]
    for type, total_page in pages:
        for page in range(1, total_page+1):
            print(type, page)
            one_page(type, str(page))


if __name__ == '__main__':
    # one_page("e1", "1")
    all_page()
