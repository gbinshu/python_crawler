import json

import redis

from genurl.create_start_urls import lists_detail

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

pool = redis.ConnectionPool(host="127.0.0.1", password="", db=3)
redis_obj = redis.Redis(connection_pool=pool)
sla_dict = {}

for i in range(0, 5):
    for j in range(0, 5):
        with open("D:\Desktop\实训项目\猎聘爬取文件\\" + lists_detail[i][j] + "_info.txt", 'r+', encoding='utf-8') as f:
            f = f.readlines()
            for line in f:
                slist = line.split("_")
                sla_dict["salary"] = slist[0]
                sla_dict["address"] = slist[1]
                sla_dict["education"] = slist[2]
                sla_dict["workExperience"] = slist[3]

                if sla_dict["salary"] != "面议":
                    lists = []
                    lists = list(map(int, sla_dict["salary"].replace("万", "").split("-")))
                    lists = [round(x / 12, 2) for x in lists]
                    sla_dict["salary"] = averagenum(lists)
                    # print(sla_dict)
                    redis_obj.lpush(lists_detail[i][j] + "_info", json.dumps(sla_dict, ensure_ascii=False))

                # redis_obj.lpush(lists_detail[i][j] + "_info", json.dumps(sla_dict, ensure_ascii=False))
                sla_dict = {}
