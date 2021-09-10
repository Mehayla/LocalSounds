
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

        // Check which page it is with the res

        // if res == '/login'
        console.log('* * * * * * * *')
        console.log(res)
        console.log('* * * * * * * *')
        $('#welcome-message').text(`welcome to the neightborhood, ${res.username}`);

    // An else statement?
        // $.post("/signup/user", userAlert  => {
        //     alert(f"{username} already exits. Now redirecting to sign-in");

    // Have Users pick a color they really like to change some of the features??? 
    // $("blue-changer").on('click', () => {
    // $(p.changes-colors).css('font-color', blue);
    // })


    });
};

$('.newpeople').on('submit', updateWelcome);


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