import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from main.action import LoginHandler, HomeHandler, RegisterHandler
from public.auth import decorator


class Home(View):
    @decorator
    def get(self, request, *args, **kwargs):
        session = self.request.session.get('c_session')
        user = session['account']
        if not user:
            user = '未登录'
        return render(request, 'main/main.html', locals())

    @decorator
    def post(self, request, *args, **kwargs):
        home_handler = HomeHandler(request)
        op_handle = home_handler.get_handler()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))


class Login(View):
    @decorator
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        login_handler = LoginHandler(request)
        op_handle = login_handler.get_handler()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))


class Register(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html', locals())

    def post(self, request, *args, **kwargs):
        register_handler = RegisterHandler(request)
        op_handle = register_handler.get_handler()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))


