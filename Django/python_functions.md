# Przykłady definicji funkcji w Pythonie

## Prosta funkcja

```python
def przywitaj():
	print("Cześć!")

przywitaj()
```

## Parametry i wartość zwracana

```python
def dodaj(a, b):
	return a + b

wynik = dodaj(3, 5)
print(wynik)  # 8
```

## Parametr z wartością domyślną

```python
def przywitaj(imie="Gościu"):
	return f"Cześć, {imie}!"

print(przywitaj())        # Cześć, Gościu!
print(przywitaj("Ania")) # Cześć, Ania!
```

## Argumenty nazwane

```python
def przedstaw(osoba, miasto):
	print(f"{osoba} mieszka w mieście {miasto}.")

przedstaw(miasto="Kraków", osoba="Jan")
```

## Dowolna liczba argumentów

```python
def suma(*liczby):
	return sum(liczby)

print(suma(1, 2, 3, 4))  # 10
```

## Funkcja z dokumentacją i adnotacjami typów

```python
def pole_prostokata(szerokosc: float, wysokosc: float) -> float:
	"""Zwraca pole prostokąta."""
	return szerokosc * wysokosc
```
