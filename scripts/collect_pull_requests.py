import os

import polars as pl

from utils.pagination import paginated_get


def fetch_pull_requests():
    prs = paginated_get(
        "https://api.github.com/repos/apache/airflow/pulls",
        # params={"state": "all"}
    )

    df = pl.DataFrame({
        "pr_number": [pr["number"] for pr in prs],
        "merged_at": [pr.get("merged_at") for pr in prs],
        # "comments": [pr["comments"] for pr in prs],
        # "additions": [pr["additions"] for pr in prs],
        # "deletions": [pr["deletions"] for pr in prs]
    })

    # ✅ Vérifier et créer le dossier s'il n'existe pas
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Sauvegarder le fichier parquet
    df.write_parquet(os.path.join(output_dir, "raw_pull_requests.parquet"))


if __name__ == "__main__":
    fetch_pull_requests()
