-- СТВОРЕННЯ ТАБЛИЦІ
-- СТОВПЧИКИ: НАЗВА, ТИП ДАНИХ
-- В БУДЬ ЯКІЙ ТАБЛИЦІ МАЄ БУТИ ID
-- SERIAL: ЦІЛЕ ЧИСЛО, АВТОМАТИЧНО СТВОРЮЄТЬСЯ

CREATE TABLE PEOPLE(
	PERSON_ID SERIAL PRIMARY KEY,
	PERSON_NAME VARCHAR(50), -- ТЕКСТ, НЕ БІЛЬШЕ 50 СИМВОЛІВ
	AGE INT,                 -- ЦІЛЕ ЧИСЛО
	BIRTH_DAY DATE           -- ДАТА
)

-- ДОДАВАННЯ ДАНИХ У ТАБЛИЦЮ
INSERT INTO PEOPLE(
	PERSON_NAME,
	AGE,
	BIRTH_DAY
)
VALUES
('JOHN', 56, '1973-02-01'),
('ALICE', 38, '1995-04-06'),
('JOHN', 15, '2010-10-25')

--ЗАПИТИ
SELECT * -- СТОВПЧИКИ, ЯКІ ДІСТАТИ, АБО * -- ДЛЯ ВСІХ СТОВПЧИКІВ
FROM PEOPLE -- ТАБЛИЦЯ, З ЯКОЇ ДІСТАВАТИ ДАНІ(СТОВПЧИКИ)

-- ЛИШЕ ІМЕНА
SELECT PERSON_NAME
FROM PEOPLE

-- ЛИШЕ ІМЕНА ТА ВІК
SELECT PERSON_NAME, AGE
FROM PEOPLE

-- ІМЕНА ЛЮДЕЙ БЕЗ ПОВТОРЕНЬ(УНІКАЛЬНІ ІМЕНА)
SELECT DISTINCT PERSON_NAME
FROM PEOPLE

-- ІМЕНА ТА ВІК ЛЮДЕЙ СТАРШИХ ЗА 30
SELECT AGE, PERSON_NAME
FROM PEOPLE
WHERE AGE > 30 -- УМОВА







