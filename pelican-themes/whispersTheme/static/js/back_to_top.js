$(document).ready(function(){
    // show or hide sticky button
        $(window).scroll(function(){
                if ($(this).scrollTop() > 200) {
                    $('.go-top').fadeIn(200);
                }
                else
                {
                    $('.go-top').fadeOut(200);
                }
            });
           $('.go-top').click(function(event){
            event.preventDefault();
            $('html, body').animate({scrollTop: 0}, 300);
           })
           });