
const urlParams = new URLSearchParams(window.location.search);
const query = urlParams.get('q');

chrome.storage.local.set({ticker: "N/A"})
chrome.storage.local.set({envRisk: 0})
chrome.storage.local.set({socRisk: 0})
chrome.storage.local.set({govRisk: 0})
chrome.storage.local.set({cont: 0}) 
chrome.storage.local.set({totRisk: 0}) 

// send query to backend
fetch('https://esgify.herokuapp.com/esg/' + query)
    .then( response => response.json() )
    .then( response => {
        chrome.storage.local.set({ticker: response.ticker})
        chrome.storage.local.set({envRisk: response.esg.environment})
        chrome.storage.local.set({socRisk: response.esg.social})
        chrome.storage.local.set({govRisk: response.esg.governance})
        chrome.storage.local.set({cont: response.esg.controversy}) 
        total_esg = response.esg.social + response.esg.environment + response.esg.governance
        chrome.storage.local.set({totRisk: total_esg}) 

        const tok_name = response.name.split(" ");
        search_url = "https://www.google.com/search?q=";
        for (let i = 0; i < tok_name.length; i++) {
            search_url.concat(tok_name[i] + "+")
        }
        search_url = search_url + "sustainability";
        console.log(search_url);
        chrome.storage.local.set({search_url: search_url})
} )
