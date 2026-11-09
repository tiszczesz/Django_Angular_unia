# Wyrażenia listowe w Pythonie: pliki i ich zawartość

Wyrażenie listowe (list comprehension) pozwala zwięźle utworzyć listę na podstawie elementów iterowalnych, opcjonalnie je przekształcając lub filtrując. Ma postać:

```python
[nowy_element for element in zrodlo if warunek]
```

Poniższe przykłady używają `pathlib`, które ułatwia pracę ze ścieżkami i plikami.

## Wyszukiwanie plików w katalogu

Utwórz listę ścieżek do plików tekstowych w katalogu `dane`:

```python
from pathlib import Path

katalog = Path("dane")
pliki_txt = [sciezka for sciezka in katalog.glob("*.txt") if sciezka.is_file()]

print(pliki_txt)
```

Można od razu utworzyć listę nazw plików:

```python
nazwy_plikow = [sciezka.name for sciezka in katalog.glob("*.txt") if sciezka.is_file()]
```

## Wczytywanie i filtrowanie wierszy

Metoda `read_text()` odczytuje cały plik jako tekst. `splitlines()` dzieli go na wiersze, a wyrażenie listowe może usunąć zbędne spacje i pominąć puste linie:

```python
sciezka = Path("dane/notatki.txt")
wiersze = [wiersz.strip() for wiersz in sciezka.read_text(encoding="utf-8").splitlines() if wiersz.strip()]

print(wiersze)
```

Dla pliku zawierającego:

```text
  Ala ma kota

  Python jest czytelny
```

wynikiem będzie:

```python
["Ala ma kota", "Python jest czytelny"]
```

## Przekształcanie elementów odczytanych z pliku

Jeśli plik zawiera jedną liczbę w każdym wierszu, można zamienić niepuste wiersze na liczby całkowite:

```python
tekst = Path("dane/liczby.txt").read_text(encoding="utf-8")
liczby = [int(wiersz.strip()) for wiersz in tekst.splitlines() if wiersz.strip()]

parzyste_kwadraty = [liczba**2 for liczba in liczby if liczba % 2 == 0]
print(parzyste_kwadraty)
```

Każdy niepusty wiersz musi zawierać poprawną liczbę całkowitą; w przeciwnym razie `int()` zgłosi `ValueError`.

## Zapis przetworzonej zawartości do pliku

List comprehension może przygotować nowe wiersze. Do samego zapisu użyj `write_text()` — nie wykonuj operacji zapisu jako efektu ubocznego wyrażenia listowego:

```python
zrodlo = Path("dane/wejscie.txt")
cel = Path("dane/wyjscie.txt")

wiersze = zrodlo.read_text(encoding="utf-8").splitlines()
przetworzone = [wiersz.strip().upper() for wiersz in wiersze if wiersz.strip()]
cel.write_text("\n".join(przetworzone) + "\n", encoding="utf-8")
```

## Wczytanie i przetworzenie wielu plików

Poniższy przykład tworzy listę niepustych wierszy ze wszystkich plików `.txt` w katalogu:

```python
katalog = Path("dane")
wiersze = [
    wiersz.strip()
    for plik in katalog.glob("*.txt")
    if plik.is_file()
    for wiersz in plik.read_text(encoding="utf-8").splitlines()
    if wiersz.strip()
]
```

Kolejność klauzul `for` ma znaczenie: najpierw wybierany jest plik, a potem jego wiersze. Przy bardziej złożonych operacjach warto użyć zwykłej pętli `for`, która ułatwia obsługę błędów odczytu i wskazanie pliku, którego dotyczy problem.

## Kiedy używać, a kiedy unikać

- Używaj list comprehension do zwięzłego filtrowania lub przekształcania elementów, np. nazw plików i wierszy.
- Nie używaj go wyłącznie do efektów ubocznych, takich jak zapis, usuwanie lub zmiana nazw plików. Takie działania czytelniej wykonać w zwykłej pętli.
- Dla dużych plików `read_text()` wczytuje całą zawartość do pamięci. Zamiast tego przetwarzaj plik wiersz po wierszu:

```python
with Path("dane/duzy_plik.txt").open(encoding="utf-8") as plik:
    wiersze = [wiersz.strip() for wiersz in plik if wiersz.strip()]
```

Powyższy wariant nadal przechowuje wynikową listę w pamięci. Jeśli lista nie jest potrzebna, przetwarzaj każdy wiersz bezpośrednio w pętli.