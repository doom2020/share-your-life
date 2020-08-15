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

    $('#example').DataTable( {
        "paging":   true,
        "ordering": false,
        "searching": false
    } );
    // 高级搜索显示隐藏
    $('#powerSearchToggle').unbind().bind('click', function () {
        $('#powerSearchDiv').slideToggle();
    });

    $("#logout").unbind().bind('click', function () {
        $.ajax({
            url: './',
            data: {"post_type": "logout"},
            type: 'post',
            dataType: 'json',
            async: 'true',
            success(data, xhr, status) {
                const ret = data.ret;
                const info = data.data;
            }
        })
    })

});