#Eric Gassel & Sam Gloss

CREATE TABLE players{
    id INT
    player_name text
}

CREATE TABLE teams{
	id INT
    team_name text
	abbreviation text
}

CREATE TABLE matchups{
	id INT
	team_1_id INT
	team_2_id INT
}

CREATE TABLE games{
    id INT
    date INT
    home_team text
} 

CREATE TABLE games_matchups{
	id INT
	games_id INT
	matchups_id INT
}

CREATE TABLE team_game_statistics{
	id INT
	games_matchups_id INT
	winning_team text
	home_team_score INT
	away_team_score INT
	point_difference INT
}

CREATE TABLE stats{
	id INT
    MP INT
    PTS INT
    FG INT
    FGA INT
    FG3 INT
    FG3A INT
    FT INT
    FTA INT
    ORB INT
    DRB INT
    TRB INT
    AST INT
    STL INT
    BLK INT
    TOV INT
    PF INT
    plus_minus INT
}

CREATE TABLE player_game_statistics{
	id INT
	games_matchups_id INT
    players_id INT
    teams_id INT
    stats_id INT
}


