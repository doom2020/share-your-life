$(function () {
    $('#leftSidebar>ul>li').unbind().bind('click', function () {
        // $(this).children('a').children('span').last().attr('class', 'glyphicon glyphicon-menu-down');
        // $(this).siblings('li').children('a').children('span').last().removeAttr('class');
        // $(this).siblings('li').children('a').children('span').last().addClass('glyphicon glyphicon-menu-right');
        // $(this).siblings('li').children('a').children('span').last().attr('class','glyphicon glyphicon-menu-right');
        $(this).children('ul').slideDown().siblings('a').children('span').last().attr('class', 'glyphicon glyphicon-menu-down');
        $(this).siblings('li').children('ul').slideUp().siblings('a').children('span').last().attr('class', 'glyphicon glyphicon-menu-right');
    });
    $('.menuShow>li').unbind().bind('click', function () {
        $(this).parent('ul').slideDown();
        $(this).css('background-color', 'black');
        $(this).siblings('li').css('background-color', '#666666');
    })
});