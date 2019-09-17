# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from genurl.create_start_urls import redis_obj
from genurl.job_city import job_city


class SalaryPipeline(object):
    def process_item(self, item, spider):
        item = dict(item)
        json_str = json.dumps(item, ensure_ascii=False)
        with open(job_city +"_info.json", "a", encoding="utf-8") as fp:
            salary = json_str + "\n"
            fp.write(salary)
        redis_obj.rpush(job_city + "salary:information", json_str)

        # with open(job_city +"_info.txt", "a", encoding="utf-8") as fp:
        #     salary = item["information"] + "\n"
        #     fp.write(salary)

