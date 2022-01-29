
if (window.location.hostname == "www.google.com"){
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    alert("query: " + query);


    // send query to backend
    fetch('{.env.backend_url}/{query}')
        .then( response => response.json() )
        .then( response => {
            // todo this??
            document.data = response
    } )
}