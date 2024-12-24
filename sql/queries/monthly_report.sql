-- Example monthly report query
SELECT
  id,
  length(json_data) AS data_length,
  datetime('now')   AS report_date
FROM my_data;
