
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

            const tok_name = response.name.split(" ");
            search_url = "https://www.google.com/search?q=";
            for (let i = 0; i < length(tok_name); i++) {
                search_url.concat(tok_name[i] + "+")
            }
            search_url = search_url + "sustainability";
            console.log(search_url);
            document.getElementById('newSearch').setAttribute('href', search_url);
    } )
}