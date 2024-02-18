-- Lists the top 3 cities' temperatures in July and August,
-- ordered by temperature in descending order.
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
