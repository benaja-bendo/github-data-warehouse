{{ config(materialized='table') }}

SELECT
    collected_at::timestamp AS collected_at,
    stars,
    forks,
    open_issues,
    subscribers
FROM {{ source('raw', 'repo_stats') }};
