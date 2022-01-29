
if (window.location.hostname == "www.google.com"){
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    console.log(domain);
    
    // send query to backend
    fetch('https://esgify.herokuapp.com/esg/' + query)
        .then( response => response.json() )
        .then( response => {
            // todo this??
            console.log("log2");
            document.getElementById('ticker').innerHTML = response.ticker;
            document.getElementById('envRisk').innerHTML = response.esg.environment;
            document.getElementById('socRisk').innerHTML = response.esg.social;
            document.getElementById('govRisk').innerHTML = response.esg.governance;
            document.getElementById('cont').innerHTML = response.esg.controversy;
    } )
}