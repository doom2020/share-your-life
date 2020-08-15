import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.
from main.action import LoginHandler, HomeHandler, RegisterHandler
from public.auth import decorator

class UserInfo(View):
    def get_user_name(self, request, *args, **kwargs):
        session = self.request.session.get('c_session')
        user = session['account']
        return user


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
        op_handler = home_handler.get_handler()
        ret_dict = op_handler()
        return HttpResponse(json.dumps(ret_dict))


class Login(View):
    @decorator
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        login_handler = LoginHandler(request)
        op_handler = login_handler.get_handler()
        ret_dict = op_handler()
        return HttpResponse(json.dumps(ret_dict))


class Register(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html', locals())
        # return HttpResponse('this is register page for get')

    def post(self, request, *args, **kwargs):
        register_handler = RegisterHandler(request)
        op_handler = register_handler.get_handler()
        ret_dict = op_handler()
        return HttpResponse(json.dumps(ret_dict))


