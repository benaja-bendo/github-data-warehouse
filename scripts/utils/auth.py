import os

def get_github_headers():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("Le token GitHub n'est pas défini dans les variables d'environnement.")

    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }