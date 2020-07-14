from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class Home(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('this is home page for get')

    def post(self, request, *args, **kwargs):
        return HttpResponse('this is home page for post')


class Login(View):

    def get(self, request, *args, **kwargs):
        # return HttpResponse('this is login page for get')
        return render(request, 'proxy/proxy.html', locals())

    def post(self, request, *args, **kwargs):
        return HttpResponse('this is login page for post')


class Register(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('this is register page for get')

    def post(self, request, *args, **kwargs):
        return HttpResponse('this is register page for post')


