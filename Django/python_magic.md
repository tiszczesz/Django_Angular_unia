# Magiczne nazwy w Pythonie (`__nazwa__`)

Nazwy otoczone podwójnymi podkreśleniami, np. `__name__` lub `__init__`, nazywa się potocznie *dunderami* (od ang. *double underscore*). Nie są to komendy. To specjalne atrybuty i metody, których znaczenie określa Python lub używana biblioteka. Dzięki nim można m.in. definiować zachowanie obiektów i sprawdzać informacje o module.

## Najczęściej spotykane nazwy

| Nazwa | Do czego służy |
| --- | --- |
| `__name__` | Nazwa modułu. Dla pliku uruchomionego bezpośrednio ma wartość `"__main__"`. |
| `__init__` | Inicjalizuje nowo utworzony obiekt klasy. |
| `__str__` | Określa czytelną dla użytkownika reprezentację obiektu, używaną np. przez `str()` i `print()`. |
| `__repr__` | Określa reprezentację przydatną przy debugowaniu, używaną przez `repr()`. |
| `__len__` | Definiuje wynik `len(obiekt)`. |
| `__iter__` | Udostępnia iterator, aby obiekt można było przeglądać w pętli `for`. |
| `__call__` | Pozwala wywołać obiekt jak funkcję, np. `obiekt()`. |
| `__enter__` i `__exit__` | Definiują zachowanie obiektu używanego z `with`, np. podczas otwierania i zamykania zasobu. |
| `__doc__` | Zawiera dokumentację obiektu, jeśli została podana w docstringu. |
| `__file__` | Zwykle zawiera ścieżkę do pliku modułu; nie występuje w każdym środowisku. |

## Wzorzec `if __name__ == "__main__"`

Ten warunek sprawdza, czy plik został uruchomiony bezpośrednio, czy zaimportowany jako moduł. Kod wewnątrz bloku wykona się tylko przy bezpośrednim uruchomieniu:

```python
def main():
	print("Program uruchomiony bezpośrednio")


if __name__ == "__main__":
	main()
```

Po zaimportowaniu pliku jego `__name__` jest zwykle nazwą modułu, więc blok nie uruchamia się automatycznie. Pozwala to używać funkcji z pliku bez wykonywania jego części startowej.

## Własne metody specjalne

Można implementować metody specjalne w klasach, aby ich obiekty współpracowały ze standardowymi operacjami Pythona:

```python
class Produkt:
	def __init__(self, nazwa):
		self.nazwa = nazwa

	def __str__(self):
		return self.nazwa


produkt = Produkt("Kawa")
print(produkt)  # Kawa
```

Nazwy takie jak `__init__` mają ustalone znaczenie — nie należy wymyślać ich do zwykłych metod ani zmieniać ich pisowni. Nie należy też mylić ich z nazwami zaczynającymi się od pojedynczego podkreślenia (`_nazwa`), które są jedynie konwencją oznaczającą element przeznaczony do użytku wewnętrznego.
