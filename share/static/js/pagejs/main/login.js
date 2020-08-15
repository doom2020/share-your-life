$(function () {
    // csrf token
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = $("[name=csrfmiddlewaretoken]").val();
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // 1.验证用户名
    $("#account").unbind().bind('blur', function () {
        const account = $(this).val();
        if(account){
            $.ajax({
                url: '/login/',
                data: {"post_type": "check_account", "account": account},
                type: 'post',
                dataType: 'json',
                async: 'true',
                success(data, xhr, status) {
                    const ret = data.ret;
                    const info = data.data;
                    if(!ret){
                        alert('用户名可用');
                    }
                    else if(ret === 1){
                        alert('此用户不存在');
                    }
                    else if(ret === 2){
                        alert(info);
                    }
                }
            })
        }
    });

    // 登录
    $("#btnLogin").unbind().bind('click', function () {
        const account = $("#account").val();
        const password = $("#upwd").val();
        if(account && password){
            $.ajax({
                url: '/login/',
                data: {"post_type": "login", "account": account, "password": password},
                type: 'post',
                dataType: 'json',
                async: 'true',
                success(data, xhr, status) {
                    const ret = data.ret;
                    const info = data.data;
                    if(!ret){
                        $("#errInfo").val('');
                        // alert('恭喜登录成功');
                        setTimeout(function () {
                            window.location.href='/'
                        }, 5)
                    }
                    else if(ret === 1){
                        $("#errInfo").text('The Account or Password is error').css('color', 'red');
                        alert('用户名或密码不正确');
                    }
                }
            })
        }
    })
});