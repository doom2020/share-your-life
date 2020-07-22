$(function () {
    $('.allMenu').on('click', function () {
        $(this).children('a').children('span').last().attr('class', 'glyphicon glyphicon-menu-down');
        $(this).children('ul').slideDown();
        $(this).siblings('li').children('a').children('span:last-child').attr('class','glyphicon glyphicon-menu-right');
        $(this).siblings('li').children('ul').slideUp();
        $(this).siblings('li').children('ul').children('li').css('background-color', '#666666');
    });
    $('.menuShow>li').unbind().bind('click', function () {
        $(this).parent('ul').slideDown();
        $(this).css('background-color', '#000000');
        $(this).siblings('li').css('background-color', '#666666');
    })
});