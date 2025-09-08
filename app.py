
from typing import Dict, Iterable, Tuple, List
from langdetect import detect

def to_one_to_one_mapping(grouped: Dict[int, Iterable[str]]) -> Dict[str, int]:
    """
    Convierte el formato 'puntaje -> [letras]' a 'letra -> puntaje',
    normalizando letras a minúsculas y validando duplicados.
    """
    one_to_one: Dict[str, int] = {}

    for points, letters in grouped.items():
        for ch in letters:
            ch_low = ch.lower()
            if ch_low in one_to_one and one_to_one[ch_low] != points:
                raise ValueError(
                    f"Conflicto: la letra '{ch_low}' ya tenía puntaje "
                    f"{one_to_one[ch_low]} y ahora intenta asignarse {points}"
                )
            one_to_one[ch_low] = points

    return one_to_one


def score_word(points_map: Dict[str, int], word: str) -> int:
    """
    Calcula el puntaje de 'word' usando 'points_map' (letra->puntaje).
    Ignora caracteres no alfabéticos.
    """
    total = 0
    for ch in word.lower():
        if ch.isalpha():
            total += points_map.get(ch, 0)
    return total



# Diccionarios de puntaje por idioma
grouped_points_en = {
    1: ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"),
    2: ("D", "G"),
    3: ("B", "C", "M", "P"),
    4: ("F", "H", "V", "W", "Y"),
    5: ("K",),
    8: ("J", "X"),
    10: ("Q", "Z"),
}

grouped_points_es = {
    1: ("A", "E", "O", "S", "I", "U", "N", "L", "R", "T"),
    2: ("D", "G"),
    3: ("B", "C", "M", "P"),
    4: ("F", "H", "V", "Y"),
    5: ("K",),
    8: ("J", "X"),
    10: ("Q", "Z"),
    6: ("Ñ",),
    7: ("LL", "CH"),
}

grouped_points_de = {
    1: ("E", "N", "S", "I", "R", "A", "T", "D", "H", "U"),
    2: ("L", "C", "G"),
    3: ("M", "O", "B"),
    4: ("W", "F", "K", "Z"),
    6: ("V", "P"),
    8: ("J", "Y"),
    10: ("Q", "X"),
}

letter_points_en = to_one_to_one_mapping(grouped_points_en)
letter_points_es = to_one_to_one_mapping(grouped_points_es)
letter_points_de = to_one_to_one_mapping(grouped_points_de)

LANG_MAP = {
    'en': letter_points_en,
    'es': letter_points_es,
    'de': letter_points_de,
}

LANG_NAMES = {
    'en': 'Inglés',
    'es': 'Español',
    'de': 'Alemán',
}

def get_language(word: str) -> str:
    try:
        lang = detect(word)
        if lang in LANG_MAP:
            return lang
        else:
            return 'en'  # Por defecto inglés si no se reconoce
    except Exception:
        return 'en'

while True:
    palabra = input("Ingresa una palabra (o 'salir' para terminar): ").strip()
    if palabra.lower() == 'salir':
        print("¡Hasta luego!")
        break
    idioma = get_language(palabra)
    puntos_letras = LANG_MAP[idioma]
    puntaje = score_word(puntos_letras, palabra)
    print(f"Idioma detectado: {LANG_NAMES.get(idioma, idioma)}")
    print(f"Puntaje de '{palabra}': {puntaje}")
