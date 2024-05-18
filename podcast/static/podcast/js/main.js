$(document).ready(function(){
    $('.pad').fadeOut();

    $('#contact_wrapper').slideUp();
    $('.sp_wrapper').slideUp();

    $('.menu_button').on('click',function(){
        
        $('.menu_button').css('display','none');
        $('.menu_close_button').css('display','block');

        $('.mobile_menu').css('visibility','visible');
        $('.mobile_menu').fadeIn('fast');
        $('.pad').fadeIn();

        

    })
    
    $('.menu_close_button').on('click',function(){
        $('.mobile_menu').fadeOut();
        $('.pad').fadeOut();

        $('.menu_button').css('display','block');
        $('.menu_close_button').css('display','none');
        

    })



    $('#contact_slider').on('click',function(){
        $('#contact_wrapper').slideToggle();
    })

    $('#menu-message').on('click',function(){
        $('#contact_wrapper').slideToggle();
    })

    $('.sp').on('click',function(){
        $('.sp_wrapper').slideToggle();
    })

    $('.menu-sp').on('click',function(){
        $('.sp_wrapper').slideToggle();
    })
    
})