"""
The API configurations are grouped in this file.
"""

# the list of categories
OFF_CATS = {
    "categories": [
        "Pâtes à tartiner au chocolat",
        "Barres chocolatées",
        "Mueslis au chocolat",
        "Chocolats en poudre",
        "Confitures de fruits",
        "Barres de fruits à coques",
        "Barres de céréales",
        "Quiches",
        "Pizzas",
        "Céréales pour petit-déjeuner",
        "Biscuits",
        "Salades composées",
        "Desserts",
        "Aliments d'origine végétale",
        "Compotes",
    ]
}

# API configuration
API_CONFIG = {
    "url": "https://fr.openfoodfacts.org/cgi/search.pl",
    "criteria": {
      "action": "process",
      "tagtype_0": "categories",
      "tag_contains_0": "contains",
      "tag_0": "category",
      "tagtype_1": "nutrition_grades",
      "tag_contains_1": "contains",
      "tag_1": "grades",
      "sort_by": "unique_scans_n",
      "page_size": "100",
      "json": "1"
    },
    "nutrition_grades": "abcde"
}
