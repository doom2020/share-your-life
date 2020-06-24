import urllib.request
import random
import time
from xml import etree


from variable import AGENT_LIST


class FreeProxyHandle:
    def __init__(self, request):
        self.request = request

    def get_handle(self):
        post_type = self.request.POST.get('post_type')
        free_proxy_cool = FreeProxyCool(self.request)
        handle = None
        if post_type and hasattr(free_proxy_cool, post_type):
            handle = getattr(free_proxy_cool, post_type)
        return handle


class FreeProxyCool:
    def __init__(self, request):
        self.request = request

    def func1(self):
        pass


class GetFreeProxy(object):
    def __init__(self):
        self.base_url = 'https://www.kuaidaili.com/free/inha'
        self.retry_count = 10
        self.timeout = 15

    def get_index_page(self):
        # 1.use proxy
        # proxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:8080'})
        # opener = urllib.request.build_opener(proxy_handler)
        # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        # opener.open(self.base_url, timeout=self.timeout)
        # 2.use proxy
        # headers = random.choice(AGENT_LIST)
        # req = urllib.request.Request(self.base_url, headers=headers)
        # proxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:8080'})
        # opener = urllib.request.build_opener(proxy_handler)
        # opener.open(req, timeout=self.timeout)
        # 3.no use proxy
        headers = random.choice(AGENT_LIST)
        req = urllib.request.Request(self.base_url, headers=headers)
        response, html = None, None
        while True:
            if self.retry_count <= 0:
                print('页面请求异常')
                return html
            try:
                response = urllib.request.urlopen(req, timeout=self.timeout)
                break
            except Exception as e:
                print(e)
                # 递归调用
                self.retry_count -= 1
                time.sleep(random.choice(1, 3))
                self.get_index_page()
        if response:
            html = response.read().decode('utf-8')
        return html

    def get_all_proxy(self):
        html = self.get_index_page()
        html = etree.HTML(html)
        result = html.xpath()





