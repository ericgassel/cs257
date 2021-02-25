/*
 * webapp.js
 * Eric Gassel and Sam Gloss
 * February 24 2021
 *
 */

window.onload = initialize;

function initialize() {
    LoadVertNavBar();

    var teams_button = document.getElementById('teams_button');
    teams_button.onclick = onTeamsButton;
}

function LoadVertNavBar(){

    var vertical_navbar = document.getElementById('vertical-navbar');
    var list_body = '<li><a>Atlanta Hawks</a></li><li><a>Boston Celtics</a></li><li><a>Brooklyn Nets</a></li>';
    vertical_navbar.innerHTML = list_body;

}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function onTeamsButton(){

    var ppg = document.getElementById('ppg-list');
    var ast = document.getElementById('ast-list');
    var url = getAPIBaseURL() + '/teams/ppg/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(ppg_list) {
        var listBody = '';
        for (var k = 0; k < ppg_list.length; k++) {
            var ppg_team = ppg_list[k];
            listBody += '<li>' + ppg_team['name']
                      + ', ' + ppg_team['points'];
                      + '</li>\n';
        }

    
        ppg.innerHTML = listBody;
        
    })

    .catch(function(error) {
        console.log(error);
    });

    url = getAPIBaseURL() + '/teams/apg/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(apg_list) {
        var listBody = '';
        for (var k = 0; k < apg_list.length; k++) {
            var apg_team = apg_list[k];
            listBody += '<li>' + apg_team['name']
                      + ', ' + apg_team['assists'];
                      + '</li>\n';
        }

        
        
        ast.innerHTML = listBody;
        
    })

    .catch(function(error) {
        console.log(error);
    });

}