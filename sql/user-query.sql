-- User needs to be able to run the following query

SELECT *
FROM PipelineReport p
JOIN MimosaStatus m ON p.ID = m.ID
WHERE p.year = {$year} AND p.month = {$month} AND p.day = {$day}
