# Word Score Game 🎯

Un juego interactivo de puntuación de palabras que calcula el puntaje de las palabras basándose en el valor de sus letras, similar al sistema de puntuación del Scrabble. El juego incluye detección automática de idioma y soporte para múltiples lenguajes.

## 🌟 Características

- **Detección automática de idioma**: Detecta automáticamente si la palabra está en inglés, español o alemán
- **Sistema de puntuación multiidioma**: Cada idioma tiene su propio sistema de puntuación de letras
- **Interfaz de línea de comandos**: Fácil de usar desde la terminal
- **Puntuación en tiempo real**: Calcula instantáneamente el puntaje de cualquier palabra
- **Soporte para caracteres especiales**: Maneja correctamente letras con tildes y caracteres únicos de cada idioma

## 🛠️ Requisitos del Sistema

- **Python 3.6 o superior**
- **pip** (gestor de paquetes de Python)
- **Conexión a internet** (para la instalación inicial de dependencias)

## 📥 Instalación Local

### 1. Clonar el Repositorio

```bash
git clone https://github.com/IronMike524/Word_Score_Game.git
cd Word_Score_Game
```

### 2. Verificar la Versión de Python

```bash
python3 --version
```

*Nota: Asegúrate de tener Python 3.6 o superior instalado*

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

**¿Qué se instala?**
- `langdetect`: Biblioteca para la detección automática del idioma de las palabras

### 4. Ejecutar el Juego

```bash
python3 app.py
```

## 🎮 Cómo Usar

1. **Iniciar el juego**: Ejecuta `python3 app.py`
2. **Ingresar palabras**: Escribe cualquier palabra cuando se te solicite
3. **Ver resultados**: El juego mostrará:
   - El idioma detectado
   - El puntaje total de la palabra
4. **Salir**: Escribe `salir` para terminar el juego

### Ejemplo de Uso

```
$ python3 app.py
Ingresa una palabra (o 'salir' para terminar): hello
Idioma detectado: Inglés
Puntaje de 'hello': 8

Ingresa una palabra (o 'salir' para terminar): hola
Idioma detectado: Español
Puntaje de 'hola': 4

Ingresa una palabra (o 'salir' para terminar): hallo
Idioma detectado: Alemán
Puntaje de 'hallo': 9

Ingresa una palabra (o 'salir' para terminar): salir
¡Hasta luego!
```

## 🌍 Idiomas Soportados

### Inglés (English)
- **Detección**: `en`
- **Letras de 1 punto**: A, E, I, O, U, L, N, R, S, T
- **Letras de 2 puntos**: D, G
- **Letras de 3 puntos**: B, C, M, P
- **Letras de 4 puntos**: F, H, V, W, Y
- **Letras de 5 puntos**: K
- **Letras de 8 puntos**: J, X
- **Letras de 10 puntos**: Q, Z

### Español (Spanish)
- **Detección**: `es`
- **Letras de 1 punto**: A, E, O, S, I, U, N, L, R, T
- **Letras de 2 puntos**: D, G
- **Letras de 3 puntos**: B, C, M, P
- **Letras de 4 puntos**: F, H, V, Y
- **Letras de 5 puntos**: K
- **Letras de 6 puntos**: Ñ
- **Letras de 7 puntos**: LL, CH
- **Letras de 8 puntos**: J, X
- **Letras de 10 puntos**: Q, Z

### Alemán (German)
- **Detección**: `de`
- **Letras de 1 punto**: E, N, S, I, R, A, T, D, H, U
- **Letras de 2 puntos**: L, C, G
- **Letras de 3 puntos**: M, O, B
- **Letras de 4 puntos**: W, F, K, Z
- **Letras de 6 puntos**: V, P
- **Letras de 8 puntos**: J, Y
- **Letras de 10 puntos**: Q, X

## 📁 Estructura del Proyecto

```
Word_Score_Game/
├── app.py              # Archivo principal del juego
├── requirements.txt    # Dependencias del proyecto
├── .gitignore         # Archivos a ignorar en Git
└── README.md          # Este archivo
```

### Descripción de Archivos

- **`app.py`**: Contiene toda la lógica del juego, incluyendo:
  - Funciones de mapeo de puntuación
  - Detección de idioma
  - Cálculo de puntajes
  - Interfaz de usuario de línea de comandos

- **`requirements.txt`**: Lista las dependencias necesarias para ejecutar el proyecto

- **`.gitignore`**: Especifica qué archivos deben ser ignorados por Git

## 🔧 Desarrollo y Personalización

### Agregar un Nuevo Idioma

Para agregar soporte para un nuevo idioma:

1. Define el mapeo de puntuación en `app.py`:
```python
grouped_points_fr = {
    1: ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"),
    # ... más configuraciones
}
```

2. Convierte el mapeo:
```python
letter_points_fr = to_one_to_one_mapping(grouped_points_fr)
```

3. Agrega al diccionario de idiomas:
```python
LANG_MAP = {
    'en': letter_points_en,
    'es': letter_points_es,
    'de': letter_points_de,
    'fr': letter_points_fr,  # Nuevo idioma
}
```

4. Agrega el nombre del idioma:
```python
LANG_NAMES = {
    'en': 'Inglés',
    'es': 'Español',
    'de': 'Alemán',
    'fr': 'Francés',  # Nuevo idioma
}
```

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'langdetect'"
**Solución**: Ejecuta `pip install -r requirements.txt`

### Error: "python3: command not found"
**Solución**: 
- En Windows: Usa `python` en lugar de `python3`
- En macOS/Linux: Instala Python 3 desde [python.org](https://python.org)

### El idioma no se detecta correctamente
**Comportamiento**: Si el idioma no se puede detectar o no está soportado, el juego usa inglés por defecto.

## 📝 Licencia

Este proyecto está disponible como código abierto. Siéntete libre de usar, modificar y distribuir según tus necesidades.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📞 Soporte

Si encuentras algún problema o tienes preguntas, por favor abre un issue en el repositorio de GitHub.

---

¡Disfruta jugando con el Word Score Game! 🎉