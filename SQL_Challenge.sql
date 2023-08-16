/*--Assignement--
Write the query that only returns the email_address column
Join the tables together using the join_id column present in both tables
Column_1 needs to be divisible by 2 without creating a decimal number (or modulo)
column_2 needs to be smaller then column_1
Column_3 needs to end with a 1 */

/*--Given starting setup created--
  --Given starting data created--*/

SELECT EMAIL
FROM DATA_TABLE
INNER JOIN EMAIL_TABLE ON DATA_TABLE.JOIN_ID = EMAIL_TABLE.JOIN_ID
WHERE (COLUMN_1 % 2) = 0
AND COLUMN_1 > COLUMN_2
AND RIGHT(COLUMN_3 ,1) REGEXP '1';
