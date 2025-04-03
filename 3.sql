SELECT *
FROM PEOPLE
--WHERE

--SELECT МОЖЕ БУТИ НЕ СТОВПЧИК А ВИРАЗ
SELECT AGE*10 + 5
FROM PEOPLE

-- РОБОТА З РЯДКАМИ
-- ВИБРАТИ ЛЮДЕЙ З ІМ'ЯМ JHON

SELECT *
FROM PEOPLE
WHERE PERSON_NAME = 'JOHN'


-- РЕГУЛЯРНІ ВИРАЗИ(REGULAR EXPRESSIONS)
-- _ - ДОВІЛЬНИЙ СИМВОЛ ОДИН РАЗ

-- ІМЕНА З 4-ОХ ЛІТЕР
SELECT *
FROM PEOPLE
WHERE PERSON_NAME LIKE '____'

-- ІМЕНА ПОЧИНАЮТЬСЯ НА J, ВСЬОГО 4 ЛІТЕРИ
SELECT *
FROM PEOPLE
WHERE PERSON_NAME LIKE 'J___'

-- % - ДОВІЛЬНІ СИМВОЛИ, ДОВІЛЬНУ КІЛЬКІСТЬ РАЗІВ(ВКЛЮЧНО З НУЛЕМ)

-- ІМЕНА ПОЧИНАЮТЬСЯ НА J
SELECT *
FROM PEOPLE
WHERE PERSON_NAME LIKE 'J%'


-- ІМЕНА ПОЧИНАЮТЬСЯ НА J, ЗАКІНЧУЄТЬСЯ НА а
SELECT *
FROM PEOPLE
WHERE PERSON_NAME LIKE 'J%a'

-- ІМЕНА ЯКІ МІСТЯТЬ БУКВУ е
SELECT *
FROM PEOPLE
WHERE PERSON_NAME LIKE '%e%'

-- ІМЕНА ЯКІ МІСТЯТЬ 2 БУКВИ е
SELECT *
FROM PEOPLE
WHERE PERSON_NAME LIKE '%e%e%'

-- ІМЕНА В НИЖНЬОМУ РЕГІСТРІ
SELECT LOWER(PERSON_NAME)
FROM PEOPLE
WHERE LOWER(PERSON_NAME) = 'john'


-- ЛЮДИ ВІКОМ ВІД 20 ДО 30
SELECT *
FROM PEOPLE
--WHERE AGE >= 20 AND AGE <= 30
WHERE AGE BETWEEN 20 AND 30



-- ОТРИМАТИ ВІК ЛЮДИНИ ПО ДАТІ НАРОДЖЕННЯ
SELECT AGE(BIRTH_DAY)
FROM PEOPLE



-- ОТРИМАТИ ЛИЩЕ РІК
SELECT EXTRACT(YEAR FROM AGE(BIRTH_DAY)), AGE
FROM PEOPLE














