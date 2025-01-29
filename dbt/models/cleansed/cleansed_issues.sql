{{ config(materialized='table') }}

WITH raw_issues AS (
    SELECT
        id AS issue_id,
        created_at::timestamp AS created_at,
        closed_at::timestamp AS closed_at,
        state,
        array_to_string(labels, ', ') AS labels
    FROM {{ source('raw', 'issues') }}
    WHERE state IN ('open', 'closed')
)
SELECT * FROM raw_issues;
