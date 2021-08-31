// function orderMelons(evt) {
//     evt.preventDefault();
    
//     const formInputs = {
//         'melon_type':$('#melon-type-field').val(),
//         'qty':$('#qty-field').val()
//     };

//     $.post('/order-melons.json', formInputs, (res) => {
//         if (res.code === 'ERROR') {
//             $('#order-status').addClass('order-error');
//         }
//         $('#order-status').html(`${res.code} and ${res.msg}`); 

//     });
// }

// $("#order-form").on('submit', orderMelons);



function playlistRec(evt){
    evt.preventDefault();

    const formInputs = {
        'city':$('#city').val(),
        'state':$('#state').val()
    };

    $.get('/', formInputs, (res) => {
// THINGS AND STUFFS AND THING
        $('#').html()
    });
}

$("#searchbar").on('submit', playlistRec)