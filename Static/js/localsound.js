
function updateWelcome(evt) {
    evt.preventDefault();

    console.log('Front-end is hard')

    const formData = {
        username:$('.username').val(),
        city:$('.city').val(),
        state:$('.state').val(),
        password:$('.password').val()               
    };

    $.post ('/signup/user', formData, (res)=>{
        $('#welcome-message').html(`${res.name}`);
    });
};

$('.newpeople').on('submit', updateWelcome);