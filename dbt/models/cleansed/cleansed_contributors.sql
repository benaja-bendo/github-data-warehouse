{{ config(materialized='table') }}

SELECT
    login,
    contributions,
    organization
FROM {{ source('raw', 'contributors') }}
WHERE login IS NOT NULL;
