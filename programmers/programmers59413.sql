SET @time = -1;
SELECT 
    (@time := @time + 1) AS 'HOUR', 
    (
        SELECT COUNT(*) FROM ANIMAL_OUTS 
        WHERE HOUR(DATETIME) = @time
    ) AS 'COUNT' 
    FROM ANIMAL_OUTS 
    WHERE @time < 23