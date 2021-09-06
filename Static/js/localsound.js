
function updateWelcome(evt) {
    evt.preventDefault();

    const formData = {
        name:$('.name').val(),
        city:$('.city').val()
    };

    $.get ('/signup', formData, (res)=>{
        $('#welcome-message').html(res);
    });
});

$('.newpeople').on('submit', updateWelcome);