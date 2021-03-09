SELECT ANIMAL_OUTS.ANIMAL_ID AS ANIMAL_ID, ANIMAL_OUTS.NAME AS NAME 
FROM ANIMAL_OUTS 
INNER JOIN ANIMAL_INS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
ORDER BY ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME DESC
LIMIT 2