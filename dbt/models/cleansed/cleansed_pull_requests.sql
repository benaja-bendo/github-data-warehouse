{{ config(materialized='table') }}

SELECT
    pr_number,
    merged_at::timestamp AS merged_at
FROM {{ source('raw', 'pull_requests') }}
WHERE merged_at IS NOT NULL;
