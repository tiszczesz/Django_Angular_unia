# Moduły w Pythonie

Moduł to plik `.py` zawierający kod, który można wykorzystać w innych plikach. Moduły ułatwiają porządkowanie i ponowne używanie kodu.

## Tworzenie modułu

Utwórz plik `matematyka.py`:

```python
PI = 3.14159

def dodaj(a, b):
	return a + b

def pole_kola(promien):
	return PI * promien ** 2
```

W pliku `main.py` w tym samym katalogu zaimportuj i użyj modułu:

```python
import matematyka

print(matematyka.dodaj(2, 3))
print(matematyka.pole_kola(2))
```

## Importowanie

```python
import matematyka                 # użycie: matematyka.dodaj(2, 3)
import matematyka as mat          # alias: mat.dodaj(2, 3)
from matematyka import dodaj      # użycie: dodaj(2, 3)
from matematyka import PI, dodaj  # import wybranych nazw
```

Unikaj `from matematyka import *`, ponieważ może utrudniać ustalenie, skąd pochodzą nazwy i powodować ich konflikty.

## Moduł uruchamiany bezpośrednio

Kod chroniony warunkiem `if __name__ == "__main__":` wykona się tylko przy bezpośrednim uruchomieniu pliku, a nie podczas importu:

```python
def main():
	print(dodaj(4, 6))

if __name__ == "__main__":
	main()
```

## Moduły standardowe i zewnętrzne

Python ma wbudowane moduły, np. `math`, `random` i `datetime`:

```python
import math
import random
from datetime import date

print(math.sqrt(25))
print(random.randint(1, 6))
print(date.today())
```

Pakiet zewnętrzny można zainstalować poleceniem `python -m pip install requests`, a następnie zaimportować przez `import requests`.

## Pakiety

Pakiet to katalog grupujący moduły. Przykładowa struktura:

```text
projekt/
├── main.py
└── narzedzia/
	├── __init__.py
	└── tekst.py
```

W pliku `narzedzia/tekst.py`:

```python
def wielkie_litery(tekst):
	return tekst.upper()
```

W `main.py`:

```python
from narzedzia.tekst import wielkie_litery

print(wielkie_litery("witaj"))
```

Plik `__init__.py` może być pusty. Uruchamiaj program z katalogu projektu, aby Python mógł odnaleźć pakiet.

## Dobre praktyki

- Używaj opisowych nazw zapisanych małymi literami, np. `obsluga_pliku.py`.
- Nie nazywaj własnych plików tak jak moduły standardowe (np. `random.py`).
- Grupuj w module powiązane funkcje i klasy.
- Unikaj kosztownych działań wykonywanych automatycznie podczas importu.
