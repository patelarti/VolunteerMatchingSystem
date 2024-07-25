--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-07-24 19:54:42

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
-- TOC entry 218 (class 1259 OID 16436)
-- Name: event_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event_details (
    event_id bigint NOT NULL,
    event_name character varying(100) NOT NULL,
    description character varying(500) NOT NULL,
    location character varying(100) NOT NULL,
    required_skills character varying(1000) NOT NULL,
    urgency character varying(10) NOT NULL,
    event_date date NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.event_details OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16435)
-- Name: event_details_event_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.event_details ALTER COLUMN event_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.event_details_event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 222 (class 1259 OID 16487)
-- Name: notifications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications (
    user_id bigint NOT NULL,
    msg character varying(200) NOT NULL,
    notification_type boolean DEFAULT true NOT NULL
);


ALTER TABLE public.notifications OWNER TO postgres;

--
-- TOC entry 4875 (class 0 OID 0)
-- Dependencies: 222
-- Name: COLUMN notifications.notification_type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.notifications.notification_type IS 'notification type - default - true that is for user sign up
for admin - he need to update notification type to false to assign event.

TRUE -> user sign up notif (admins will receive this)
FALSE-> assign event notif (users will receive this)';


--
-- TOC entry 219 (class 1259 OID 16460)
-- Name: user_profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_profile (
    user_id bigint NOT NULL,
    full_name character varying(50) NOT NULL,
    address_1 character varying(100) NOT NULL,
    address_2 character varying(100),
    city character varying(100) NOT NULL,
    state character varying(2) NOT NULL,
    zipcode character varying(9) NOT NULL,
    skills character varying(1000) NOT NULL,
    preference character varying(1000) NOT NULL,
    availability date NOT NULL
);


ALTER TABLE public.user_profile OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16425)
-- Name: usercredentials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usercredentials (
    id bigint NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255) NOT NULL,
    is_admin boolean DEFAULT false NOT NULL
);


ALTER TABLE public.usercredentials OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16434)
-- Name: usercredentials_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.usercredentials ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.usercredentials_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 16472)
-- Name: volunteer_history; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.volunteer_history (
    history_id bigint NOT NULL,
    user_id bigint NOT NULL,
    event_id bigint NOT NULL
);


ALTER TABLE public.volunteer_history OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16471)
-- Name: volunteer_history_history_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.volunteer_history ALTER COLUMN history_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.volunteer_history_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4865 (class 0 OID 16436)
-- Dependencies: 218
-- Data for Name: event_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event_details (event_id, event_name, description, location, required_skills, urgency, event_date, user_id) FROM stdin;
2	abc	description	new york	Event Planning,Public Speaking,Organization,Customer Service,	High	2024-07-30	4
3	test 7-24 event	test description	test location	Environmental Awareness,Physical Fitness,Teamwork,Event Planning,Public Speaking,Organization,Customer Service,Lifting,Patience,Communication,Mentoring,Conflict Resolution,Creativity,Customer Service,	High	2024-07-31	4
\.


--
-- TOC entry 4869 (class 0 OID 16487)
-- Dependencies: 222
-- Data for Name: notifications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications (user_id, msg, notification_type) FROM stdin;
17	test_notif signed up!	t
17	You have been assigned the event abc on 2024-07-30	f
17	You have been assigned the event test 7-24 event on 2024-07-31	f
4	You have been assigned the event abc on 2024-07-30	f
4	You have been assigned the event test 7-24 event on 2024-07-31	f
17	You have been assigned the event abc on 2024-07-30	f
18	ashutosh signed up!	t
\.


--
-- TOC entry 4866 (class 0 OID 16460)
-- Dependencies: 219
-- Data for Name: user_profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_profile (user_id, full_name, address_1, address_2, city, state, zipcode, skills, preference, availability) FROM stdin;
4	Arti Patel	new address		houston	TX	77007	Environmental Awareness,Public Speaking		2024-07-17
17	test	3515 Hughes Ln		Dickinson	TX	77539	Environmental Awareness,Physical Fitness,Teamwork		2024-07-26
18	Ashutosh Kumar	1234 Sadak Rd	Mohalla Nagar	Sheherpuri	TX	77007	Environmental Awareness,Physical Fitness,Teamwork,Event Planning,Public Speaking,Organization,Customer Service,Lifting,Patience,Communication,Mentoring,Conflict Resolution,Creativity,Customer Service	No holds bar	2024-07-24
\.


--
-- TOC entry 4862 (class 0 OID 16425)
-- Dependencies: 215
-- Data for Name: usercredentials; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usercredentials (id, username, email, password, is_admin) FROM stdin;
2	abc123	abc123@gmail.com	$2b$12$lRv1LqiFOK7jsB58ePZWWuJKxvm1EAAFzbaushiyESMzsRsp/WFBa	f
3	test_abc	test_abc@gmail.com	$2b$12$45KIN4R9wI4UQ82GFHI2f.wpENZOUMmJ6.6W8t4eRf4fCiUylaTQu	f
4	patelarti91	patelarti91@gmail.com	$2b$12$lVZxk9ehVn6nBPzzwbusm.6KFYm1xIJJ7IcTpau0ZMex9GyNXoLtu	f
5	patelarti92	patelarti92@gmail.com	$2b$12$sDCCbUzOgeiSreFhy4aU5eLqAbIWl78jyUXB/rHxhVPqVPm8t2m5u	f
6	patelarti93	patelarti93@gmail.com	$2b$12$1lidYbDmrB8ZtSffvvUGAukw8bCdbPOfiNWEe4/bzKm5DKnrhE97.	f
7	random	random@gmail.com	$2b$12$F6Oi2RSwD8D8V8wvKCke1eiqGPlA10bV/sLHfr25EF9bqs/3Ds/jW	f
8	random1	random1@gmail.com	$2b$12$NIBEKYmAZCZz.t6r3.9SLumElFQ8peD1TM8injNMScwIpqk8nsWeu	f
9	random2	random2@gmail.com	$2b$12$DtD2B7.fsh6vqexnvcUfFu4Nr2x8hfQ.xCYntwk9Kv0UfUl2TlFDq	f
10	random8	random8@gmail.com	$2b$12$hYshgxGBZE9.1GiEzHszA.eUxoR/qreVuW1Y/4nsi3RxE2iufiWcC	f
11	random9	random9@gmail.com	$2b$12$cgbzJS1dV0umHH3qnobo3uT.L2JW2n2MNtt3RJyLKeEfysETSqmfS	f
12	random10	random10@gmail.com	$2b$12$LpdqMrwwcGZ7SVSkquUvWOtLvGayHRYvZliyKqXkooPrUT5gff9w6	t
17	test_notif	test_notif@gmail.com	$2b$12$AL2pSaNGvtzvyVpcQkO4M.OyeJ5JAPU9PoqgYe1GcWwjlDHQAtFvK	f
18	ashutosh	ashutosh@example.com	$2b$12$vlnBMzBF9fC9ZZw49UOdvukUUQP4qCX/OImUfhCXQvLp.ydhMWPJG	t
\.


--
-- TOC entry 4868 (class 0 OID 16472)
-- Dependencies: 221
-- Data for Name: volunteer_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.volunteer_history (history_id, user_id, event_id) FROM stdin;
1	4	2
2	4	3
3	17	2
4	17	3
5	4	2
6	4	3
7	17	2
\.


--
-- TOC entry 4876 (class 0 OID 0)
-- Dependencies: 217
-- Name: event_details_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.event_details_event_id_seq', 7, true);


--
-- TOC entry 4877 (class 0 OID 0)
-- Dependencies: 216
-- Name: usercredentials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usercredentials_id_seq', 18, true);


--
-- TOC entry 4878 (class 0 OID 0)
-- Dependencies: 220
-- Name: volunteer_history_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.volunteer_history_history_id_seq', 7, true);


--
-- TOC entry 4709 (class 2606 OID 16433)
-- Name: usercredentials UserCredentials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usercredentials
    ADD CONSTRAINT "UserCredentials_pkey" PRIMARY KEY (id);


--
-- TOC entry 4711 (class 2606 OID 16442)
-- Name: event_details event_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_details
    ADD CONSTRAINT event_details_pkey PRIMARY KEY (event_id);


--
-- TOC entry 4713 (class 2606 OID 16476)
-- Name: volunteer_history volunteer_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.volunteer_history
    ADD CONSTRAINT volunteer_history_pkey PRIMARY KEY (history_id);


--
-- TOC entry 4716 (class 2606 OID 16482)
-- Name: volunteer_history event_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.volunteer_history
    ADD CONSTRAINT event_id FOREIGN KEY (event_id) REFERENCES public.event_details(event_id);


--
-- TOC entry 4714 (class 2606 OID 16455)
-- Name: event_details user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_details
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.usercredentials(id) NOT VALID;


--
-- TOC entry 4715 (class 2606 OID 16465)
-- Name: user_profile user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_profile
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.usercredentials(id);


--
-- TOC entry 4717 (class 2606 OID 16477)
-- Name: volunteer_history user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.volunteer_history
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.usercredentials(id);


--
-- TOC entry 4718 (class 2606 OID 16491)
-- Name: notifications user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.usercredentials(id);


-- Completed on 2024-07-24 19:54:42

--
-- PostgreSQL database dump complete
--

