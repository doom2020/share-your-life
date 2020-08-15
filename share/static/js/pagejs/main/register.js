$(function () {
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
    $("#btnRegister").unbind().bind('click', function () {
        var account = $("#account").val();
        var phone = $("#phone").val();
        var email = $("#email").val();
        var upwd = $("#upwd").val();
        var cpwd = $("#cpwd").val();
        var gender = $("input:radio:checked").val();
        if($("#picture").val() != ""){
            var picture = $("#picture").prop('files')[0];
        }else {
            var picture = '';
        }
        console.log(account, phone, email, upwd, cpwd, gender, picture);
        if(account && upwd && cpwd && gender){
            $.ajax({
                url: './',
                data: {"post_type": 'register', "account": account, "phone": phone, "email": email, "upwd": upwd,
                        "cpwd": cpwd, "gender": gender, "picture": picture},
                type: 'post',
                dataType: 'json',
                async: 'true',
                success: function (data, status, xhr) {
                    var result = data.ret;
                    var info = data.data;
                    return true;
                }
            })
        }
    });

    // 验证用户名
    $("#account").unbind().bind('blur', function () {
        var account = $(this).val();
        if(account.length < 3 || account.length > 6){
            $(this).siblings('span').addClass('errBackgroundColor');
            $(this).addClass('errBorder');
        }else {
            $.ajax({
            });
            $(this).siblings('span').removeClass('errBackgroundColor');
            $(this).removeClass('errBorder');
        }
    });

    // 验证手机号
    $("#phone").unbind().bind('blur', function () {
        var phone = $(this).val();
    });

    // 验证email
    $("#email").unbind().bind('blur', function () {
        var email = $(this).val();
    });

    // 验证密码
    $("#upwd").unbind().bind('blur', function () {
        var upwd = $(this).val();
    });

    // 验证确认密码
    $("#cpwd").unbind().bind('blur', function () {
        var cpwd = $(this).val();
    })
});