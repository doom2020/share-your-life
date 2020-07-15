$(function () {
    $('#example').DataTable( {
        "paging":   false,
        "ordering": false,
        "searching": false
    } );

    $('#powerSearchToggle').unbind().bind('click', function () {
        $('#powerSearchDiv').slideToggle();
    })
});