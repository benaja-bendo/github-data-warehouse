import os
import requests
import polars as pl

from utils.pagination import paginated_get


def fetch_issues():
    issues = paginated_get(
        "https://api.github.com/repos/apache/airflow/issues",
        # params={"state": "all"}
    )

    df = pl.DataFrame({
        "id": [issue["number"] for issue in issues],
        "created_at": [issue["created_at"] for issue in issues],
        "closed_at": [issue.get("closed_at") for issue in issues],
        "state": [issue["state"] for issue in issues],
        "labels": [[label["name"] for label in issue["labels"]] for issue in issues]
    })

    # ✅ Vérifier et créer le dossier s'il n'existe pas
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Sauvegarder le fichier parquet
    df.write_parquet(os.path.join(output_dir, "raw_issues.parquet"))


if __name__ == "__main__":
    fetch_issues()
