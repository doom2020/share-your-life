import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .action import FreeProxyHandle


class FreeProxy(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'proxy/proxy.html', locals())

    def post(self, request, *args, **kwargs):
        free_proxy_handle = FreeProxyHandle(request)
        op_handle = free_proxy_handle.get_handle()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))
