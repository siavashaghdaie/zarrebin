$(document).ready(function(){

    
    $('.mobile_menu_close').on('click',function(){
        $('.mobile_menu').css('display','block');
        $('.mobile_menu').fadeToggle();
    })

    $('.menu_button').on('click',function(){
        $('.mobile_menu').fadeToggle();
    })
    
})