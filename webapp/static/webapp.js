/*
 * webapp.js
 * Eric Gassel and Sam Gloss
 * February 24 2021
 *
 */

window.onload = initialize;
var season = '2020_2021'
var selected = 'players'

function initialize() {
    LoadVertNavBar();
    onPlayersButton();

    var players_button = document.getElementById('players_button');
    players_button.onclick = playersSelected();
    var teams_button = document.getElementById('teams_button');
    teams_button.onclick = teamsSelected();
    var games_button = document.getElementById('games_button');
    games_button.onclick = onGamesButton;

    
}

function playersSelected(){
    console.log('players')
    selected = 'players'
    onPlayersButton();
}
function teamsSelected(){
    console.log("teams")
    selected = 'teams'
    onTeamsButton();
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
function GetSelectedValue(){
    var e = document.getElementById("season");
    var result = e.options[e.selectedIndex].value;
    season = result
    if (selected = "players"){
        onPlayersButton();
    } 
    else if (selected = "teams"){
        onTeamsButton();
    }
    else{
        console.log('something went wrong');
    }
   
}

function onPlayersButton(){
    var PPG_content = document.getElementById('ppg-list');
    var APG_content = document.getElementById('ast-list');
    var RPG_content = document.getElementById('reb-list');
    var SPG_content = document.getElementById('stl-list');
    var BPG_content = document.getElementById('blk-list');
    var TOV_content = document.getElementById('tov-list');

    players_button.focus();

    
    type = 'PPG';

    var url = getAPIBaseURL() + '/players/' + type + '/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        PPG_content.innerHTML = listBody;
    })

    type = 'APG'
    var url2 = getAPIBaseURL() + '/players/' + type + '/' + season + '/';

    fetch(url2, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        APG_content.innerHTML = listBody;
    })
    
    type = 'SPG'
    var url3 = getAPIBaseURL() + '/players/' + type + '/' + season + '/';

    fetch(url3, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        SPG_content.innerHTML = listBody;
    })
    
    type = 'BPG'
    var url4 = getAPIBaseURL() + '/players/' + type + '/' + season + '/';

    fetch(url4, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        BPG_content.innerHTML = listBody;
    })
    
    type = 'RPG'
    var url5 = getAPIBaseURL() + '/players/' + type + '/' + season + '/';

    fetch(url5, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        RPG_content.innerHTML = listBody;
    })

    
    type = 'TOV'
    var url6 = getAPIBaseURL() + '/players/' + type + '/' + season + '/';

    fetch(url6, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        TOV_content.innerHTML = listBody;
    })

}

function fillTopFive(per_games_list){
    var listBody = '';
    
        for (var k = 0; k < 5; k++) {
            var stat_player = per_games_list[k];
            listBody += '<a class="top-list"> '+ (k+1)+'. ' + stat_player['name'] 
                      + '-'+stat_player['per_game']+'</a>'
                      ;
        }
    return listBody;
}

function onTeamsButton(){
    var PPG_content = document.getElementById('ppg-list');
    var APG_content = document.getElementById('ast-list');
    var RPG_content = document.getElementById('reb-list');
    var SPG_content = document.getElementById('stl-list');
    var BPG_content = document.getElementById('blk-list');
    var TOV_content = document.getElementById('tov-list');

    teams_button.focus();

    type = 'PPG';

    var url = getAPIBaseURL() + '/teams/' + type + '/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        PPG_content.innerHTML = listBody;
    })

    type = 'APG'
    var url2 = getAPIBaseURL() + '/teams/' + type + '/' + season + '/';

    fetch(url2, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        APG_content.innerHTML = listBody;
    })
    
    type = 'SPG'
    var url3 = getAPIBaseURL() + '/teams/' + type + '/' + season + '/';

    fetch(url3, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        SPG_content.innerHTML = listBody;
    })
    
    type = 'BPG'
    var url4 = getAPIBaseURL() + '/teams/' + type + '/' + season + '/';

    fetch(url4, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        BPG_content.innerHTML = listBody;
    })
    
    type = 'RPG'
    var url5 = getAPIBaseURL() + '/teams/' + type + '/' + season + '/';

    fetch(url5, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        RPG_content.innerHTML = listBody;
    })

    
    type = 'TOV'
    var url6 = getAPIBaseURL() + '/teams/' + type + '/' + season + '/';

    fetch(url6, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        listBody = fillTopFive(per_games_list);
        TOV_content.innerHTML = listBody;
    })
            
}
    
function onGamesButton(){

    var content = document.getElementById('content');

    season = "2019_2020"

    var url = getAPIBaseURL() + '/games/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(games_list) {
        listBody = '<games-page>';
        for (var k = 0; k < games_list.length; k++) {
            var game = games_list[k];
            listBody += '<a class="game"> '+ game['away_team']+' @ '+game['home_team']+'</a>'
                      ;
        }
        listBody+='<games-page>';
        content.innerHTML = listBody;
    })


}
function search_player() { 
        var  content = document.getElementById('content');
        let input = document.getElementById('player_name').value 
        input=input.toLowerCase(); 
        var url = getAPIBaseURL() + '/players/<game_stat>/<season>/<input>/'

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
    } 

