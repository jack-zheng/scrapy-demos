import random

class RandomUserAgentMiddleWare:
    def process_request(self, request, spider):
        ua = random.choice(spider.settings.get("USER_AGENT_LIST"))
        request.headers["User-Agent"] = ua

class CheckAgentMiddleWare:
    def process_response(self, request, response, spider):
        print("*"*10 + "agent" + "*"*10)
        print(request.headers["User-Agent"])
        return response