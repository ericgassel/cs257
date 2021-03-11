/*
 * webapp.js
 * Eric Gassel and Sam Gloss
 * February 24 2021
 *
 */

window.onload = initialize;
var season = '2019_2020'
var selected = 'players'

function initialize() {
    load_vert_nav_bar();
    on_players_button();

    var players_button = document.getElementById('players_button');
    players_button.onclick = on_players_button
    var teams_button = document.getElementById('teams_button');
    teams_button.onclick = on_teams_button
    var games_button = document.getElementById('games_button');
    games_button.onclick = on_games_button
    
    
}


function get_API_base_URL() {
    var base_URL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return base_URL;
}

function load_vert_nav_bar(){

    var vertical_navbar = document.getElementById('team_scroll_bar');
    var url = get_API_base_URL() + '/teams/';

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
function get_selected_value(){
    var e = document.getElementById("season");
    var result = e.options[e.selectedIndex].value;
    season = result
    console.log(selected)
    if (selected == 'players'){
        on_players_button()
    } 
    else if (selected == 'teams'){
        on_teams_button()
    }
    else if (selected == 'games'){
        on_games_button()
    }
    else{
        console.log('something went wrong');
    }
   
}

function on_players_button(){
    var PPG_content = document.getElementById('ppg-list');
    var APG_content = document.getElementById('ast-list');
    var RPG_content = document.getElementById('reb-list');
    var SPG_content = document.getElementById('stl-list');
    var BPG_content = document.getElementById('blk-list');
    var TOV_content = document.getElementById('tov-list');

    selected = 'players'
    players_button.focus();

    
    type = 'PPG';

    var url = get_API_base_URL() + '/players/' + type + '/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        PPG_content.innerHTML = list_body;
    })

    type = 'APG'
    var url2 = get_API_base_URL() + '/players/' + type + '/' + season + '/';

    fetch(url2, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        APG_content.innerHTML = list_body;
    })
    
    type = 'SPG'
    var url3 = get_API_base_URL() + '/players/' + type + '/' + season + '/';

    fetch(url3, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        SPG_content.innerHTML = list_body;
    })
    
    type = 'BPG'
    var url4 = get_API_base_URL() + '/players/' + type + '/' + season + '/';

    fetch(url4, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        BPG_content.innerHTML = list_body;
    })
    
    type = 'RPG'
    var url5 = get_API_base_URL() + '/players/' + type + '/' + season + '/';

    fetch(url5, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        RPG_content.innerHTML = list_body;
    })

    
    type = 'TOV'
    var url6 = get_API_base_URL() + '/players/' + type + '/' + season + '/';

    fetch(url6, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        TOV_content.innerHTML = list_body;
    })

}

function fill_top_five(per_games_list){
    var list_body = '';
    
        for (var k = 0; k < 5; k++) {
            var stat_player = per_games_list[k];
            list_body += '<a class="top-list"> '+ (k+1)+'. ' + stat_player['name'] 
                      + '-'+stat_player['per_game']+'</a>'
                      ;
        }
    return list_body;
}

function on_teams_button(){
    var PPG_content = document.getElementById('ppg-list');
    var APG_content = document.getElementById('ast-list');
    var RPG_content = document.getElementById('reb-list');
    var SPG_content = document.getElementById('stl-list');
    var BPG_content = document.getElementById('blk-list');
    var TOV_content = document.getElementById('tov-list');

    teams_button.focus();
    console.log('teams')
    selected = 'teams'

    type = 'PPG';

    var url = get_API_base_URL() + '/teams/' + type + '/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        PPG_content.innerHTML = list_body;
    })

    type = 'APG'
    var url2 = get_API_base_URL() + '/teams/' + type + '/' + season + '/';

    fetch(url2, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        APG_content.innerHTML = list_body;
    })
    
    type = 'SPG'
    var url3 = get_API_base_URL() + '/teams/' + type + '/' + season + '/';

    fetch(url3, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        SPG_content.innerHTML = list_body;
    })
    
    type = 'BPG'
    var url4 = get_API_base_URL() + '/teams/' + type + '/' + season + '/';

    fetch(url4, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        BPG_content.innerHTML = list_body;
    })
    
    type = 'RPG'
    var url5 = get_API_base_URL() + '/teams/' + type + '/' + season + '/';

    fetch(url5, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        RPG_content.innerHTML = list_body;
    })

    
    type = 'TOV'
    var url6 = get_API_base_URL() + '/teams/' + type + '/' + season + '/';

    fetch(url6, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_games_list) {
        list_body = fill_top_five(per_games_list);
        TOV_content.innerHTML = list_body;
    })
            
}
    
function on_games_button(){

    var content = document.getElementById('content');

    selected = 'game'

    var url = get_API_base_URL() + '/games/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(games_list) {
        list_body = '<games-page>';
        for (var k = 0; k < games_list.length; k++) {
            var game = games_list[k];
            list_body += '<a class="game"> '+ game['away_team']+' @ '+game['home_team']+'</a>'
                      ;
        }
        list_body+='<games-page>';
        content.innerHTML = list_body;
    })


}
function search_player() { 
        var  content = document.getElementById('content');
        let input = document.getElementById('player_name').value 
        input=input.toLowerCase(); 
        var url = get_API_base_URL() + '/players/PPG/<season>?player_name=<input>/'

        fetch(url, {method: 'get'})

        .then((response) => response.json())
        
        .then(function(player_list) {
            var list_body = 'good job';
            /*for (var k = 0; k < player_list.length; k++) {
                var player = player_list[k];
                list_body += '<p>' +player['player']+player['team']+'</p>';
            }*/
            content.innerHTML = list_body;
        })
    } 

