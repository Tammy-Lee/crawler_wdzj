# -*- coding: utf-8 -*-
"""
create on 2018-08-19 17:02
author @66492
"""
API_COMPANY_STATUS = {
    "url": "https://www.wdzj.com/dangan/search?filter={type}&currentPage={page}",
    "method": "GET",
    "collection": "company_status"
}
API_ALL_COMPANIES = {
    "url": "https://www.wdzj.com/wdzj/html/json/dangan_search.json",
    "method": "GET",
    "collection": "company_list"
}
API_PROBLEM = {
    "url": "https://shuju.wdzj.com/problem-list-all.html?year={year}",
    "method": "GET",
    "collection": "company_list"
}
API_SHUTDOWN = {
    "url": "https://shuju.wdzj.com/shutdown-list-all.html?year={year}",
    "method": "GET",
    "collection": "company_list"
}
# 平台成交数据
API_PLAT_CUSTOM = "https://shuju.wdzj.com/plat-data-custom.html"
API_PLAT_SOURCE = {
    "url": API_PLAT_CUSTOM,
    "method": "POST",
    "formdata": {
        "type": 1,
        "shujuDate": ""
    },
    "collection": "company_list"
}
API_PLAT_INFO = "https://shuju.wdzj.com/plat-info-target.html"
# 基本数据
# 成交量
API_VOLUME = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 1,
        "target2": 0
    },
    "collection": "daily"
}
# 参考收益率
API_RETURN_RATE = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 2,
        "target2": 0
    },
    "collection": "daily"
}
# 投资人数分级
API_INVESTOR_NUM_RANK = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 3,
        "target1": 16,
        "target2": 1
    },
    "collection": "monthly"
}
# 借款人数分级
API_BORROWER_NUM_RANK = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 3,
        "target1": 16,
        "target2": 2
    },
    "collection": "monthly"
}
# 不同期限标的参考收益率
API_RETURN_RATE_DIFF = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 3,
        "target1": 17,
        "target2": 1
    },
    "collection": "monthly"
}
# 不同期限标的的满标用时
API_COMPLETE_TIME_DIFF = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 3,
        "target1": 17,
        "target2": 2
    },
    "collection": "monthly"
}
# 数据VS
# 投资人数VS借款人数
API_NUM_INVESTOR_VS_BORROWER = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 5,
        "target2": 6
    },
    "collection": "daily"
}
# 人均投资金额VS人均借款金额
API_MEAN_AMOUNT_INVESTOR_VS_BORROWER = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 7,
        "target2": 8
    },
    "collection": "daily"
}
# 新投资人数VS老投资人数
API_NUM_INVESTOR_NEW_VS_OLD = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 19,
        "target2": 20
    },
    "collection": "daily"
}
# 新投资人总额VS老投资人总额
API_AMOUNT_INVESTOR_NEW_VS_OLD = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 21,
        "target2": 22
    },
    "collection": "daily"
}
# 平均借款期限VS行业平均期限
API_BORROW_TIME_MEAN_PLATFORM_VS_INDUSTRY = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 10,
        "target2": 23
    },
    "collection": "daily"
}
# 深度数据
# 借款标数和平均借款期限
API_NUM_BORROW_AND_MEAN_BORROW_TIME = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 9,
        "target2": 10
    },
    "collection": "daily"
}
# 待还借款人数和待收投资人数
API_NUM_ACTION_BORROWER_AND_INVESTOR = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 1,
        "target1": 12,
        "target2": 11
    },
    "collection": "daily"
}
# 前十大借款人待还金额占比和前十大土豪待收金额占比
API_RATIO_TEN = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 3,
        "target1": 18,
        "target2": 1
    },
    "collection": "monthly"
}
# 前五十大借款人待还金额占比和前五十大土豪待收金额占比
API_RATIO_FIFTY = {
    "url": API_PLAT_INFO,
    "method": "POST",
    "formdata": {
        "wdzjPlatId": 0,
        "type": 3,
        "target1": 18,
        "target2": 2
    },
    "collection": "monthly"
}
