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
            list_body += '<button class="team" onclick="on_selected_team(\'' + team + '\')">' + team  + '</button>';
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
    var content = document.getElementById('content');
    content.innerHTML = top_five_page();

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

    var list_body = '<table>';
    
        for (var k = 0; k < 5; k++) {
            var stat_player = per_games_list[k];
            list_body += '<tr><td>'+ (k+1)+'. ' + stat_player['name']+'</td>' 
                      + '<td>'+stat_player['per_game']+'</td>'
                      ;
        }

        list_body+='</table>'
    return list_body;
}

function top_five_page(){
    list_body = '<div class="mini-header">Points Per Game</div><div class="mini-header">'+
    'Assists Per Game</div><div class="stat-content"><a id = "ppg-list"></a></div>'+
    '<div class="stat-content"><a id = "ast-list"></a></div><div class="mini-header">Rebounds Per Game'+
    '</div><div class="mini-header">Blocks Per Game</div><div class="stat-content"><a id = "reb-list"></a>'+
    '</div><div class="stat-content"><a id = "blk-list"></a></div><div class="mini-header">Steals Per Game</div><div class="mini-header">Turnovers Per Game'+
    '</div><div class="stat-content"><a id = "stl-list"></a></div><div class="stat-content"><a id = "tov-list"></a></div>';
    return list_body;
}

function on_teams_button(){
    var content = document.getElementById('content');
    content.innerHTML = top_five_page();
    
    var PPG_content = document.getElementById('ppg-list');
    var APG_content = document.getElementById('ast-list');
    var RPG_content = document.getElementById('reb-list');
    var SPG_content = document.getElementById('stl-list');
    var BPG_content = document.getElementById('blk-list');
    var TOV_content = document.getElementById('tov-list');

    teams_button.focus();
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

    var filter = document.getElementById('filter-month');
    var content = document.getElementById('content');

    selected = 'game'

    var url = get_API_base_URL() + '/games/' + season + '/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(games_list) {
        var list_body = '<table><tr><th>Away Team</th><th>Away Score</th><th>Home Team</th><th>Home Score</th><th>Date</th></tr>';

    
        for (var k = 0; k < games_list.length; k++) {
            var game = games_list[k];
            list_body += '<tr><td>'+ game['away_team']+'</td>' 
                        + '<td>'+ game['away_score']+'</td>'
                        + '<td>'+ game['home_team']+'</td>'
                        + '<td>'+ game['home_score']+'</td>'
                      + '<td>'+game['month']+'-'+game['day']+'-'+game['year']+'</td>'
                      ;
        }

        list_body+='</table>'
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

function on_selected_team(team){

    var content = document.getElementById('content');

    list_body = '<div class = "team-page-header">' + team + '</div>';

    var url_roster = get_API_base_URL() + '/' + team + '/' + season + '/';
    var url_ppg = get_API_base_URL() + '/teams/PPG/' + season + '/?team_name=' + team;
    var url_apg = get_API_base_URL() + '/teams/APG/' + season + '/?team_name=' + team;
    var url_rpg = get_API_base_URL() + '/teams/RPG/' + season + '/?team_name=' + team;
    var url_bpg = get_API_base_URL() + '/teams/BPG/' + season + '/?team_name=' + team;
    var url_spg = get_API_base_URL() + '/teams/SPG/' + season + '/?team_name=' + team;
    var url_tov = get_API_base_URL() + '/teams/TOV/' + season + '/?team_name=' + team;
    var url_schedule = get_API_base_URL() + '/games/' + season + '/?team_neame=' + team;

    fetch(url_roster, {method: 'get'})

    .then((response) => response.json())

    .then(function(roster_list) {
        list_body+='<div class="roster"><table><tr><th>Roster</th></tr>'
        for (var k = 0; k < roster_list.length; k++) {
            var player = roster_list[k];
            list_body += '<tr><td>'+ player['name']+'</td></tr>'
                      ;
        }
    
        list_body+='</table></div>'
        content.innerHTML = list_body;

    })

    fetch(url_schedule, {method: 'get'})

    .then((response) => response.json())

    .then(function(games_list) {
        list_body += '<div class="schedule"><table><tr><th>Away Team</th><th>Away Score</th><th>Home Team</th><th>Home Score</th><th>Date</th></tr>';

        for (var k = 0; k < games_list.length; k++) {
            var game = games_list[k];
            list_body += '<tr><td>'+ game['away_team']+'</td>' 
                        + '<td>'+ game['away_score']+'</td>'
                        + '<td>'+ game['home_team']+'</td>'
                        + '<td>'+ game['home_score']+'</td>'
                      + '<td>'+game['month']+'-'+game['day']+'-'+game['year']+'</td>'
                      ;
        }

        list_body+='</table></div>';
        content.innerHTML=list_body;

    })

    fetch(url_ppg, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_game_list) {
        list_body+='<div class="team-stats"><table><tr><th>Team Stats</th></tr>'
        for (var k = 0; k < per_game_list.length; k++) {
            var stat = per_game_list[k];
            list_body += '<tr><td> PPG: '+ stat['per_game']+'</td></tr>'
                      ;
        }
    })

    fetch(url_apg, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_game_list) {
        for (var k = 0; k < per_game_list.length; k++) {
            var stat = per_game_list[k];
            list_body += '<tr><td> APG: '+ stat['per_game']+'</td></tr>'
                      ;
        }
    })

    fetch(url_rpg, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_game_list) {
        for (var k = 0; k < per_game_list.length; k++) {
            var stat = per_game_list[k];
            list_body += '<tr><td> RPG: '+ stat['per_game']+'</td></tr>'
                      ;
        }
    })

    fetch(url_spg, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_game_list) {
        for (var k = 0; k < per_game_list.length; k++) {
            var stat = per_game_list[k];
            list_body += '<tr><td> SPG: '+ stat['per_game']+'</td></tr>'
                      ;
        }
    })

    fetch(url_bpg, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_game_list) {
        for (var k = 0; k < per_game_list.length; k++) {
            var stat = per_game_list[k];
            list_body += '<tr><td> BPG: '+ stat['per_game']+'</td></tr>'
                      ;
        }
    })

    fetch(url_tov, {method: 'get'})

    .then((response) => response.json())

    .then(function(per_game_list) {
        for (var k = 0; k < per_game_list.length; k++) {
            var stat = per_game_list[k];
            list_body += '<tr><td> TOV: '+ stat['per_game']+'</td></tr>'
                      ;
        }
        list_body+='</table></div>';
        content.innerHTML = list_body;
    })



}
