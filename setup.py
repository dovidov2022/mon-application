from setuptools import setup, find_packages

setup(
    name="mon_projet_ai",  # Nom de votre projet
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'tornado',  # Dépendance Tornado
        'flask',  # Si vous utilisez Flask dans d'autres parties de votre projet
        'gTTS',   # Si vous utilisez gTTS
        'Pillow',  # Si vous utilisez Pillow pour les images
        'google-generativeai',  # Si vous utilisez l'API Gemini
    ],
)
