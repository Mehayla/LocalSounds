
function updateWelcome(evt) {
    evt.preventDefault();

    let username = $('.username').val();

    const formData = {
        username:username,
        city:$('.city').val(),
        state:$('.state').val(),
        password:$('.password').val()               
    };

    $.post ('/signup/user', formData, (res)=>{

        if (res['create-status']){
            $('#uwelcome-message').html(`welcome to the neightborhood, ${username}`)}
            // Change this^^^^ to update on the home page?

        else {
            alert('An account with that username already exists. Please try another one.')}

        window.location = res['url'];

    // Have Users pick a color they really like to change some of the features??? 
    // $("blue-changer").on('click', () => {
    // $(p.changes-colors).css('font-color', blue);
    // })

    });
};

$('.newpeople').on('submit', updateWelcome);




function newArtist(evt) {
    evt.preventDefault();

    let aname = $('.aname').val();

    const formData = {
        aname:aname,
        password:$('.password').val(),
        city:$('.city').val(),
        state:$('.state').val(),
        bc_link:$('.bc_link').val(),
        link_1:$('.link_1').val(),
        link_2:$('.link_2').val()               
    };

    $.post ('/signup/artist', formData, (res)=>{

        if (res['create-status']){
            $('#uwelcome-message').html(`welcome to the neightborhood, ${aname}`)}
            // Change this^^^^ to update on the home page?

        else {
            alert('Your information has been updated')}

        window.location = res['url'];
    });
};


$('.newartist').on('submit', newArtist);


// If sign-in == True
    // $('#login-button').remove('sign-up');

// document.querySelector('#login-button').addEventListener('click', (evt) => {
    
//     const button = evt.target;
//     let innerButtonText = button.innerText

//     if (innerButtonText == "Log In") {
//       innerButtonText = "Log Out";
//     } 

//     else if (innerButtonText == "Log Out") {
//         innerButtonText = "Log In";
//         }
    
//     else {
//         innerButtonText = "Oh no we seem to have hit an issue. . . so sorry"
//             }
//     })






        // add .append/.remove here
        // $('#login-button').remove();
        // $("#prompt-1").append("<button id='login-button'>Log In</button>")