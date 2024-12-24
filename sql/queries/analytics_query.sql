-- Example analytics query
SELECT
  JSON_EXTRACT(json_data, '$.uuid') AS uuid,
  JSON_EXTRACT(json_data, '$.company.name') AS companyName,
  JSON_EXTRACT(json_data, '$.roles')       AS roles
FROM my_data;
