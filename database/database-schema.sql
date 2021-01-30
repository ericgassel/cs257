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

