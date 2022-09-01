from pathlib import Path

EXTENSIONS_MAPPING = {".pdf": "DocPDF",
                      ".doc": "DocWord",
                      ".md": "DocExcel",
                      ".csv": "DocExcel",
                      ".txt": "BlocNote",
                      ".md": "BlocNote"
                      }

BASE_DIR = Path('C:/Users/Geoffrey/Downloads/Downloads2/Documents')
# BASE_DIR2 = BASE_DIR / "Downloads3"
# BASE_DIR2.mkdir(exist_ok=True)
# On récupère tous les fichiers dans le dossier de base
files = [f for f in BASE_DIR.iterdir() if f.is_file()]
# print(files)
for file in files:  # On boucle sur chaque fichier
    # On récupère le dossier cible à partir du dictionnaire
    dossier_cible = EXTENSIONS_MAPPING.get(file.suffix, "Divers")
    # On concatène le dossier de base avec le dossier cible
    dossier_cible_absolu = BASE_DIR / dossier_cible
    # On crée le dossier cible s'il n'existe pas déjà
    dossier_cible_absolu.mkdir(exist_ok=True)
    # On concatène le dossier cible avec le nom du fichier
    fichier_cible = dossier_cible_absolu / file.name
    # On déplace le fichier
    file.rename(fichier_cible)





