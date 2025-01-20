import os
import time
import google.generativeai as genai
from tkinter import *
from tkinter import messagebox, scrolledtext
from gtts import gTTS
import re
from PIL import Image, ImageTk  # Pour gérer les icônes

# Liste des niches (100 niches ajoutées)
niches = [
    "Motivation", "Développement personnel", "Finance", "Santé", "Éducation", "Technologie", "Voyage",
    "Cuisine", "Sport", "Entrepreneuriat", "Leadership", "Spiritualité", "Bien-être", "Productivité",
    "Psychologie", "Relations", "Innovation", "Histoire", "Art", "Science", "Musique", "Mode", "Société",
    "Environnement", "Politique", "Agriculture", "Écologie", "Bâtiment", "Architecture", "Aviation",
    "Brevets", "Industrie", "Marketing", "Commerce", "Finance personnelle", "Cryptomonnaies", "Bitcoin",
    "Investissement", "Culture", "Design", "Cuisine santé", "Alimentation", "Fitness", "Coaching", "Création",
    "Startups", "Technologie numérique", "Intelligence artificielle", "Blockchain", "E-commerce", "Réseaux sociaux",
    "Sécurité informatique", "Réseautage", "Consulting", "Éthique", "Développement durable", "Automatisation",
    "Big data", "Cloud computing", "Objectifs", "Analyse de données", "Bien-être mental", "Techniques de relaxation",
    "Art de vivre", "Finance durable", "Planification", "Stratégie", "Innovation sociale", "Croissance", "Savoir-être",
    "Développement des compétences", "Reconnaissance", "Communication", "Leadership inclusif", "Réseautage professionnel",
    "Créativité", "Génie industriel", "Télétravail", "Transformation digitale", "Web design", "Formation", "Apprentissage",
    "Compétences interpersonnelles", "Gestion du temps", "Finances écologiques", "Nouvelles technologies", "Startup innovations",
    "Mindfulness", "Développement économique", "Science-fiction", "Écriture créative", "Art digital", "Développement communautaire",
    "Futurs possibles", "Téléphonie", "Services financiers", "Commerce électronique", "Publicité", "Énergie renouvelable",
    "Mobilité", "Transport", "Agriculture durable", "Technologies médicales", "Énergie solaire", "Energies vertes", "Nouvelles pratiques",
    "Médias sociaux", "Marketing digital", "Photographie", "Gestion de projet", "Design UX/UI", "Industrie automobile", "Robots", "Cuisine créative",
    "Économie circulaire", "Recyclage", "Fintech", "Nouvelles formes d'éducation", "Futur du travail", "Energie hydrogène", "Énergie éolienne", "Villes intelligentes"
]

# Fonction pour générer le texte
def generate_text(api_key, words_per_minute, niche, language, duration_seconds, user_prompt):
    genai.configure(api_key=api_key)

    # Calculer le nombre de mots basé sur la durée
    total_words = words_per_minute * (duration_seconds / 60)

    # Créer le prompt final avec la langue et la durée, et ajouter le prompt personnalisé de l'utilisateur
    prompt_text = f"Génère un texte de {int(total_words)} mots sur le sujet '{niche}' en {language}. {user_prompt}"

    try:
        # Appel à l'API pour générer le texte
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Langue : {language}. {prompt_text}")
       
        return response.text

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
        return None

# Fonction pour générer des hashtags basés sur un prompt utilisateur
def generate_hashtags_prompt(api_key, user_prompt):
    genai.configure(api_key=api_key)

    try:
        # Créer un prompt pour la génération de hashtags
        prompt_text = f"En utilisant le texte suivant, génère des hashtags pertinents : {user_prompt}"
       
        # Appel à l'API pour générer les hashtags
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"{prompt_text}")

        # Supposons que Gemini retourne directement des hashtags sous forme de texte
        hashtags = response.text.strip()
        return hashtags

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
        return None

# Fonction pour convertir le texte en audio
def convert_text_to_audio(text):
    try:
        # Créer un nom unique basé sur l'heure actuelle
        timestamp = int(time.time())
        audio_path = os.path.join("output", f"audio_{timestamp}.mp3")
       
        tts = gTTS(text, lang='fr')
        tts.save(audio_path)
       
        return audio_path
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de la conversion du texte en audio : {e}")
        return None

# Interface utilisateur avec Tkinter
def main():
    api_key = "AIzaSyAbnVb7QGv8DLHk4neRF0MoLJow_jsraiE"  # Remplacez par votre clé API Gemini

    root = Tk()
    root.title("Générateur de texte AI")

    # Création du dossier "output" si nécessaire
    if not os.path.exists("output"):
        os.makedirs("output")

    # Chargement d'une icône pour le bouton
    icon_path = "hashtag_icon.png"  # Assurez-vous que cette image existe
    try:
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20))  # Redimensionner l'icône si nécessaire
        icon_tk = ImageTk.PhotoImage(icon_image)
    except:
        icon_tk = None

    # Interface pour entrer les informations
    Label(root, text="Durée (en secondes) :").pack()
    duration_var = Entry(root, width=20)
    duration_var.pack()

    Label(root, text="Choisissez la niche :").pack()
    niche_var = StringVar(value=niches[0])
    niche_menu = OptionMenu(root, niche_var, *niches)
    niche_menu.pack()

    Label(root, text="Choisissez la langue :").pack()
    language_var = StringVar(value="Français")
    language_menu = OptionMenu(root, language_var, "Français", "Anglais", "Espagnol", "Allemand", "Italien", "Portugais", "Néerlandais", "Arabe", "Chinois",
    "Japonais", "Coréen", "Russe", "Hindi", "Bengali", "Turc", "Polonais", "Suédois", "Norvégien", "Danois",
    "Finlandais", "Grec", "Tchèque", "Hongrois", "Roumain", "Indonésien", "Malais", "Thaïlandais")
    language_menu.pack()

    Label(root, text="Vitesse (mots par minute) :").pack()
    speed_var = StringVar(value="160")
    speed_entry = Entry(root, textvariable=speed_var)
    speed_entry.pack()

    Label(root, text="Entrez votre prompt personnalisé pour le texte :").pack()
    prompt_textbox = scrolledtext.ScrolledText(root, width=40, height=5)
    prompt_textbox.pack()

    # Interface pour entrer un prompt pour les hashtags
    Label(root, text="Entrez votre prompt personnalisé pour les hashtags :").pack()
    hashtags_prompt_textbox = scrolledtext.ScrolledText(root, width=40, height=5)
    hashtags_prompt_textbox.pack()

    # Fonction pour générer le texte et convertir en audio
    def on_generate():
        # Récupérer les données de l'utilisateur
        niche = niche_var.get()
        language = language_var.get()
        words_per_minute = int(speed_var.get())
        duration_seconds = int(duration_var.get())
        user_prompt = prompt_textbox.get("1.0", END).strip()

        if not user_prompt:
            messagebox.showerror("Erreur", "Vous devez entrer un prompt pour le texte.")
            return

        if duration_seconds <= 0:
            messagebox.showerror("Erreur", "La durée doit être un nombre positif.")
            return

        # Générer le texte avec Gemini
        generated_text = generate_text(api_key, words_per_minute, niche, language, duration_seconds, user_prompt)

        if generated_text:
            # Afficher le texte généré à l'utilisateur dans un champ éditable
            text_window = Toplevel(root)
            text_window.title("Texte généré")
            text_box = scrolledtext.ScrolledText(text_window, width=40, height=10)
            text_box.insert(INSERT, generated_text)
            text_box.pack()

            # Sauvegarder le texte dans un fichier
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            text_file_path = os.path.join(desktop_path, "texte_genere.txt")
            with open(text_file_path, "w", encoding="utf-8") as f:
                f.write(generated_text)

            messagebox.showinfo("Sauvegarde", f"Le texte a été sauvegardé sous : {text_file_path}")

            # Permettre la révision du texte avant de le convertir en audio
            def on_convert_audio():
                text_to_convert = text_box.get("1.0", END).strip()
                # Convertir en audio
                audio_path = convert_text_to_audio(text_to_convert)
                if audio_path:
                    messagebox.showinfo("Audio généré", f"L'audio a été généré et sauvegardé sous {audio_path}")
                text_window.destroy()

            # Bouton pour générer l'audio à partir du texte corrigé
            convert_audio_button = Button(text_window, text="Convertir en Audio", command=on_convert_audio)
            convert_audio_button.pack()

    # Fonction pour générer les hashtags
    def on_generate_hashtags():
        hashtags_prompt = hashtags_prompt_textbox.get("1.0", END).strip()

        if not hashtags_prompt:
            messagebox.showerror("Erreur", "Vous devez entrer un prompt pour les hashtags.")
            return

        hashtags = generate_hashtags_prompt(api_key, hashtags_prompt)

        if hashtags:
            hashtags_window = Toplevel(root)
            hashtags_window.title("Hashtags générés")
            hashtags_box = scrolledtext.ScrolledText(hashtags_window, width=40, height=5)
            hashtags_box.insert(INSERT, hashtags)
            hashtags_box.pack()

            # Sauvegarder les hashtags dans un fichier
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            hashtags_file_path = os.path.join(desktop_path, "hashtags_genere.txt")
            with open(hashtags_file_path, "w", encoding="utf-8") as f:
                f.write(hashtags)

            messagebox.showinfo("Sauvegarde", f"Les hashtags ont été sauvegardés sous : {hashtags_file_path}")

    # Bouton pour générer le texte
    generate_button = Button(root, text="Générer le texte", command=on_generate)
    generate_button.pack(pady=10)

    # Bouton pour générer les hashtags avec l'icône
    generate_hashtags_button = Button(root, text="Générer les Hashtags", command=on_generate_hashtags, image=icon_tk, compound="left")
    generate_hashtags_button.pack(pady=10)

    root.mainloop()

# Lancer l'application
if __name__ == "__main__":
    main()

