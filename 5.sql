-- ТАБЛИЦЯ.СТОВПЧИК
SELECT DOCTORS.NAME
FROM DOCTORS

-- КОРОТКА НАЗВА ТАБЛИЦІ
SELECT DOC.NAME
FROM DOCTORS DOC

-- ВИВЕСТИ ДАНІ ПРО ЛІКАРІВ ТА ЇХНІ ВАКАНСІЇ
SELECT *
FROM DOCTORS JOIN VACATIONS ON VACATIONS.DOCTORID = DOCTORS.ID

-- ВИВЕСТИ ДАНІ ПРО ЛІКАРІВ ТА ЇХНІ ВАКАНСІЇ, ЩО ПОЧИНАЮТЬСЯ ПІСЛЯ 2025-03-10
SELECT *
FROM DOCTORS JOIN VACATIONS ON VACATIONS.DOCTORID = DOCTORS.ID
WHERE STARTDATE > '2025-03-10'


--ВІДДІЛЕННЯ, СПОНСОРИ ТА ПОЖЕРТВУВАННЯ
SELECT *
FROM Donations 
	JOIN DEPARTMENTS ON Donations.DEPARTMENTID = DEPARTMENTS.ID
	JOIN SPONSORS ON Donations.SPONSORID = SPONSORS.ID
--WHERE DEPARTMENTS.NAME = 'Кафедра анатомії'
WHERE AMOUNT > 1000
















	