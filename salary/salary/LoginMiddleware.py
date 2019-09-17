import json

import redis


class LoginMiddleware(object):
    def __init__(self):
        self.client = redis.StrictRedis()

    def process_request(self, request, spider):
        if spider.name == "":
            cookies = json.loads(self.client.lpop('cookies').decode())
            request.cookies = cookies