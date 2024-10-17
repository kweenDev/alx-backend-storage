-- Task 2: Rank country origins of bands by number of fans
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;
