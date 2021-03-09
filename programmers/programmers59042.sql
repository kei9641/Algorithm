SELECT ANIMAL_OUTS.ANIMAL_ID AS ANIMAL_ID, ANIMAL_OUTS.NAME AS NAME 
FROM ANIMAL_OUTS 
LEFT JOIN ANIMAL_INS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
WHERE ANIMAL_INS.NAME IS NULL AND ANIMAL_OUTS.NAME IS NOT NULL 
ORDER BY ANIMAL_OUTS.ANIMAL_ID