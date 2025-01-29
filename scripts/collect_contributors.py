import os

import requests
import polars as pl

from scripts.utils.pagination import paginated_get
from utils.auth import get_github_headers



def fetch_contributors():
    headers = get_github_headers()  # Récupération des headers avec le token

    contributors = paginated_get(
        url="https://api.github.com/repos/apache/airflow/contributors",
        headers=headers  # Ajout des headers ici
    )

    orgs = []
    for contributor in contributors:
        user_data = requests.get(
            contributor["url"],
            headers=headers  # Ajout des headers ici aussi
        ).json()
        orgs.append(user_data.get("company"))

    df = pl.DataFrame({
        "login": [c["login"] for c in contributors],
        "contributions": [c["contributions"] for c in contributors],
        "organization": orgs
    })

    # ✅ Vérifier et créer le dossier s'il n'existe pas
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Sauvegarder le fichier dans le dossier
    df.write_parquet(os.path.join(output_dir, "raw_contributors.parquet"))

    # df.write_parquet("data/raw/raw_contributors.parquet")


if __name__ == "__main__":
    fetch_contributors()