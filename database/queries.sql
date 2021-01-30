SELECT DISTINCT athletes_games.NOC
FROM athletes_games
ORDER BY NOC;

SELECT athletes.names
FROM athletes, athletes_games
WHERE athletes.id = athletes_games.athlete_id
AND athlete_games.NOC LIKE 'Kenya%';

SELECT athletes.names, athletes_total.medal, games.year
FROM athletes, athletes_total, games, athletes_games
WHERE athletes.id = athletes_games.athlete_id
AND games.id = athlete_games.games_id
AND athlete.names LIKE 'Greg Louganis%'

SELECT DISTINCT athletes_games.NOC, athletes_total.medal
FROM athlete_games, athletes_total
WHERE athletes_games.id = athletes_total.athletes_games_id
ORDER BY medal;