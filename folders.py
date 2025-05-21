import os

FOLDER_DIR = "/Applications/MAMP/htdocs/fortnite-maps-archives"

def detect_deepest_folders(path):
    try:
        # Obtenir tous les sous-dossiers du dossier actuel
        # Obtain every sub folders from the actual folder
        sub_folders = [f.path for f in os.scandir(path) if f.is_dir() and not f.name.startswith('.')]

        # Si aucun sous-dossier → on est au bout
        # If we found no sub folder → we are at the end
        if not sub_folders:
            print(f"📁 Final folder found : {path}")
            # → On affiche les fichiers présents
            # → We display all files existing
            files = [f.name for f in os.scandir(path) if f.is_file() and not f.name.startswith('.')]
            if files:
                print("📄 Files founded :")
                for file in files:
                    # On récupére le nom sans extension
                    # We get the name without the extension
                    file_name_without_ext = os.path.splitext(file)[0]
                    # On définit le nom et le chemin du dossier
                    # We define the folder path and the name he'll get
                    folder_path = os.path.join(path, file_name_without_ext)
                    complete_file_path = os.path.join(path, file)
                    # Vérifier si le dossier n'existe pas déjà
                    # Verify if the folder isn't existing already
                    if not os.path.exists(folder_path):
                        # Si ca n'existe pas, on le créer
                        # If it doesn't exist, we create it
                        os.mkdir(folder_path)
                        print(f"     📂 Created folder: {folder_path}")
                        # Au final, on déplace le fichier dans son nouveau dossier (du même nom)
                        # Finally, we move the file in his new folder (which have the same name)
                        complete_new_file_path = os.path.join(folder_path, file)
                        os.replace(complete_file_path, complete_new_file_path)
                        print(f"     ✅ Your file has been moved")
                    else:
                        print(f"     ⚠️ Folder already exists: {folder_path}")
            else:
                print("   (No file found)")
            print("-" * 40)
            return
        
        # Sinon on continue la détection afin de trouver le dernier sous-dossier
        # Or we continue detecting until we find the last sub folder
        for folder in sub_folders:
            detect_deepest_folders(folder)

    except Exception as e:
        print(f"Erreur en parcourant {path} : {e}")

detect_deepest_folders(FOLDER_DIR)
