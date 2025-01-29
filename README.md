# 📊 Analyse des Données GitHub avec DuckDB & dbt

## 🚀 Objectif du Projet
Ce projet permet de collecter, transformer et analyser les données du dépôt **Apache Airflow** sur GitHub.  
Nous utilisons **DuckDB** pour le stockage des données et **dbt** pour leur transformation et modélisation.


---

## 📥 **Collecte des Données**
Nous utilisons l'**API GitHub** pour extraire les données des contributeurs, issues, pull requests et statistiques du dépôt.

### **Exécution des scripts de collecte**
```bash
python scripts/collect_contributors.py
python scripts/collect_issues.py
python scripts/collect_pull_requests.py
python scripts/collect_repo_stats.py
```

Les fichiers .parquet sont stockés dans scripts/data/raw/.

### 🗄️ Chargement des Données dans DuckDB

Une fois les fichiers .parquet générés, nous les chargeons dans DuckDB :

**Sources de données** :

- GET /users
- GET /repos/{owner}/{repo}/commits
- GET /repos/{owner}/{repo}/issues
- GET /repos/{owner}/{repo}/pulls
- GET /orgs/{org}