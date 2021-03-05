/*
 * webapp.js
 * Eric Gassel and Sam Gloss
 * February 24 2021
 *
 */

window.onload = initialize;

function initialize() {
    LoadVertNavBar();

    var players_button = document.getElementById('players_button');
    players_button.onclick = onPlayersButton;

    onPlayersButton();

    var teams_button = document.getElementById('teams_button');
    teams_button.onclick = onTeamsButton;
    var games_button = document.getElementById('games_button');
    games_button.onclick = onGamesButton;

    
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function LoadVertNavBar(){

    var vertical_navbar = document.getElementById('team_scroll_bar');
    var url = getAPIBaseURL() + '/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams_list) {
        var list_body = '';
        for (var k = 0; k < teams_list.length; k++) {
            var team = teams_list[k];
            list_body += '<button class="team">' + team
                      + '</button>';
        }
        vertical_navbar.innerHTML = list_body;
    })

    .catch(function(error) {
        console.log(error);
    });

}

function onPlayersButton(){
    //hardcoding data because failing queries
    var ppg_content = document.getElementById('ppg-list');
    var ast_content = document.getElementById('ast-list');
    var reb_content = document.getElementById('reb-list');

    ppg_content.innerHTML = '<p>1. Bradley Beal       32.9</p><p>2. Joel Embiid       30.2</p><p>3. Damian Lillard       29.8</p><p>4. Stephen Curry       29.7</p><p>5. Giannis Antetokounmpo       29</p>'
    ast_content.innerHTML = '<p>1. James Harden      11.1</p><p>2. Russell Westbrook       9.8</p><p>3. Trae Young       9.4</p><p>4. Luka Doncic       9.0</p><p>5. Chris Paul       8.8</p>'
}

function onGamesButton(){
    var  content = document.getElementById('content'); 
    var url = getAPIBaseURL() + '/games/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(games_list) {
        var list_body = '<games>';
        for (var k = 0; k < games_list.length; k++) {
            var game = games_list[k];
            list_body += '<p>';
            if (game['team_score']>game['opponent_score']){
                list_body+='<w>'+game['team']+'</w>'+' - '+game['team_score']+'</p>'+'<p>'+game['opponent']+' - '+game['opponent_score'];
            }
            else{
                list_body+=game['team']+' - '+game['team_score']+'</p>'+'<p>'+'<w>'+game['opponent']+'<w>'+' - '+game['opponent_score'];
            }
                
            list_body+='  '+'<date>'+game['month']+'-'+game['day']+'-'+game['year']+'</date>'+'</p>';
        }
        list_body += '</games>'
        content.innerHTML = list_body;
    })

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
            listBody += '<li>' + ppg_team['team']
                      + ', ' + ppg_team['points'];
                      + '</li>\n';
        }

        ppg.innerHTML = listBody;
        
    })

    .catch(function(error) {
        console.log(error);
    });

    /*url = getAPIBaseURL() + '/teams/apg/';

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
    });*/

function search_player() { 
        var  content = document.getElementById('content');
        let input = document.getElementById('player_name').value 
        input=input.toLowerCase(); 
        var url = getAPIBaseURL() + '/players/<input>/'

        fetch(url, {method: 'get'})

        .then((response) => response.json())
        
        .then(function(player_list) {
            var list_body = '';
            for (var k = 0; k < player_list.length; k++) {
                var player = player_list[k];
                list_body += '<p>' +player['player']+player['team']+'</p>';
            }
            content.innerHTML = list_body;
        })


        /*let x = list_body
        
          
        for (i = 0; i < x.length; i++) {  
            if (!x[i].innerHTML.toLowerCase().includes(input)) { 
                x[i].style.display="none"; 
            } 
            else { 
                x[i].style.display="";                  
            } 
        } */
    } 

}