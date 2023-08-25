import os
import requests

base_url = "https://szs.ch/wp-content/uploads/"

response = requests.get(base_url)
if response.status_code == 200:
    # Analyser la page pour extraire les noms de fichiers ou les liens vers les fichiers
    # Utilisez des bibliothèques comme BeautifulSoup si la page est HTML

    # Une fois que vous avez la liste des noms de fichiers ou des liens, parcourez-la
    for file_link in list_of_file_links:
        file_url = base_url + file_link
        file_response = requests.get(file_url)
        if file_response.status_code == 200:
            # Assurez-vous d'ajuster le chemin de sauvegarde en fonction de votre configuration
            save_path = os.path.join("downloaded_files", file_link)
            with open(save_path, "wb") as f:
                f.write(file_response.content)
            print(f"Fichier {file_link} téléchargé avec succès.")
        else:
            print(f"Échec du téléchargement du fichier {file_link}. Code d'état : {file_response.status_code}")
else:
    print("Échec de la requête de base. Code d'état :", response.status_code)
