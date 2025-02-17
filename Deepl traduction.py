import deepl 

# Initialisation du traducteur
translator = deepl.Translator('xxxxx')

# Liste des langues disponibles
languages = {
    1: 'BG', 2: 'CS', 3: 'DA', 4: 'DE', 5: 'EL', 6: 'EN-GB', 7: 'EN-US',
    8: 'ES', 9: 'ET', 10: 'FI', 11: 'FR', 12: 'HU', 13: 'ID', 14: 'IT',
    15: 'JA', 16: 'LT', 17: 'LV', 18: 'NL', 19: 'PL', 20: 'PT-BR', 21: 'PT-PT',
    22: 'RO', 23: 'RU', 24: 'SK', 25: 'SL', 26: 'SV', 27: 'TR', 28: 'UK',
    29: 'ZH'
}

# Affichage du texte et des options de langue
text = input("Quel est le texte que vous souhaitez traduire ? ")
print("""
    1 - Bulgarian
    2 - Czech
    3 - Danish
    4 - German
    5 - Greek
    6 - English (British)
    7 - English (American)
    8 - Spanish
    9 - Estonian
    10 - Finnish
    11 - French
    12 - Hungarian
    13 - Indonesian
    14 - Italian
    15 - Japanese
    16 - Lithuanian
    17 - Latvian
    18 - Dutch
    19 - Polish
    20 - Portuguese (Brazilian)
    21 - Portuguese (all Portuguese varieties excluding Brazilian Portuguese)
    22 - Romanian
    23 - Russian
    24 - Slovak
    25 - Slovenian
    26 - Swedish
    27 - Turkish
    28 - Ukrainian
    29 - Chinese (simplified)
""")

# Saisie du choix de langue
try:
    chosen_element = int(input("Enter a number from 1 to 29: "))
    if chosen_element in languages:
        target_language = languages[chosen_element]
        result = translator.translate_text(text, target_lang=target_language)
        print("Texte traduit :", result.text)
    else:
        print("Veuillez choisir une valeur entre 1 et 29. Veuillez réessayer.")
except ValueError:
    print("Entrée invalide. Veuillez entrer un numéro.")
