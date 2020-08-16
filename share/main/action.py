from django.http import HttpResponse
from main.models import UserInfo


class HomeHandler(object):
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        post_type = self.request.POST.get("post_type")
        home_cool = HomeCool(self.request)
        handle = None
        if post_type and hasattr(home_cool, post_type):
            getattr(home_cool, post_type)
        return handle


class HomeCool(object):
    def __init__(self, request):
        self.request = request


class LoginHandler(object):
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        post_type = self.request.POST.get("post_type")
        login_cool = LoginCool(self.request)
        handle = None
        if post_type and hasattr(login_cool, post_type):
            handle = getattr(login_cool, post_type)
        return handle


class LoginCool(object):
    def __init__(self, request):
        self.request = request

    def check_account(self):
        ret_dict = {'ret': 0, 'data': ''}
        try:
            account = self.request.POST.get('account')
            user_info_objs = UserInfo.objects.filter(name=account, is_delete=0)
            if not user_info_objs:
                ret_dict['ret'] = 1
        except Exception as e:
            ret_dict['ret'] = 2
            ret_dict['data'] = e
            print(e)
            return ret_dict
        return ret_dict

    def login(self):
        ret_dict = {'ret': 0, 'data': ''}
        account = self.request.POST.get('account')
        password = self.request.POST.get('password')
        try:
            user_info_obj = UserInfo.objects.get(name=account, password=password, is_delete=0)
            if user_info_obj:
                res = HttpResponse()
                res.set_cookie("c_cookie", "account", expires=60*60)
                session_dict = {"account"}
                self.request.session["c_session"] = {"account": account, 'password': password}
        except Exception as e:
            ret_dict['ret'] = 1
            return ret_dict
        return ret_dict


class RegisterHandler(object):
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        post_type = self.request.POST.get("post_type")
        register_cool = RegisterCool(self.request)
        handle = None
        if post_type and hasattr(register_cool, post_type):
            handle = getattr(register_cool, post_type)
        return handle


class RegisterCool(object):
    def __init__(self, request):
        self.request = request
        self.ret_dict = {'ret': 0, 'data': ''}

    def register(self):
        account = self.request.POST.get('account')
        phone = self.request.POST.get('phone')
        email = self.request.POST.get('email')
        upwd = self.request.POST.get('upwd')
        cpwd = self.request.POST.get('cpwd')
        gender = self.request.POST.get('gender')
        # picture_file = self.request.FILES['picture']
        print("account: %s, phone: %s, email: %s, upwd: %s, cpwd: %s, gender: %s" % (account, phone,\
               email, upwd, cpwd, gender))

        return self.ret_dict
