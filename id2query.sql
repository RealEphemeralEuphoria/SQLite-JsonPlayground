SELECT 
  json_extract(value, '$.id') AS id,
  json_extract(value, '$.name') AS name,
  json_extract(value, '$.role') AS role,
  json_extract(value, '$.salary') AS salary
FROM 
  raw_json, 
  json_each(raw_json.data)
WHERE 
  json_extract(value, '$.role') = 'DevOps';
