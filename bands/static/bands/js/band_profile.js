function imageDisplay() {
    $('.profile-sm-img').click(function() {
        let clickedImage = $(this).attr('src')
        let mainImage = $('.profile-main-img').attr('src')

        $(this).fadeOut(500, function(){
            $(this).attr('src', mainImage)
            $(this).fadeIn()
        })
        $('.profile-main-img').fadeOut(500, function(){
            $('.profile-main-img').attr('src', clickedImage)
            $('.profile-main-img').fadeIn()
        })

    })
}

$(document).ready(function() {
    imageDisplay()
});
    
