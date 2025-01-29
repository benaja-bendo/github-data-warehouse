{{ config(materialized='table') }}

WITH raw_prs AS (
    SELECT
        pr_number,
        merged_at::timestamp AS merged_at,
        comments,
        additions,
        deletions
    FROM {{ source('raw', 'pull_requests') }}
    WHERE merged_at IS NOT NULL
)
SELECT * FROM raw_prs;
