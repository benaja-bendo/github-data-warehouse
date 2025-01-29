{{ config(materialized='table') }}

WITH raw_contributors AS (
    SELECT
        login,
        contributions,
        organization
    FROM {{ source('raw', 'contributors') }}
    WHERE login IS NOT NULL
)
SELECT * FROM raw_contributors;
