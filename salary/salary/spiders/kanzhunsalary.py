# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import TextResponse
from scrapy_redis.spiders import RedisCrawlSpider

from genurl.job_city import job_city
from salary.items import SalaryItem

class salary_startSpider(RedisCrawlSpider):
    name = 'kanzhunsalary'
    allowed_domains = ['liepin.com']
    redis_key = job_city +"salary:start_urls"

    def parse(self, response):
        assert isinstance(response, TextResponse)#代码自动补全
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()

        salary = response.xpath("//ul[@class='sojob-list']/li/div")
        for each_salary in salary:
            item = SalaryItem()
            try:
                # item['information'] = each_salary.xpath("./@title").extract()[0]
                item['salary'] = each_salary.xpath("./div[@class='job-info']/p[1]/span[1]/text()").extract_first()
                item['address'] = each_salary.xpath("./div[@class='job-info']/p[1]/a[1]/text()").extract_first()
                item['education'] = each_salary.xpath("./div[@class='job-info']/p[1]/span[2]/text()").extract_first()
                item['workExperience'] = each_salary.xpath("./div[@class='job-info']/p[1]/span[3]/text()").extract_first()
                item['company'] = each_salary.xpath("./div[@class='company-info nohover']/p[1]/a/text()").extract_first()
            except IndexError:
                print("wrong")
                pass
            yield item