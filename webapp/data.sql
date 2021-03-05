
CREATE TABLE players(
    id INT,
    player text
);

CREATE TABLE matchups(
	id INT,
	team text,
	opponent text
);

CREATE TABLE games(
    id INT,
    game_id text,
    year INT,
    month INT,
    day INT,
    home_team text
);

CREATE TABLE games_matchups(
	id INT,
	games_id INT,
	matchups_id INT,
    result text,
	team_score INT,
	opponent_score INT,
	point_difference INT
);


CREATE TABLE stats(
	id INT,
    MP INT,
    PTS INT,
    FG INT,
    FGA INT,
    FG3 INT,
    FG3A INT,
    FT INT,
    FTA INT,
    ORB INT,
    DRB INT,
    TRB INT,
    AST INT,
    STL INT,
    BLK INT,
    TOV INT,
    PF INT,
    plus_minus INT
);

CREATE TABLE player_game_statistics(
	id INT,
	games_matchups_id INT,
    players_id INT,
    stats_id INT
);

\copy players from 'csv-data/players.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy games from 'csv-data/games.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy matchups from 'csv-data/matchups.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy games_matchups from 'csv-data/games_matchups.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy stats from 'csv-data/stats.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy player_game_statistics from 'csv-data/player_game_statistics.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
