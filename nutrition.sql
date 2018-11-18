--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.13
-- Dumped by pg_dump version 9.5.13

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.records DROP CONSTRAINT records_profile_id_fkey;
ALTER TABLE ONLY public.records DROP CONSTRAINT records_food_id_fkey;
ALTER TABLE ONLY public.profiles DROP CONSTRAINT profiles_user_id_fkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.records DROP CONSTRAINT records_pkey;
ALTER TABLE ONLY public.profiles DROP CONSTRAINT profiles_pkey;
ALTER TABLE ONLY public.foods DROP CONSTRAINT foods_pkey;
ALTER TABLE ONLY public.dietaryreference DROP CONSTRAINT dietaryreference_pkey;
ALTER TABLE ONLY public.caloriereference DROP CONSTRAINT caloriereference_pkey;
ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
ALTER TABLE public.records ALTER COLUMN record_id DROP DEFAULT;
ALTER TABLE public.profiles ALTER COLUMN profile_id DROP DEFAULT;
ALTER TABLE public.foods ALTER COLUMN food_id DROP DEFAULT;
ALTER TABLE public.dietaryreference ALTER COLUMN dietary_id DROP DEFAULT;
ALTER TABLE public.caloriereference ALTER COLUMN calorie_id DROP DEFAULT;
DROP SEQUENCE public.users_user_id_seq;
DROP TABLE public.users;
DROP SEQUENCE public.records_record_id_seq;
DROP TABLE public.records;
DROP SEQUENCE public.profiles_profile_id_seq;
DROP TABLE public.profiles;
DROP SEQUENCE public.foods_food_id_seq;
DROP TABLE public.foods;
DROP SEQUENCE public.dietaryreference_dietary_id_seq;
DROP TABLE public.dietaryreference;
DROP SEQUENCE public.caloriereference_calorie_id_seq;
DROP TABLE public.caloriereference;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: caloriereference; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.caloriereference (
    calorie_id integer NOT NULL,
    gender character varying(1),
    min_age double precision NOT NULL,
    max_age double precision,
    calories_sedentary double precision NOT NULL,
    calories_modactive double precision NOT NULL,
    calories_active double precision NOT NULL
);


--
-- Name: caloriereference_calorie_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.caloriereference_calorie_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: caloriereference_calorie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.caloriereference_calorie_id_seq OWNED BY public.caloriereference.calorie_id;


--
-- Name: dietaryreference; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dietaryreference (
    dietary_id integer NOT NULL,
    min_age double precision NOT NULL,
    max_age double precision,
    gender character varying(1),
    carbohydrates double precision NOT NULL,
    fiber double precision,
    fat double precision,
    protein double precision NOT NULL,
    "vitA" double precision NOT NULL,
    "vitC" double precision NOT NULL,
    "vitD" double precision NOT NULL,
    "vitE" double precision NOT NULL,
    "vitB6" double precision NOT NULL,
    "vitB12" double precision NOT NULL,
    thiamin double precision NOT NULL,
    riboflavin double precision NOT NULL,
    niacin double precision NOT NULL,
    folate double precision NOT NULL,
    calcium double precision NOT NULL,
    copper double precision NOT NULL,
    iodine double precision NOT NULL,
    iron double precision NOT NULL,
    magnesium double precision NOT NULL,
    phosphorus double precision NOT NULL,
    selenium double precision NOT NULL,
    zinc double precision NOT NULL,
    potassium double precision NOT NULL,
    sodium double precision NOT NULL,
    chloride double precision NOT NULL
);


--
-- Name: dietaryreference_dietary_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dietaryreference_dietary_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dietaryreference_dietary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dietaryreference_dietary_id_seq OWNED BY public.dietaryreference.dietary_id;


--
-- Name: foods; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.foods (
    food_id integer NOT NULL,
    food_name character varying NOT NULL,
    brand_name character varying,
    serving_qty double precision NOT NULL,
    serving_unit character varying NOT NULL,
    serving_weight_grams double precision NOT NULL,
    calories double precision NOT NULL,
    carbohydrates double precision NOT NULL,
    fiber double precision NOT NULL,
    fat double precision,
    protein double precision NOT NULL,
    "vitA" double precision NOT NULL,
    "vitC" double precision NOT NULL,
    "vitD" double precision NOT NULL,
    "vitE" double precision NOT NULL,
    "vitB6" double precision NOT NULL,
    "vitB12" double precision NOT NULL,
    thiamin double precision NOT NULL,
    riboflavin double precision NOT NULL,
    niacin double precision NOT NULL,
    folate double precision NOT NULL,
    calcium double precision NOT NULL,
    copper double precision NOT NULL,
    iodine double precision NOT NULL,
    iron double precision NOT NULL,
    magnesium double precision NOT NULL,
    phosphorus double precision NOT NULL,
    selenium double precision NOT NULL,
    zinc double precision NOT NULL,
    potassium double precision NOT NULL,
    sodium double precision NOT NULL,
    chloride double precision NOT NULL,
    alt_measures character varying(200)
);


--
-- Name: foods_food_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.foods_food_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: foods_food_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.foods_food_id_seq OWNED BY public.foods.food_id;


--
-- Name: profiles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.profiles (
    profile_id integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(64) NOT NULL,
    birthdate date NOT NULL,
    gender boolean NOT NULL
);


--
-- Name: profiles_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.profiles_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: profiles_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.profiles_profile_id_seq OWNED BY public.profiles.profile_id;


--
-- Name: records; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.records (
    record_id integer NOT NULL,
    profile_id integer NOT NULL,
    food_id integer NOT NULL,
    date date NOT NULL,
    serving_qty double precision NOT NULL,
    serving_unit character varying NOT NULL,
    serving_weight_grams double precision NOT NULL
);


--
-- Name: records_record_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.records_record_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: records_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.records_record_id_seq OWNED BY public.records.record_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    fname character varying(64) NOT NULL,
    lname character varying(64) NOT NULL,
    email character varying(64) NOT NULL,
    password character varying(64) NOT NULL
);


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: calorie_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.caloriereference ALTER COLUMN calorie_id SET DEFAULT nextval('public.caloriereference_calorie_id_seq'::regclass);


--
-- Name: dietary_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dietaryreference ALTER COLUMN dietary_id SET DEFAULT nextval('public.dietaryreference_dietary_id_seq'::regclass);


--
-- Name: food_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.foods ALTER COLUMN food_id SET DEFAULT nextval('public.foods_food_id_seq'::regclass);


--
-- Name: profile_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profiles ALTER COLUMN profile_id SET DEFAULT nextval('public.profiles_profile_id_seq'::regclass);


--
-- Name: record_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.records ALTER COLUMN record_id SET DEFAULT nextval('public.records_record_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: caloriereference; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.caloriereference (calorie_id, gender, min_age, max_age, calories_sedentary, calories_modactive, calories_active) FROM stdin;
1	M	2	3	1000	1000	1000
2	M	3	4	1000	1400	1400
3	M	4	5	1200	1400	1600
4	M	5	6	1200	1400	1600
5	M	6	7	1400	1600	1800
6	M	7	8	1400	1600	1800
7	M	8	9	1400	1600	2000
8	M	9	10	1600	1800	2000
9	M	10	11	1600	1800	2200
10	M	11	12	1800	2000	2200
11	M	12	13	1800	2200	2400
12	M	13	14	2000	2200	2600
13	M	14	15	2000	2400	2800
14	M	15	16	2200	2600	3000
15	M	16	17	2400	2800	3200
16	M	17	18	2400	2800	3200
17	M	18	19	2400	2800	3200
18	M	19	21	2600	2800	3000
19	M	21	26	2400	2800	3000
20	M	26	31	2400	2600	3000
21	M	31	36	2400	2600	3000
22	M	36	41	2400	2600	2800
23	M	41	46	2200	2600	2800
24	M	46	51	2200	2400	2800
25	M	51	56	2200	2400	2800
26	M	56	61	2200	2400	2600
27	M	61	66	2000	2400	2600
28	M	66	71	2000	2200	2600
29	M	71	76	2000	2200	2600
30	M	76	\N	2000	2200	2400
31	F	2	3	1000	1000	1000
32	F	3	4	1000	1200	1400
33	F	4	5	1200	1400	1400
34	F	5	6	1200	1400	1600
35	F	6	7	1200	1400	1600
36	F	7	8	1200	1600	1800
37	F	8	9	1400	1600	1800
38	F	9	10	1400	1600	1800
39	F	10	11	1400	1800	2000
40	F	11	12	1600	1800	2000
41	F	12	13	1600	2000	2200
42	F	13	14	1600	2000	2200
43	F	14	15	1800	2000	2400
44	F	15	16	1800	2000	2400
45	F	16	17	1800	2000	2400
46	F	17	18	1800	2000	2400
47	F	18	19	1800	2000	2400
48	F	19	21	2000	2200	2400
49	F	21	26	2000	2200	2400
50	F	26	31	1800	2000	2400
51	F	31	36	1800	2000	2200
52	F	36	41	1800	2000	2200
53	F	41	46	1800	2000	2200
54	F	46	51	1800	2000	2200
55	F	51	56	1600	1800	2200
56	F	56	61	1600	1800	2200
57	F	61	66	1600	1800	2000
58	F	66	71	1600	1800	2000
59	F	71	76	1600	1800	2000
60	F	76	\N	1600	1800	2000
\.


--
-- Name: caloriereference_calorie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.caloriereference_calorie_id_seq', 60, true);


--
-- Data for Name: dietaryreference; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.dietaryreference (dietary_id, min_age, max_age, gender, carbohydrates, fiber, fat, protein, "vitA", "vitC", "vitD", "vitE", "vitB6", "vitB12", thiamin, riboflavin, niacin, folate, calcium, copper, iodine, iron, magnesium, phosphorus, selenium, zinc, potassium, sodium, chloride) FROM stdin;
1	0	0.5	I	60	\N	31	9.09999999999999964	400	40	10	4	0.100000000000000006	0.400000000000000022	0.200000000000000011	0.299999999999999989	2	65	200	200	110	0.270000000000000018	30	100	15	2	0.400000000000000022	0.119999999999999996	0.179999999999999993
2	0.5	1	I	95	\N	30	11	500	50	10	5	0.299999999999999989	0.5	0.299999999999999989	0.400000000000000022	4	80	260	220	130	11	75	275	20	3	0.699999999999999956	0.369999999999999996	0.569999999999999951
3	1	4	C	130	19	\N	13	300	15	15	6	0.5	0.900000000000000022	0.5	0.5	6	150	700	340	90	7	80	460	20	3	3	1	1.5
4	4	9	C	130	25	\N	19	400	25	15	7	0.599999999999999978	1.19999999999999996	0.599999999999999978	0.599999999999999978	8	200	1000	440	90	10	130	500	30	5	3.79999999999999982	1.19999999999999996	1.89999999999999991
5	9	14	M	130	31	\N	34	600	45	15	11	1	1.80000000000000004	0.900000000000000022	0.900000000000000022	12	300	1300	700	120	8	240	1250	40	8	4.5	1.5	2.29999999999999982
6	14	19	M	130	38	\N	52	900	75	15	15	1.30000000000000004	2.39999999999999991	1.19999999999999996	1.30000000000000004	16	400	1300	890	150	11	410	1250	55	11	4.70000000000000018	1.5	2.29999999999999982
7	19	31	M	130	38	\N	56	900	90	15	15	1.30000000000000004	2.39999999999999991	1.19999999999999996	1.30000000000000004	16	400	1000	900	150	8	400	700	55	11	4.70000000000000018	1.5	2.29999999999999982
8	31	51	M	130	38	\N	56	900	90	15	15	1.30000000000000004	2.39999999999999991	1.19999999999999996	1.30000000000000004	16	400	1000	900	150	8	420	700	55	11	4.70000000000000018	1.5	2.29999999999999982
9	51	71	M	130	30	\N	56	900	90	15	15	1.69999999999999996	2.39999999999999991	1.19999999999999996	1.30000000000000004	16	400	1000	900	150	8	420	700	55	11	4.70000000000000018	1.30000000000000004	2
10	71	\N	M	130	30	\N	56	900	90	20	15	1.69999999999999996	2.39999999999999991	1.19999999999999996	1.30000000000000004	16	400	1200	900	150	8	420	700	55	11	4.70000000000000018	1.19999999999999996	1.80000000000000004
11	9	14	F	130	26	\N	34	600	45	15	11	1	1.80000000000000004	0.900000000000000022	0.900000000000000022	12	300	1300	700	120	8	240	1250	40	8	4.5	1.5	2.29999999999999982
12	14	19	F	130	26	\N	46	700	65	15	15	1.19999999999999996	2.39999999999999991	1	1	14	400	1300	890	150	15	360	1250	55	9	4.70000000000000018	1.5	2.29999999999999982
13	19	31	F	130	25	\N	46	700	75	15	15	1.30000000000000004	2.39999999999999991	1.10000000000000009	1.10000000000000009	14	400	1000	900	150	18	310	700	55	8	4.70000000000000018	1.5	2.29999999999999982
14	31	51	F	130	25	\N	46	700	75	15	15	1.30000000000000004	2.39999999999999991	1.10000000000000009	1.10000000000000009	14	400	1000	900	150	18	320	700	55	8	4.70000000000000018	1.5	2.29999999999999982
15	51	71	F	130	21	\N	46	700	75	15	15	1.5	2.39999999999999991	1.10000000000000009	1.10000000000000009	14	400	1200	900	150	8	320	700	55	8	4.70000000000000018	1.30000000000000004	2
16	71	\N	F	130	21	\N	46	700	75	20	15	1.5	2.39999999999999991	1.10000000000000009	1.10000000000000009	14	400	1200	900	150	8	320	700	55	8	4.70000000000000018	1.19999999999999996	1.80000000000000004
17	14	19	P	175	28	\N	71	750	80	15	15	1.89999999999999991	2.60000000000000009	1.39999999999999991	1.39999999999999991	18	600	1300	1000	220	27	400	1250	60	12	4.70000000000000018	1.5	2.29999999999999982
18	19	31	P	175	28	\N	71	770	85	15	15	1.89999999999999991	2.60000000000000009	1.39999999999999991	1.39999999999999991	18	600	1000	1000	220	27	350	700	60	11	4.70000000000000018	1.5	2.29999999999999982
19	31	51	P	175	28	\N	71	770	85	15	15	1.89999999999999991	2.60000000000000009	1.39999999999999991	1.39999999999999991	18	600	1000	1000	220	27	360	700	60	11	4.70000000000000018	1.5	2.29999999999999982
20	14	19	L	210	29	\N	71	1200	115	15	19	2	2.79999999999999982	1.39999999999999991	1.60000000000000009	17	500	1300	1300	290	10	360	1250	70	13	5.09999999999999964	1.5	2.29999999999999982
21	19	31	L	210	29	\N	71	1300	120	15	19	2	2.79999999999999982	1.39999999999999991	1.60000000000000009	17	500	1000	1300	290	9	310	700	70	12	5.09999999999999964	1.5	2.29999999999999982
22	31	51	L	210	29	\N	71	1300	120	15	19	2	2.79999999999999982	1.39999999999999991	1.60000000000000009	17	500	1000	1300	290	9	320	700	70	12	5.09999999999999964	1.5	2.29999999999999982
\.


--
-- Name: dietaryreference_dietary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.dietaryreference_dietary_id_seq', 22, true);


--
-- Data for Name: foods; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.foods (food_id, food_name, brand_name, serving_qty, serving_unit, serving_weight_grams, calories, carbohydrates, fiber, fat, protein, "vitA", "vitC", "vitD", "vitE", "vitB6", "vitB12", thiamin, riboflavin, niacin, folate, calcium, copper, iodine, iron, magnesium, phosphorus, selenium, zinc, potassium, sodium, chloride, alt_measures) FROM stdin;
1	AppleSauce	\N	1	container	111	75.480000000000004	19.4100000000000001	1.33000000000000007	0.190000000000000002	0.179999999999999993	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	cup: 246, container: 111, pouch: 90, g: 100
2	Watermelon Juice	\N	1	container	111	100	30	1.33000000000000007	0.190000000000000002	0.179999999999999993	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	cup: 246, container: 111, pouch: 90, g: 100
3	applesauce	\N	1	container	111	75.480000000000004	19.4100000000000001	1.33000000000000007	0.190000000000000002	0.179999999999999993	0	1.88700000000000001	0	0.199800000000000005	0.0299999999999999989	0	0.0189000000000000001	0.0244000000000000015	0.0798999999999999988	1.1100000000000001	3.33000000000000007	0.0354999999999999968	0	0.133200000000000013	3.33000000000000007	6.66000000000000014	0.333000000000000018	0.0333000000000000032	83.25	2.2200000000000002	0	cup:246, container:111, pouch:90, g:100
4	applesauce pouch	\N	1	pouch	90	61.2000000000000028	15.7400000000000002	1.08000000000000007	0.149999999999999994	0.140000000000000013	0	1.53000000000000003	0	0.162000000000000005	0.0242999999999999987	0	0.0152999999999999994	0.0198000000000000016	0.0647999999999999965	0.900000000000000022	2.70000000000000018	0.0287999999999999992	0	0.107999999999999999	2.70000000000000018	5.40000000000000036	0.270000000000000018	0.0269999999999999997	67.5	1.80000000000000004	0	cup:246, container:111, pouch:90, g:100
5	avocado	\N	1	fruit, without skin and seed	136	227.120000000000005	11.75	9.25	20.9600000000000009	2.66999999999999993	9.51999999999999957	11.968	0	2.6791999999999998	0.39029999999999998	0	0.101999999999999993	0.194500000000000006	2.60029999999999983	121.040000000000006	17.6799999999999997	0.231199999999999989	0	0.829600000000000004	39.4399999999999977	73.4399999999999977	0.544000000000000039	0.924799999999999955	689.519999999999982	10.8800000000000008	0	NLEA serving:30, fruit, without skin and seed:68, cup, pureed:230, cup, cubes:150, g:100
6	mango	\N	1	cup pieces	165	99	24.7199999999999989	2.64000000000000012	0.630000000000000004	1.35000000000000009	89.0999999999999943	60.0600000000000023	0	1.4850000000000001	0.196399999999999991	0	0.046199999999999998	0.0627000000000000057	1.1039000000000001	70.9500000000000028	18.1499999999999986	0.183200000000000002	0	0.264000000000000012	16.5	23.1000000000000014	0.989999999999999991	0.148499999999999993	277.199999999999989	1.64999999999999991	0	fruit without refuse:336, cup pieces:165, g:100
7	grape	\N	10	grapes	49	33.8100000000000023	8.86999999999999922	0.440000000000000002	0.0800000000000000017	0.349999999999999978	1.46999999999999997	1.56800000000000006	0	0.0931000000000000022	0.0420999999999999985	0	0.0337999999999999967	0.0342999999999999972	0.0921000000000000013	0.979999999999999982	4.90000000000000036	0.0621999999999999983	0	0.176400000000000001	3.43000000000000016	9.80000000000000071	0.0490000000000000019	0.0342999999999999972	93.5900000000000034	0.979999999999999982	0	NLEA serving:126, grapes:49, cup:151, grape:5, g:100
8	pear	\N	1	medium	178	101.459999999999994	27.1099999999999994	5.51999999999999957	0.25	0.640000000000000013	1.78000000000000003	7.65399999999999991	0	0.213600000000000012	0.0516	0	0.0213999999999999989	0.0463000000000000009	0.286600000000000021	12.4600000000000009	16.0199999999999996	0.145999999999999991	0	0.320400000000000018	12.4600000000000009	21.3599999999999994	0.177999999999999992	0.177999999999999992	206.47999999999999	1.78000000000000003	0	NLEA serving:166, cup, cubes:161, cup, slices:140, large:230, medium:178, small:148, g:100
9	orange	\N	1	fruit (2-7/8" dia)	140	68.5999999999999943	17.5599999999999987	3.08000000000000007	0.209999999999999992	1.27000000000000002	16.8000000000000007	82.7399999999999949	0	0.209999999999999992	0.110600000000000004	0	0.0952000000000000068	0.0714000000000000051	0.594999999999999973	47.6000000000000014	60.2000000000000028	0.0546000000000000027	0	0.181999999999999995	15.4000000000000004	32.2000000000000028	0	0.112000000000000002	232.400000000000006	1.39999999999999991	0	NLEA serving:154, fruit (2-7/8" dia):140, cup sections, without membranes:165, slice:17, section:17, small:96, large:184, g:100
10	chicken nugget	\N	1	piece	16	49.1199999999999974	2.39000000000000012	0.140000000000000013	3.25999999999999979	2.54999999999999982	0.800000000000000044	0.096000000000000002	0.0320000000000000007	0.179199999999999998	0.0236999999999999988	0.0527999999999999997	0.0146999999999999995	0.032599999999999997	0.957600000000000007	1.76000000000000001	1.76000000000000001	0.00820000000000000069	0	0.132800000000000001	3.83999999999999986	43.5200000000000031	2.75199999999999978	0.0943999999999999978	40.1599999999999966	95.0400000000000063	0	pieces:96, piece:16, cup:139, g:100, tsp:2.9, tbsp:8.69
11	mangosteen	\N	1	fruit	76	55.4799999999999969	13.6099999999999994	1.37000000000000011	0.440000000000000002	0.309999999999999998	1.52000000000000002	2.20400000000000018	0	0	0.0137000000000000004	0	0.0410000000000000017	0.0410000000000000017	0.21740000000000001	23.5599999999999987	9.11999999999999922	0.0524000000000000021	0	0.228000000000000008	9.88000000000000078	6.08000000000000007	0	0.159599999999999992	36.4799999999999969	5.32000000000000028	0	cup:216, cup, drained:196, fruit:76, g:100
12	apple	\N	1	medium (3" dia)	182	94.6400000000000006	25.129999999999999	4.37000000000000011	0.309999999999999998	0.469999999999999973	5.45999999999999996	8.37199999999999989	0	0.327600000000000002	0.0745999999999999996	0	0.0309000000000000004	0.0473000000000000018	0.165599999999999997	5.45999999999999996	10.9199999999999999	0.0490999999999999978	0	0.218400000000000011	9.09999999999999964	20.0199999999999996	0	0.0728000000000000036	194.740000000000009	1.82000000000000006	0	NLEA serving:242, extra small (2-1/2" dia):101, small (2-3/4" dia):149, medium (3" dia):182, large (3-1/4" dia):223, cup slices:109, cup, quartered or chopped:125, g:100
13	corn	\N	1	ear medium	103	98.8799999999999955	21.6099999999999994	2.4700000000000002	1.55000000000000004	3.50999999999999979	13.3900000000000006	5.66500000000000004	0	0.0927000000000000046	0.143199999999999994	0	0.0957999999999999963	0.0587000000000000022	1.73350000000000004	23.6900000000000013	3.08999999999999986	0.0505000000000000032	0	0.463500000000000023	26.7800000000000011	79.3100000000000023	0.205999999999999989	0.638599999999999945	224.539999999999992	1.03000000000000003	0	baby ear:8, cup cut:149, ear large (7-3/4" to 9" long):118, ear medium (6-3/4" to 7-1/2" long):103, ear small (5-1/2" to 6-1/2" long):89, g:100
14	carrot	\N	1	carrot	46	16.1000000000000014	3.7799999999999998	1.37999999999999989	0.0800000000000000017	0.349999999999999978	391.920000000000016	1.65599999999999992	0	0.473799999999999999	0.0704000000000000042	0	0.0303999999999999999	0.0201999999999999992	0.296700000000000019	6.44000000000000039	13.8000000000000007	0.00779999999999999964	0	0.156400000000000011	4.59999999999999964	13.8000000000000007	0.322000000000000008	0.0919999999999999984	108.099999999999994	26.6799999999999997	0	carrot:46, cup slices:78, tbsp:9.7, g:100, cup:155.2, tsp:3.23
15	peach	\N	1	large (2-3/4" dia)	175	68.25	16.6999999999999993	2.62999999999999989	0.440000000000000002	1.59000000000000008	28	11.5500000000000007	0	1.27750000000000008	0.0437999999999999987	0	0.0420000000000000026	0.054300000000000001	1.41050000000000009	7	10.5	0.118999999999999995	0	0.4375	15.75	35	0.174999999999999989	0.297499999999999987	332.5	0	0	NLEA serving:147, extra large (3" dia):224, large (2-3/4" dia):175, medium (2-2/3" dia):150, small (2-1/2" dia):130, cup slices:154, g:100
16	almond	\N	1	almond	1.29000000000000004	7.70999999999999996	0.270000000000000018	0.140000000000000013	0.680000000000000049	0.270000000000000018	0	0	0	0.308300000000000018	0.00179999999999999995	0	0.00100000000000000002	0.0154000000000000005	0.0468999999999999972	0.70950000000000002	3.45719999999999983	0.0142000000000000008	0	0.0480999999999999969	3.59909999999999997	6.07589999999999986	0.0258	0.0427000000000000018	9.19999999999999929	6.42419999999999991	0	oz (22 whole kernels):28.35, cup whole kernels:138, almond:1.29, g:100
17	pineapples	\N	0.5	cup, chunks	82.5	41.25	10.8200000000000003	1.15999999999999992	0.100000000000000006	0.450000000000000011	2.47500000000000009	39.4350000000000023	0	0.0165000000000000008	0.092399999999999996	0	0.0651999999999999941	0.0263999999999999999	0.412499999999999978	14.8499999999999996	10.7249999999999996	0.0908000000000000057	0	0.239300000000000013	9.90000000000000036	6.59999999999999964	0.0825000000000000039	0.0990000000000000047	89.9300000000000068	0.824999999999999956	0	slice, thin (3-1/2" dia x 1/2" thick):56, slice (3-1/2" dia x 3/4" thick):84, slice (4-2/3" dia x 3/4" thick):166, fruit:905, cup, chunks:82.5, g:100
18	appletini	\N	1	cocktail	84.75	149.110000000000014	6.69000000000000039	0.0500000000000000028	0.0100000000000000002	0.0299999999999999989	0.152499999999999997	1.09040000000000004	0	0.0175000000000000017	0.0028999999999999998	0	0.00440000000000000027	0.00589999999999999986	0.0152	0.686300000000000021	1.34610000000000007	0.0102000000000000007	0	0.0165000000000000008	0.707400000000000029	3.24589999999999979	0.0451999999999999971	0.0214999999999999983	9.08999999999999986	3.12219999999999986	0	fl oz:29, cocktail:84.75, g:100
\.


--
-- Name: foods_food_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.foods_food_id_seq', 18, true);


--
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.profiles (profile_id, user_id, name, birthdate, gender) FROM stdin;
1	1	Matthew	2016-08-06	f
7	1	kellie	1986-10-04	t
\.


--
-- Name: profiles_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.profiles_profile_id_seq', 8, true);


--
-- Data for Name: records; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.records (record_id, profile_id, food_id, date, serving_qty, serving_unit, serving_weight_grams) FROM stdin;
2	1	2	2018-10-07	3	cup	246
1	1	1	2018-10-07	2	container	111
3	1	5	2018-10-07	0	fruit, without skin and seed	136
4	1	3	2018-11-01	0	container	111
5	1	5	2018-11-01	0	fruit, without skin and seed	136
6	1	6	2018-11-01	0	cup pieces	165
7	1	7	2018-11-01	0	grapes	49
8	1	8	2018-11-01	0	medium	178
9	1	9	2018-11-01	0	fruit (2-7/8" dia)	140
10	1	10	2018-11-01	0	piece	16
11	1	11	2018-11-01	0	fruit	76
14	1	11	2018-11-04	0	fruit	76
17	1	8	2018-11-04	0	medium	178
20	1	15	2018-11-04	0	large (2-3/4" dia)	175
23	1	17	2018-11-04	0	cup, chunks	82.5
15	1	12	2018-11-04	3	medium (3" dia)	182
12	1	5	2018-11-04	3	fruit, without skin and seed	136
13	1	6	2018-11-04	4	cup pieces	165
16	1	7	2018-11-04	6	grapes	49
18	1	13	2018-11-04	1	ear medium	103
22	1	16	2018-11-04	2	almond	1.29000000000000004
19	1	14	2018-11-04	2	carrot	46
21	1	9	2018-11-04	2	fruit (2-7/8" dia)	140
24	1	6	2018-11-05	0	cup pieces	165
25	1	12	2018-11-05	3	medium (3" dia)	182
37	1	3	2018-11-05	2	container	111
38	1	18	2018-11-04	0	cocktail	84.75
39	1	11	2018-11-05	0	fruit	76
40	1	3	2018-11-11	0	container	111
41	1	6	2018-11-11	0	cup pieces	165
\.


--
-- Name: records_record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.records_record_id_seq', 41, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (user_id, fname, lname, email, password) FROM stdin;
1	Kellie	Tay	kellie@gmail.com	password
2	Paul	Ng	paul@gmail.com	password
3	Allian	Roman	a@gmail.com	password
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_user_id_seq', 3, true);


--
-- Name: caloriereference_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.caloriereference
    ADD CONSTRAINT caloriereference_pkey PRIMARY KEY (calorie_id);


--
-- Name: dietaryreference_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dietaryreference
    ADD CONSTRAINT dietaryreference_pkey PRIMARY KEY (dietary_id);


--
-- Name: foods_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.foods
    ADD CONSTRAINT foods_pkey PRIMARY KEY (food_id);


--
-- Name: profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey PRIMARY KEY (profile_id);


--
-- Name: records_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (record_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: profiles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: records_food_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_food_id_fkey FOREIGN KEY (food_id) REFERENCES public.foods(food_id);


--
-- Name: records_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(profile_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

