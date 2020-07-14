$(function () {
    // 自定义一些方法迭代使用
    // methods 1
    var getTableData = function(flag, filter_condition){
        $('#tableId').DataTable( {
        "paging":   false,
        "ordering": false,
        "searching": false
        } );
    };

    getTableData('', '');

    // 普通搜索
    $("#basicSearch").unbind().bind('click', function () {
        var input_value = $('#keyWords').val();
        if(input_value){
            var filter_condition = JSON.stringify({"input_value": input_value});
            getTableData('normal_search', filter_condition);

        }
    });

    // 下载
    $("#downloadTable").unbind().bind('click', function () {
       return true;
    });

    // 刷新
    $("#refreshPage").unbind().bind('click', function () {
        getTableData('', '');
    });

    // 显示高级搜索
    $("#toggleForm").unbind().bind('click', function () {
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