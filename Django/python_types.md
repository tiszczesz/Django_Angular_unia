# Typy danych w Pythonie

Python przypisuje typ do **wartości**, a nie na stałe do nazwy zmiennej. Ta sama zmienna może więc kolejno przechowywać wartości różnych typów:

```python
wartosc = 10          # int
wartosc = "dziesięć"  # str
```

Typ wartości można sprawdzić funkcją `type()`, a przynależność do typu (również jego podklasy) — funkcją `isinstance()`:

```python
liczba = 10
print(type(liczba))              # <class 'int'>
print(isinstance(liczba, int))   # True
```

## Podstawowe typy wbudowane

### Liczby

- `int` — liczby całkowite o dowolnej precyzji, np. `-3`, `0`, `42`.
- `float` — liczby zmiennoprzecinkowe, np. `3.14`, `-0.5`, `2.0`. Mogą wystąpić typowe ograniczenia precyzji zapisu binarnego.
- `complex` — liczby zespolone, np. `2 + 3j`.

```python
wiek = 25
cena = 19.99
liczba_zespolona = 2 + 3j

print(7 // 2)   # 3 — dzielenie całkowite
print(7 / 2)    # 3.5 — zwykłe dzielenie
print(7 % 2)    # 1 — reszta z dzielenia
print(2 ** 3)   # 8 — potęgowanie
```

### Wartości logiczne

`bool` ma dwie wartości: `True` i `False`. W Pythonie `bool` jest podtypem `int` (`True` zachowuje się liczbowo jak `1`, a `False` jak `0`), ale w kodzie warto traktować je jako wartości logiczne.

```python
czy_pelnoletni = wiek >= 18
print(czy_pelnoletni)  # True
```

### Tekst

`str` przechowuje tekst Unicode. Napisy można zapisywać w apostrofach, cudzysłowach lub potrójnych cudzysłowach. Są niemutowalne — nie zmienia się pojedynczych znaków w miejscu.

```python
imie = "Ala"
wiadomosc = f"Cześć, {imie}!"
print(wiadomosc)  # Cześć, Ala!
```

### Kolekcje

- `list` — uporządkowana, mutowalna kolekcja; może zawierać powtarzające się elementy.
- `tuple` — uporządkowana, niemutowalna kolekcja.
- `range` — niemutowalna sekwencja liczb całkowitych, często używana w pętli.
- `dict` — mutowalny słownik par klucz–wartość; klucze muszą być hashowalne.
- `set` — mutowalny zbiór unikalnych, hashowalnych elementów; nie gwarantuje kolejności.
- `frozenset` — niemutowalny zbiór.

```python
owoce = ["jabłko", "gruszka", "jabłko"]
punkt = (3, 5)
indeksy = range(3)
produkt = {"nazwa": "notes", "cena": 12.50}
unikalne_liczby = {1, 2, 2, 3}

owoce.append("śliwka")
print(unikalne_liczby)  # {1, 2, 3}
print(produkt["nazwa"]) # notes
```

Pusty słownik tworzy się przez `{}`, a pusty zbiór przez `set()` — zapis `{}` nie tworzy zbioru.

### Brak wartości i dane binarne

`None` oznacza brak wartości. `bytes` przechowuje niemutowalne dane binarne, a `bytearray` — ich mutowalną wersję.

```python
wynik = None
bajty = "żółć".encode("utf-8")
tekst = bajty.decode("utf-8")
```

## Mutowalność — ważna różnica

Listy, słowniki, zbiory i `bytearray` można modyfikować. Liczby, napisy, krotki i `bytes` są niemutowalne — operacje tworzą nową wartość.

```python
lista = [1, 2]
lista.append(3)       # zmienia tę samą listę

tekst = "Ala"
tekst = tekst + " ma kota"  # powstaje nowy napis przypisany do zmiennej
```

## Konwersja typów

### Konwersja jawna

Funkcje `int()`, `float()`, `str()`, `bool()` i konstruktory kolekcji pozwalają jawnie utworzyć wartość innego typu:

```python
int("42")                 # 42
float("3.5")              # 3.5
str(42)                    # "42"
bool(1)                    # True
list((1, 2))               # [1, 2]
tuple([1, 2])              # (1, 2)
set([1, 1, 2])             # {1, 2}
dict([( "a", 1), ("b", 2)]) # {'a': 1, 'b': 2}
```

Wartości tekstowe muszą mieć format odpowiedni dla konwertowanego typu:

```python
int("42")       # działa
int("42.5")     # ValueError
float("42.5")   # działa
```

`int()` odrzuca część ułamkową liczby zmiennoprzecinkowej, nie zaokrągla:

```python
int(3.9)   # 3
int(-3.9)  # -3
round(3.9) # 4 — zaokrąglenie
```

Niepoprawna konwersja może zgłosić wyjątek, np. `ValueError` dla `int("abc")` albo `TypeError` dla nieobsługiwanego typu argumentu. Jeśli dane pochodzą od użytkownika, obsłuż błąd w odpowiednim miejscu:

```python
tekst_liczby = input("Podaj liczbę całkowitą: ")

try:
    liczba = int(tekst_liczby)
except ValueError:
    print("To nie jest poprawna liczba całkowita.")
else:
    print(f"Podano: {liczba}")
```

`input()` zawsze zwraca `str`, dlatego liczby z wejścia trzeba skonwertować przed obliczeniami.

### Konwersja na wartość logiczną

`bool()` zwraca `False` dla wartości uznawanych za puste lub zerowe, m.in. `0`, `0.0`, `""`, `[]`, `{}`, `set()` i `None`. Pozostałe wartości są zwykle uznawane za `True`, także tekst `"False"`:

```python
bool(0)        # False
bool("")       # False
bool("False")  # True — niepusty tekst
bool([0])      # True — lista nie jest pusta
```

Dlatego nie używaj `bool()` do odczytywania tekstowych odpowiedzi „tak/nie” bez wcześniejszego sprawdzenia ich treści.

### Konwersja liczb podczas działań

W działaniach arytmetycznych Python może automatycznie promować liczby do szerszego typu, np. `int` do `float`:

```python
wynik = 5 + 2.5
print(wynik)        # 7.5
print(type(wynik))  # <class 'float'>
```

Nie oznacza to, że każdy typ da się automatycznie połączyć z każdym innym. Na przykład dodanie liczby i tekstu powoduje `TypeError`:

```python
"Wiek: " + str(25)  # "Wiek: 25"
# "Wiek: " + 25     # TypeError
```

## Dobre praktyki

- Konwertuj dane na wejściu, gdy znasz oczekiwany typ, i obsługuj możliwe błędy konwersji.
- Używaj `isinstance(x, Typ)` do sprawdzania typu w sytuacjach, w których jest to potrzebne; zwykle czytelniej jest po prostu użyć wartości.
- Nie myl tekstu reprezentującego liczbę (`"12"`) z liczbą (`12`).
- Pamiętaj, że `str(x)` tworzy tekst do wyświetlenia, a niekoniecznie zapis, który można bezpiecznie odtworzyć jako ten sam typ.
- Przy konwersji `str` i `bytes` podawaj kodowanie, najczęściej `"utf-8"`.
