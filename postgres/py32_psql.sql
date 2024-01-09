--
-- PostgreSQL database dump
--

-- Dumped from database version 13.10 (Ubuntu 13.10-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.10 (Ubuntu 13.10-1.pgdg20.04+1)

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
-- Name: person; Type: TABLE; Schema: public; Owner: hello
--

CREATE TABLE public.person (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    age integer NOT NULL,
    last_name text,
    CONSTRAINT person_age_check CHECK (((age > 0) AND (age < 20)))
);


ALTER TABLE public.person OWNER TO hello;

--
-- Name: person_id_seq; Type: SEQUENCE; Schema: public; Owner: hello
--

CREATE SEQUENCE public.person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.person_id_seq OWNER TO hello;

--
-- Name: person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hello
--

ALTER SEQUENCE public.person_id_seq OWNED BY public.person.id;


--
-- Name: shop; Type: TABLE; Schema: public; Owner: hello
--

CREATE TABLE public.shop (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    price integer,
    quantity integer,
    CONSTRAINT product_price_check CHECK ((price > 0))
);


ALTER TABLE public.shop OWNER TO hello;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: hello
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO hello;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hello
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.shop.id;


--
-- Name: person id; Type: DEFAULT; Schema: public; Owner: hello
--

ALTER TABLE ONLY public.person ALTER COLUMN id SET DEFAULT nextval('public.person_id_seq'::regclass);


--
-- Name: shop id; Type: DEFAULT; Schema: public; Owner: hello
--

ALTER TABLE ONLY public.shop ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: hello
--

COPY public.person (id, name, age, last_name) FROM stdin;
\.


--
-- Data for Name: shop; Type: TABLE DATA; Schema: public; Owner: hello
--

COPY public.shop (id, name, price, quantity) FROM stdin;
2	Iphone 10	650	\N
3	mouse	200	\N
4	watch	350	\N
5	AirPods	150	\N
6	MacBook Pro M3	1950	\N
7	Iphone 13	850	\N
10	AirPods Pro	180	\N
1	Iphone 12 Pro Max	750	\N
12	Iphone 12 Pro Max	700	\N
13	mouse	30	\N
14	MacBook Pro M3	2200	\N
15	Iphone 10	660	\N
8	mouse	150	\N
\.


--
-- Name: person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hello
--

SELECT pg_catalog.setval('public.person_id_seq', 3, true);


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hello
--

SELECT pg_catalog.setval('public.product_id_seq', 15, true);


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: hello
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);


--
-- Name: shop product_pkey; Type: CONSTRAINT; Schema: public; Owner: hello
--

ALTER TABLE ONLY public.shop
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

