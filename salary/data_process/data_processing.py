# -*- coding: utf-8 -*-

import json

import redis

from genurl.create_start_urls import lists_detail

#平均薪资
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

pool = redis.ConnectionPool(host="127.0.0.1", password="", db=5)
redis_obj = redis.Redis(connection_pool=pool)

dicts_detail = [[] for i in range(5)]
[dicts_detail[i].append([]) for i in range(5) for j in range(5)]

for i in range(0, 5):
    for j in range(0, 5):
        for k in redis_obj.lrange(lists_detail[i][j] + "_info", 0, -1):
            # json_str = json.dumps(json.loads(k, encoding="utf-8"), ensure_ascii=False)
            dict_tmp = {}
            dict_tmp = json.loads(k, encoding="utf-8")
            if dict_tmp["salary"] !="面议":
                lists = []
                lists = list(map(int, dict_tmp["salary"].replace("万", "").split("-")))
                lists = [round(x/12, 2) for x in lists]

                dict_tmp["salary"] = averagenum(lists)
                dicts_detail[i][j].append(dict_tmp)









