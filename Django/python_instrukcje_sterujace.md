# Instrukcje sterujące i pętle w Pythonie

Instrukcje sterujące decydują, które fragmenty programu zostaną wykonane i ile razy. Do podstawowych należą warunki `if`, pętle `for` i `while` oraz słowa kluczowe `break`, `continue` i `pass`.

## Warunki: `if`, `elif`, `else`

Warunek wykonuje blok kodu tylko wtedy, gdy jego wyrażenie ma wartość prawdziwą. Bloki w Pythonie wyznacza się wcięciami (zwykle czterema spacjami), a nie nawiasami klamrowymi.

```python
temperatura = 21

if temperatura > 25:
    print("Jest ciepło")
elif temperatura >= 15:
    print("Jest umiarkowanie")
else:
    print("Jest chłodno")
```

Można łączyć warunki operatorami `and`, `or`, `not` oraz porównaniami. Porównania można łańcuchować:

```python
wiek = 20
if 18 <= wiek < 65 and wiek != 30:
    print("Warunek został spełniony")
```

## Pętla `for`

`for` przechodzi kolejno po elementach iterowalnego obiektu, np. listy, napisu, słownika lub zakresu `range`.

```python
owoce = ["jabłko", "gruszka", "śliwka"]

for owoc in owoce:
    print(owoc)
```

Przejście po napisie zwraca kolejne znaki, a po słowniku — domyślnie kolejne klucze:

```python
for znak in "Python":
    print(znak)

ceny = {"chleb": 5.50, "mleko": 4.20}
for nazwa, cena in ceny.items():
    print(f"{nazwa}: {cena} zł")
```

### `range()` — zakres liczb dla pętli

`range()` tworzy sekwencję liczb całkowitych. Wartość końcowa nie należy do zakresu:

- `range(stop)` — od `0` do `stop - 1`;
- `range(start, stop)` — od `start` do `stop - 1`;
- `range(start, stop, step)` — z podanym krokiem.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

for i in range(10, 0, -2):
    print(i)  # 10, 8, 6, 4, 2
```

Krok nie może wynosić `0`. Przy kroku dodatnim zakres rośnie, a przy ujemnym maleje. `range()` nie tworzy od razu listy wszystkich liczb — można po nim iterować bez przechowywania całej sekwencji w pamięci.

Jeśli potrzebny jest indeks i wartość elementu, użyj `enumerate()` zamiast ręcznie indeksować listę:

```python
for indeks, owoc in enumerate(owoce, start=1):
    print(indeks, owoc)
```

## Pętla `while`

`while` wykonuje blok, dopóki warunek jest prawdziwy. Zadbaj, aby warunek w końcu stał się fałszywy — inaczej powstanie pętla nieskończona.

```python
pozostalo = 3
while pozostalo > 0:
    print(f"Pozostało: {pozostalo}")
    pozostalo -= 1
```

## `break`, `continue` i `pass`

- `break` natychmiast kończy najbliższą pętlę.
- `continue` pomija resztę bieżącej iteracji i przechodzi do następnej.
- `pass` niczego nie robi; służy jako pusta instrukcja, gdy składnia wymaga bloku, który uzupełnimy później.

```python
for liczba in range(1, 8):
    if liczba == 5:
        break
    if liczba % 2 == 0:
        continue
    print(liczba)  # 1, 3

if True:
    pass  # miejsce na kod dodany później
```

`pass` nie pomija iteracji ani nie kończy pętli — do tego służą odpowiednio `continue` i `break`.

## `else` przy pętlach

Pętla może mieć blok `else`. Wykona się on po normalnym zakończeniu pętli, ale nie po jej przerwaniu przez `break`.

```python
szukana = 7

for liczba in [2, 4, 6, 8]:
    if liczba == szukana:
        print("Znaleziono")
        break
else:
    print("Nie znaleziono")
```

Ten wzorzec przydaje się przy wyszukiwaniu: `else` oznacza, że pętla sprawdziła wszystkie elementy i nie znalazła pasującego.

## Zagnieżdżone pętle

Pętla może znajdować się wewnątrz drugiej pętli. Każde zagnieżdżenie zwiększa wcięcie:

```python
for wiersz in range(1, 4):
    for kolumna in range(1, 3):
        print(f"({wiersz}, {kolumna})")
```

`break` i `continue` wpływają na najbliższą pętlę, w której się znajdują.

## Typowe pomyłki

- `range(1, 5)` kończy się na `4`, bo koniec zakresu jest wyłączny.
- Pętla `while` może nie kończyć się, jeśli jej warunek nigdy nie stanie się fałszywy.
- Wcięcia w bloku muszą być spójne.
- `break`, `continue` i `pass` mają różne znaczenie: zakończenie pętli, pominięcie iteracji i pusta instrukcja.
