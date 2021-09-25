// Change main image by selecting small image
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

// Change band rating to star icons
function starRating() {
    rating = $(".star-rating").each(function() {
        let rating = parseInt($(this).text());

        $(this).empty();
        
        let starRating = $(this).append(
            "<i class='fas fa-star'></i>".repeat(rating)
        )

        return starRating
    });
}

// Set rating range from 1 to 5
function ratingRange() {
    $('input[type=number]').on('mouseup keyup', function () {
        $(this).val(Math.min(5, Math.max(1, $(this).val())));
    });
}
 
$(document).ready(function() {
    imageDisplay()
    starRating()
    ratingRange()
});
    
