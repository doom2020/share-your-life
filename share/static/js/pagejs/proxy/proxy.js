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
    // 自定义一些方法迭代使用
    // methods 1
    getTableData = function(flag, filter_condition){
        $('#tableId').DataTable( {
            serverSide: true,
            ajax: {
              "url": '/proxy/',
              'type': 'POST',
              "data": {"post_type": "get_table_data", "flag": flag, "filter_condition": filter_condition}
            },
            columns: [
                {data: 'ip'},
                {data: 'port'},
                {data: 'anonymous'},
                {data: 'type'},
                {data: 'location'},
                {data: 'response_speed'},
                {data: 'format_time'},
                {data: 'score'}
            ],
            columnDefs: [
                {
                    "targets": 3,
                    "render": function (data, type, row, meta) {
                        if(row.type === 'HTTP'){
                            return '<span style="font-size: 13px;background-color: #66CC00;color: #ffffff;text-align: center">HTTP</span>'
                        }else {
                            return '<span style="font-size: 13px;background-color: #ffCC00;color: #ffffff;text-align: center">HTTPS</span>'
                        }
                    }
                },
                {
                    "targets": 7,
                    "render": function (data, type, row, meta) {
                        if(row.score >= 90){
                            return '<span style="font-size: 13px;background-color: #990000;color: #ffffff;text-align: center">' + row.score + '</span>'
                        }
                        else if(80 <= row.score < 90){
                            return '<span style="font-size: 13px;background-color: #CCFFBB;color: #ffffff;text-align: center">' + row.score + '</span>'
                        }
                        else if(60 <= row.score < 80){
                            return '<span style="font-size: 13px;background-color: #CCFFBB;color: #ffffff;text-align: center">' + row.score + '</span>'
                        }else {
                            return '<span style="font-size: 13px;background-color: #CCFFBB;color: #ffffff;text-align: center">' + row.score + '</span>'
                        }
                    }
                }
            ],
            sInfo: false,
            searching: false,
            lengthMenu: [10, 50, 100, 500],
            ordering: false,
            destroy: true,
            "sPaginationType": "extStyle"
        } );
    };

    getTableData('', '');

    // 普通搜索
    $("#btnBasicSearch").unbind().bind('click', function () {
        var input_value = $('#basicSearchValue').val();
        // if(input_value){
        //     var filter_condition = JSON.stringify({"input_value": input_value});
        //     getTableData('basic_search', filter_condition);
        //
        // }
    });

    // 下载
    $("#downloadBtn").unbind().bind('click', function () {
       return true;
    });

    // 刷新
    $("#refreshBtn").unbind().bind('click', function () {
        getTableData('', '');
    });

    // 显示高级搜索
    $("#powerSearchToggle").unbind().bind('click', function () {
        $('#powerSearchDiv').slideToggle();
    });

    // 高级搜索
    $("#powerSearch").unbind().bind('click', function () {
        return true;
    });

    // 清除表单元素
    $("#clearForm").unbind().bind('click', function () {
        return true;
    })


});