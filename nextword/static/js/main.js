(function(jQuery) {


    $('.submit-button').click(search);
    $(document).keypress(function(e) {
        if(e.which == 13 && $('.search-text').is(':focus')) { // Enter
            console.log("clicked");
            search();
        }
    });

    function search() {
        if ($('.submit-button').hasClass('disabled')) {return;}
        $('.submit-button').addClass('disabled');

        $('.result').remove();
        var text = $('.search-text').val();
        var ignore = $('#ignore').is(':checked');
        console.log("This is the ignore value:");
        console.log(ignore);

        $.get('/find?pattern=' + text + '&ignore=' + ignore, function(data) {
            console.log("Success! Here is the data");
            console.log(data);

            $('.submit-button').removeClass('disabled');
            $('.no-results').hide();
            $('.results').show();

            // Animate search bar up
            $('body').animate({paddingTop: '30px'});

            // Display the results
            for (var i=0; i<data.length; i++) {
                var result = data[i][0].join(" ");
                if (result.length == 0) {
                    $('no-results').show();
                } else {
                var count = data[i][1]
                    $('.results').append(
                        "<div class='result'>" +
                            result +
                            "<div class='count'>" + count + "</div>" +
                        "</div>"
                    );
                }
            }
        });
    };

})($);
