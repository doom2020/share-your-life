$(function () {
    $('#example').DataTable( {
        "paging":   true,
        "ordering": false,
        "searching": false
    } );
    // 高级搜索显示隐藏
    $('#powerSearchToggle').unbind().bind('click', function () {
        $('#powerSearchDiv').slideToggle();
    });

});