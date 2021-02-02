CREATE TABLE athletes (
    id INT,
    names text,
    sex text,
    weight INT
);

CREATE TABLE games(
    id INT,
    years INT,
    season text,
    city text
);

CREATE TABLE events(
    id INT,
    events text,
    sports text
);


CREATE TABLE athletes_games (
    id INT,
    athletes_id INT,
    games_id INT,
    NOC text,
    team text
);

CREATE TABLE athletes_total(
    id INT,
    athletes_games_id INT,
    events INT,
    medal text
);

\copy athletes from 'athletes.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy games from 'games.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy events from 'events.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy athletes_games from 'athletes_games.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
\copy athletes_total from 'athletes_total.csv' DELIMITER ',' CSV NULL AS 'NA' HEADER;
