chrome.storage.local.get("ticker", function(data) {
    if(typeof data.ticker == "undefined") {
      document.getElementById('ticker').innerHTML = "undef";
    } else {
      document.getElementById('ticker').innerHTML = data.ticker;
    }
});

chrome.storage.local.get("envRisk", function(data) {
    if(typeof data.envRisk == "undefined") {
      document.getElementById('envRisk').innerHTML = "undef";
    } else {
      document.getElementById('envRisk').innerHTML = data.envRisk;
    }
});

chrome.storage.local.get("socRisk", function(data) {
    if(typeof data.socRisk == "undefined") {
      document.getElementById('socRisk').innerHTML = "undef";
    } else {
      document.getElementById('socRisk').innerHTML = data.socRisk;
    }
});

chrome.storage.local.get("govRisk", function(data) {
    if(typeof data.govRisk == "undefined") {
      document.getElementById('govRisk').innerHTML = "undef";
    } else {
      document.getElementById('govRisk').innerHTML = data.govRisk;
    }
});

chrome.storage.local.get("cont", function(data) {
    if(typeof data.cont == "undefined") {
      document.getElementById('cont').innerHTML = "undef";
    } else {
      document.getElementById('cont').innerHTML = data.cont;
    }
});

chrome.storage.local.get("totRisk", function(data) {
    if(typeof data.totRisk == "undefined") {
      document.getElementById('totRisk').innerHTML = "undef";
    } else {
      document.getElementById('totRisk').innerHTML = data.totRisk;
    }
});
