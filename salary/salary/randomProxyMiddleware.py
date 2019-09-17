import random
import scrapy
import logging
class MyUserProxyMiddleware(object):
    proxy_list=[
        "http://163.125.221.127:8118",
        "http://112.111.77.163:9999",
        "http://121.232.194.146:9000"]
    def process_request(self,request,spider):
        # if not request.meta['proxies']:
        request.meta['proxy'] = random.choice(self.proxy_list)

