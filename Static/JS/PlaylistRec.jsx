// "use strict";

// // const()

// $('.searchbar').on('click',() => {
//     location.href="playlist"
        // get_artists from CRUD???
// }
// );

// PUT ALL OF THE FUNCTIONS/CHANGES TO HTML YOU WILL WANT HERE
// THEN FOLLOW WITH ReactDOM.render(<tag you want it rendered in></tag>, document.querySelector('#id'))
// MAKE A REAUSABLE COMPNENT HERE FOR THE PLAYLIST RECOMENDATIONS???

function Hello(){
    <h3>Listen to the sound scape</h3>
};

// function search(props){
//     const[currentState, newState] = React.useState(props.initial[0]) OR JUST 0
//     return(<div>Stuff and Things</div>)
// };

function search(){
    function playlist_rec(){
        // The function that gives the artist info from API
    }
    return (
        <submit onSubmit={playlist_rec}>

        </submit>
    )
};

React.useEffect(()=>{
    fetch("/search")
        .then((get_artist)=> Response.json(1)
        .then((result)=>{
            setFruits(result);
        }));
},[]);

ReactDOM.render(<playlist/>, document.querySelector('#playlist'))