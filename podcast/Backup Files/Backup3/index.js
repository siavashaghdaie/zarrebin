$(document).ready(function(){
    $('.pad').fadeOut();
    $('.castbox').slideUp();
    $('#contact_wrapper').slideUp();
    $('.sp_wrapper').slideUp();


    $('.menu_button').on('click',function(){
        
        $('.mobile_menu').fadeIn();
        $('.pad').fadeIn();
        $('.mobile_menu').css('visibility','visible');
        

        $('.menu_close_button').css('display','block');
        $('.menu_button').css('display','none');

    })
    
    $('.menu_close_button').on('click',function(){
        $('.mobile_menu').fadeOut();
        $('.pad').fadeOut();

        $('.menu_close_button').css('display','none');
        $('.menu_button').css('display','block');

    })

    

    

    $('#last_episode_listen').on('click',function(){
        $('.castbox').slideToggle();
    })

    $('#contact_slider').on('click',function(){
        $('#contact_wrapper').slideToggle();
    })

    $('.sp_title').on('click',function(){
        $('.sp_wrapper').slideToggle();
    })
    
})