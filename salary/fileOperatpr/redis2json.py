# -*- coding: utf-8 -*-

import json

import redis

from genurl.create_start_urls import lists_detail

pool = redis.ConnectionPool(host="127.0.0.1", password="", db=5)
redis_obj = redis.Redis(connection_pool=pool)

for i in range(0, 5):
    for j in range(0, 5):
        with open(lists_detail[i][j] + "_info.json", "w", encoding="utf-8") as fp:
            for k in redis_obj.lrange(lists_detail[i][j] + "_info", 0, -1):
                json_str = json.dumps(json.loads(k, encoding="utf-8"), ensure_ascii=False)
                fp.write(json_str + "\n")








