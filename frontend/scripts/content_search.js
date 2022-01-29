
if (window.location.hostname == "www.google.com"){
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    alert("query: " + query);

    
    // send query to backend
    fetch('{.env.backend_url}/{query}')
        .then( response => response.json() )
        .then( response => {
            // todo this??
            document.getElementById('ticker').innerHTML = response.ticker;
            document.getElementById('envRisk').innerHTML = response.esg.environment;
            document.getElementById('socRisk').innerHTML = response.esg.social;
            document.getElementById('govRisk').innerHTML = response.esg.governance;
            document.getElementById('cont').innerHTML = response.esg.controversy;
    } )
}