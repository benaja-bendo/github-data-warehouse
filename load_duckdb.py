# import duckdb
# import glob
#
# conn = duckdb.connect("airflow_warehouse.db")
#
# # Création du schéma raw
# conn.execute("CREATE SCHEMA IF NOT EXISTS raw;")
#
# # Chargement de tous les fichiers Parquet
# for parquet_file in glob.glob("data/raw/*.parquet"):
#     table_name = f"raw.{parquet_file.split('/')[-1].replace('.parquet', '')}"
#
#     conn.execute(f"""
#         CREATE OR REPLACE TABLE {table_name}
#         AS SELECT * FROM read_parquet('{parquet_file}');
#     """)
#
# # Vérification
# print(conn.sql("SHOW TABLES FROM raw;"))

import duckdb
import os

# ✅ Correction du chemin de la base DuckDB
DB_PATH = "airflow_warehouse.db"

# ✅ Définition du dossier contenant les fichiers Parquet
RAW_DATA_DIR = "data/raw"

# ✅ Vérifier que le dossier `data/raw` existe avant de continuer
if not os.path.exists(RAW_DATA_DIR):
    raise FileNotFoundError(f"Le dossier {RAW_DATA_DIR} n'existe pas.")

# ✅ Connexion à DuckDB
conn = duckdb.connect(DB_PATH)

# ✅ Création du schéma raw s'il n'existe pas
conn.execute("CREATE SCHEMA IF NOT EXISTS raw;")

# ✅ Liste des fichiers Parquet et leurs tables correspondantes
parquet_files = {
    "raw_contributors.parquet": "contributors",
    "raw_issues.parquet": "issues",
    "raw_pull_requests.parquet": "pull_requests",
    "raw_repo_stats.parquet": "repo_stats",
}

# ✅ Chargement des fichiers Parquet dans DuckDB
for file_name, table_name in parquet_files.items():
    file_path = os.path.join(RAW_DATA_DIR, file_name)
    if os.path.exists(file_path):
        print(f"📥 Chargement du fichier {file_name} dans la table raw.{table_name}...")
        conn.execute(f"""
            CREATE OR REPLACE TABLE raw.{table_name} AS 
            SELECT * FROM read_parquet('{file_path}');
        """)
    else:
        print(f"⚠️ Fichier {file_name} introuvable. Il sera ignoré.")

# ✅ Vérification du contenu des tables
print("\n📊 Vérification des premières lignes de chaque table :")
for table in parquet_files.values():
    print(f"\n🔍 Table raw.{table}:")
    result = conn.execute(f"SELECT * FROM raw.{table} LIMIT 5").fetchdf()
    print(result)

# ✅ Fermeture de la connexion
conn.close()

print("\n✅ Chargement terminé avec succès !")
