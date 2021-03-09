CREATE TABLE player(
    id INT,
    player text
);

CREATE TABLE team(
    id INT,
    team text
);

CREATE TABLE game(
    id INT,
    home_team INT,
    away_team INT,
    year INT,
    month INT,
    day INT
);

CREATE TABLE player_game(
    id INT,
    player_id INT,
    game_id INT,
    team_id INT,
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

\copy player from 'csv-data/players.csv' DELIMITER ',' CSV NULL AS 'NULL' HEADER;
\copy team from 'csv-data/team.csv' DELIMITER ',' CSV NULL AS 'NULL' HEADER;
\copy game from 'csv-data/games.csv' DELIMITER ',' CSV NULL AS 'NULL' HEADER;
\copy player_game from 'csv-data/players_games.csv' DELIMITER ',' CSV NULL AS 'NULL' HEADER;