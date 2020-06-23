

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

    def get_proxy(self):
        pass
