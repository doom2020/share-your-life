from django.shortcuts import render, redirect


def decorator(func):
    def inner(self, request, *args, **kwargs):
        # 获取当前请求的url路径
        url_path = self.request.path_info
        cookie = self.request.COOKIES.get('c_cookie', None)
        session = self.request.session.get('c_session', None)
        if url_path != '/login/':
            if cookie or session:
                return func(self, request, *args, **kwargs)
            else:
                return redirect('/login/')
        else:
            if cookie or session:
                return redirect('/')
            else:
                return render(request, 'login.html')
    return inner
