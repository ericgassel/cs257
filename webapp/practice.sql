--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: team_data; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.team_data (
    team_name text,
    ppg double precision,
    papg double precision,
    wins integer,
    loses integer,
    point_differential double precision,
    rpg double precision,
    apg double precision
);


--
-- Data for Name: team_data; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.team_data (team_name, ppg, papg, wins, loses, point_differential, rpg, apg) FROM stdin;
Atlanta Hawks	106	99	47	35	7	50	16
Boston Celtics	104	107	48	34	-3	65	25
Brooklyn Nets	98	104	46	36	-6	69	24
Charlotte Hornets	108	104	23	59	4	65	28
Chicago Bulls	99	99	44	38	0	63	23
Cleveland Cavaliers	103	99	44	38	4	70	26
Dallas Mavericks	103	104	45	37	-1	59	19
Denver Nuggets	107	108	49	33	-1	59	15
Detroit Pistons	102	100	52	30	2	61	33
Golden State Warriors	105	99	63	19	6	52	21
Houston Rockets	104	108	34	48	-4	52	23
Indiana Pacers	103	101	21	61	2	65	20
Los Angeles Clippers	106	98	40	42	8	60	19
Los Angeles Lakers	106	100	49	33	6	68	27
Memphis Grizzlies	107	106	64	18	1	69	28
Miami Heat	108	104	50	32	4	56	24
Milwaukee Bucks	114	102	65	17	6	51	28
Minnesota Timberwolves	109	108	59	23	0	67	35
New Orleans Pelicans	103	105	54	28	-2	58	35
New York Knicks	105	101	47	35	4	62	20
Oklahoma City Thunder	98	103	34	48	-5	53	31
Orlando Magic	105	104	48	34	1	61	28
Philadelphia 76ers	104	105	40	42	-1	69	23
Phoenix Suns	98	98	46	36	0	58	28
Portland Trail Blazers	98	101	51	31	-3	70	18
Sacramento Kings	108	107	47	35	1	66	24
San Antonio Spurs	101	99	34	48	2	59	21
Toronto Raptors	101	103	30	52	-2	64	21
Utah Jazz	107	108	28	54	-1	69	18
Washington Wizards	101	100	48	34	1	55	26
\.


--
-- PostgreSQL database dump complete
--

