# import requests
# from time import sleep
# from typing import List, Dict
# from scripts.utils.auth import get_github_headers
#
#
#
# def paginated_get(url: str, params: dict = None) -> List[Dict]:
#     results = []
#     page = 1
#
#     while True:
#         response = requests.get(
#             url,
#             params={**(params or {}), "page": page, "per_page": 100},
#             headers=get_github_headers()
#         )
#
#         if response.status_code == 403:
#             sleep(60)  # Gestion des rate limits
#             continue
#
#         response.raise_for_status()
#         data = response.json()
#
#         if not data:
#             break
#
#         results.extend(data)
#         page += 1
#         sleep(1)  # Respect des limites de l'API
#
#     return results

import requests


def paginated_get(url, headers=None, per_page=100):
    results = []
    page = 1

    while True:
        response = requests.get(
            f"{url}?page={page}&per_page={per_page}",
            headers=headers
        )

        if response.status_code == 401:
            raise ValueError("Erreur 401: Vérifiez votre token GitHub.")

        response.raise_for_status()

        data = response.json()
        if not data:
            break

        results.extend(data)
        page += 1

    return results
