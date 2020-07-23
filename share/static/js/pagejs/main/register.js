$(function () {
    $("#btnRegister").unbind().bind('click', function () {
        return true
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