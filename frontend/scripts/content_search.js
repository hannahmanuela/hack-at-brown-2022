const urlParams = new URLSearchParams(window.location.search);
const query = urlParams.get('q');
alert("query: " + query);


// send query to backend
fetch('{.env.backend_url}/{query}')
    .then( response => response.json() )
    .then( response => {
        // send response from backend to background

        /*
        var msg = {};
        msg.sender = "content_search";
        msg.receiver = "background"; // keep this? 
        msg.destination = "popup";

        chrome.runtime.sendMessage(msg, function(response) {
            console.log(response.received_by.concat(" heard me."));
        });
        */
} );