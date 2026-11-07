# Operacje na listach, zbiorach i słownikach w Pythonie

## Listy (`list`)

Lista to uporządkowana, modyfikowalna kolekcja, która może zawierać powtarzające się elementy.

```python
owoce = ["jabłko", "gruszka", "śliwka"]
owoce.append("banan")             # dodaje element na końcu
owoce.insert(1, "malina")         # wstawia element pod wskazanym indeksem
owoce.extend(["kiwi", "mango"])  # dodaje wiele elementów
owoce.remove("gruszka")           # usuwa pierwsze pasujące wystąpienie
ostatni = owoce.pop()              # usuwa i zwraca ostatni element
owoce[0] = "ananas"               # zmienia element
fragment = owoce[1:3]              # pobiera wycinek
```

Przydatne operacje obejmują sprawdzanie długości, wyszukiwanie i sortowanie:

```python
liczby = [3, 1, 2, 1]
len(liczby)        # 4 — liczba elementów
liczby.count(1)    # 2 — liczba wystąpień wartości 1
liczby.index(2)    # 2 — indeks pierwszego wystąpienia wartości 2
liczby.sort()      # sortuje listę w miejscu
nowa = sorted(liczby)  # zwraca nową, posortowaną listę
```

Wyrażenie listowe pozwala zwięźle utworzyć listę na podstawie innych danych:

```python
kwadraty = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

## Zbiory (`set`)

Zbiór przechowuje unikalne, hashowalne elementy. Nie służy do dostępu przez indeks. Pusty zbiór tworzy się przez `set()` — zapis `{}` tworzy pusty słownik.

```python
kolory = {"czerwony", "zielony", "niebieski"}
kolory.add("żółty")
kolory.update(["biały", "czarny"])
kolory.discard("zielony")  # nie zgłasza błędu, jeśli elementu brak
kolory.remove("biały")     # zgłasza KeyError, jeśli elementu brak
```

Zbiory obsługują podstawowe operacje teoriomnogościowe:

```python
a = {1, 2, 3}
b = {3, 4, 5}
a | b  # suma: {1, 2, 3, 4, 5}
a & b  # część wspólna: {3}
a - b  # różnica: {1, 2}
a ^ b  # różnica symetryczna: {1, 2, 4, 5}
2 in a # sprawdzanie przynależności: True
```

Zbiór pomaga usuwać duplikaty, np. `unikalne = set([1, 1, 2])`.

## Słowniki (`dict`)

Słownik przechowuje pary klucz–wartość. Klucze są unikalne i muszą być hashowalne, a wartości mogą być dowolnego typu. Słownik zachowuje kolejność wstawiania elementów.

```python
osoba = {"imie": "Ada", "wiek": 30}
osoba["miasto"] = "Kraków"            # dodaje lub zmienia wartość
imie = osoba["imie"]                  # odczyt; brak klucza powoduje KeyError
wiek = osoba.get("wiek")              # bezpieczny odczyt
telefon = osoba.get("telefon", "brak")  # odczyt z wartością domyślną
osoba.update({"wiek": 31})            # aktualizuje wpisy
miasto = osoba.pop("miasto")          # usuwa klucz i zwraca jego wartość
```

Po słowniku można iterować po kluczach, wartościach lub parach:

```python
for klucz in osoba:
	print(klucz, osoba[klucz])

for klucz, wartosc in osoba.items():
	print(klucz, wartosc)
```

Metody `keys()`, `values()` i `items()` udostępniają odpowiednio klucze, wartości i pary. `len(osoba)` zwraca liczbę par. Wyrażenie słownikowe tworzy słownik na podstawie danych:

```python
kwadraty = {x: x ** 2 for x in range(5)}
```

### Operacje statystyczne na elementach listy

Dla listy liczb można użyć wbudowanych funkcji `sum()`, `min()` i `max()`. Średnią arytmetyczną i medianę udostępnia moduł `statistics`:

```python
import statistics

liczby = [3, 1, 2, 1]
suma = sum(liczby)                         # 7
minimum = min(liczby)                     # 1
maksimum = max(liczby)                    # 3
srednia = statistics.mean(liczby)          # 1.75
mediana = statistics.median(liczby)        # 1.5
```

Funkcje te wymagają danych liczbowych; dla pustej listy `min()` i `max()` zgłaszają `ValueError`, a `statistics.mean()` i `statistics.median()` — `StatisticsError`.



## Wybór kolekcji

- **Lista** — gdy liczy się kolejność, indeksowanie lub powtarzające się elementy.
- **Zbiór** — gdy potrzebne są unikalne elementy i sprawdzanie przynależności.
- **Słownik** — gdy wartości mają być wyszukiwane za pomocą kluczy.
