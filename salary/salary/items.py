# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SalaryItem(scrapy.Item):
    # define the fields for your item here like:

    information = scrapy.Field()
    salary = scrapy.Field()
    address = scrapy.Field()
    education = scrapy.Field()
    workExperience = scrapy.Field()
    company = scrapy.Field()
