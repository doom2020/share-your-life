import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from public.auth import decorator
from .action import FreeProxyHandler


class FreeProxy(View):
    @decorator
    def get(self, request, *args, **kwargs):
        session = self.request.session.get('c_session')
        user = session['account']
        if not user:
            user = '未登录'
        return render(request, 'proxy/proxy.html', locals())

    @decorator
    def post(self, request, *args, **kwargs):
        free_proxy_handler = FreeProxyHandler(request)
        op_handle = free_proxy_handler.get_handler()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))
