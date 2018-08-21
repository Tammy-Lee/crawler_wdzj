# -*- coding: utf-8 -*-
"""
create on 2018-08-21 23:08
author @66492
"""
from lxml import etree

def parse_status(html):
    content = etree.HTML(html)
    company_lis = content.xpath('//ul[@class="terraceList"]/li')
    for li in company_lis:
        wdzj_plat_id = li.xpath('.//a[@class="attention"]/@data-platid')[0]
        name = li.xpath('./div/h2/a/text()')[0]
        try:
            register_time = li.xpath('.//a[@class="itemConLeft"]/div[@class="itemConBox"][4]/text()')[0].split("：")[1]
        except IndexError:
            register_time = None
        try:
            register_location = li.xpath('.//div[@class="itemConBox"][3]/text()')[0].split("：")[1]
        except IndexError:
            register_location = None
        yield {"wdzj_plat_id": wdzj_plat_id, "name": name, "register_time": register_time, "register_location": register_location}
