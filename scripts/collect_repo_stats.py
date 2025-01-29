import os
import requests
import polars as pl
from datetime import datetime

from utils.auth import get_github_headers


def fetch_repo_stats():
    response = requests.get(
        "https://api.github.com/repos/apache/airflow",
        headers=get_github_headers()
    )
    response.raise_for_status()

    stats = response.json()
    df = pl.DataFrame({
        "collected_at": [datetime.now().isoformat()],
        "stars": [stats["stargazers_count"]],
        "forks": [stats["forks_count"]],
        "open_issues": [stats["open_issues"]],
        "subscribers": [stats["subscribers_count"]]
    })

    # ✅ Vérifier et créer le dossier s'il n'existe pas
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Sauvegarder le fichier parquet
    df.write_parquet(os.path.join(output_dir, "raw_repo_stats.parquet"))


if __name__ == "__main__":
    fetch_repo_stats()
