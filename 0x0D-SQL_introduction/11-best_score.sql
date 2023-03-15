-- List name and scores >= 10 in decending order in the table second_table
SELECT `score` `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
