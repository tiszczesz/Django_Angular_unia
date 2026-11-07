# Typy proste i złożone w TypeScript — porównanie z JavaScript

## JavaScript a TypeScript

JavaScript jest językiem dynamicznie typowanym: typ wartości jest sprawdzany podczas działania programu. TypeScript dodaje statyczne sprawdzanie typów, dzięki któremu wiele błędów można wykryć przed uruchomieniem. TypeScript kompiluje się do JavaScriptu, a adnotacje typów nie są zwykle obecne w wynikowym kodzie.

```js
// JavaScript: zmienna może później przechowywać wartość innego typu
let wartosc = 42;
wartosc = "tekst";
```

```ts
let wartosc: number = 42;
// wartosc = "tekst"; // błąd TypeScriptu
```

## Typy proste

Podstawowe typy TypeScriptu obejmują `string`, `number`, `boolean`, `bigint`, `symbol`, `null` i `undefined`. Typ `void` opisuje najczęściej funkcję, która nie zwraca wartości.

```ts
let imie: string = "Ala";
let wiek: number = 28;
let aktywny: boolean = true;
let duzaLiczba: bigint = 9007199254740991n;
```

TypeScript potrafi wnioskować o typie na podstawie wartości początkowej:

```ts
let miasto = "Gdańsk"; // string
let licznik = 0;        // number
```

W JavaScript nie zapisuje się takich adnotacji. Można używać tych samych rodzajów wartości, ale zmienna może zmienić typ, a problem może ujawnić się dopiero w trakcie działania.

```js
let wiek = 28;
wiek = "dwadzieścia osiem"; // poprawna składnia JavaScriptu
```

Przy włączonym `strictNullChecks` (np. przez `"strict": true` w `tsconfig.json`) `null` i `undefined` trzeba uwzględnić jawnie:

```ts
let drugieImie: string | null = null;
drugieImie = "Maria";
```

## Tablice i krotki

Tablica może zawierać elementy jednego określonego typu. Zapis `T[]` jest równoważny `Array<T>`.

```ts
const oceny: number[] = [5, 4, 3];
const nazwy: Array<string> = ["Ada", "Jan"];
// oceny.push("dobry"); // błąd: element musi być liczbą
```

JavaScript nie ogranicza typu elementów tablicy:

```js
const oceny = [5, 4, 3];
oceny.push("dobry"); // dozwolone przez JavaScript
```

Krotka (tuple) określa typ i pozycję elementów:

```ts
const osoba: [string, number] = ["Ola", 31];
// const bledna: [string, number] = [31, "Ola"]; // błąd
```

JavaScript nie ma osobnego typu krotki — jest to zwykła tablica bez statycznej kontroli jej struktury.

## Obiekty, aliasy typów i interfejsy

Typ obiektu opisuje jego właściwości i ich typy. Znak `?` oznacza właściwość opcjonalną.

```ts
type Uzytkownik = {
	id: number;
	imie: string;
	email?: string;
};

const uzytkownik: Uzytkownik = { id: 1, imie: "Kamil" };
```

Kształt obiektu można też opisać przez `interface`:

```ts
interface Produkt {
	nazwa: string;
	cena: number;
	dostepny: boolean;
}

const produkt: Produkt = {
	nazwa: "Kubek",
	cena: 25,
	dostepny: true,
};
```

`type` pozwala tworzyć aliasy typów prostych, obiektów, unii i krotek. `interface` jest często używany do opisywania obiektów i może być rozszerzany przez inne interfejsy. JavaScript ma obiekty, ale nie ma składni deklarowania ich kształtu ani sprawdzania go przed uruchomieniem.

## Unie i zawężanie typów

Unia (`|`) oznacza, że wartość może być jednego z kilku typów. Sprawdzenie warunku pozwala zawęzić typ i bezpiecznie użyć właściwej operacji.

```ts
function opiszWartosc(wartosc: string | number): string {
	if (typeof wartosc === "number") {
		return wartosc.toFixed(2);
	}
	return wartosc.toUpperCase();
}
```

JavaScript obsługuje `typeof`, ale parametr funkcji nie ma statycznie określonego typu:

```js
function opiszWartosc(wartosc) {
	if (typeof wartosc === "number") return wartosc.toFixed(2);
	return wartosc.toUpperCase();
}
```

## Typy literalne i enum

Typ literalny ogranicza wartość do wskazanych stałych. Unie takich typów przydają się np. do opisywania statusów:

```ts
type Status = "oczekuje" | "oplacone" | "wyslane";

function zmienStatus(status: Status): void {
	console.log(status);
}

zmienStatus("oplacone");
// zmienStatus("anulowane"); // błąd
```

TypeScript oferuje również `enum`:

```ts
enum Kierunek {
	Gora,
	Dol,
}

const ruch: Kierunek = Kierunek.Gora;
```

JavaScript nie ma składni typów literalnych ani `enum` TypeScriptu. Można utworzyć obiekt stałych, ale JavaScript sam nie wymusi, by wartość należała do określonego zbioru.

## Funkcje

TypeScript pozwala opisać typy parametrów i wyniku funkcji:

```ts
function dodaj(a: number, b: number): number {
	return a + b;
}

const powitaj = (imie: string): string => `Cześć, ${imie}!`;
```

W JavaScript nie ma adnotacji, więc błędne argumenty nie zostaną odrzucone przez system typów przed uruchomieniem:

```js
function dodaj(a, b) {
	return a + b;
}
```

## Typy generyczne

Generyki umożliwiają tworzenie funkcji wielokrotnego użytku, zachowujących informację o typie danych:

```ts
function pierwsza<T>(elementy: T[]): T | undefined {
	return elementy[0];
}

const pierwszaLiczba = pierwsza([10, 20]); // number | undefined
const pierwszaNazwa = pierwsza(["Ada", "Jan"]); // string | undefined
```

JavaScript może zawierać funkcję o takim samym działaniu, ale nie zapisuje parametru typu `T` ani nie sprawdza statycznie typu wyniku.

## `any` i `unknown`

`any` wyłącza sprawdzanie typu dla danej wartości. `unknown` jest bezpieczniejszy, ponieważ wymaga sprawdzenia typu przed użyciem.

```ts
let dowolne: any = "tekst";
dowolne.nieistniejacaMetoda(); // kompilator nie zgłasza błędu

let nieznane: unknown = "tekst";
if (typeof nieznane === "string") {
	console.log(nieznane.toUpperCase());
}
```

## Podsumowanie

JavaScript dostarcza wartości, obiekty i operacje sprawdzane głównie podczas działania. TypeScript dodaje statyczny opis typów prostych i złożonych, takich jak tablice, krotki, obiekty, unie i generyki. Pomaga wcześniej wykrywać pomyłki, ale nie zastępuje walidacji danych w czasie działania, np. danych otrzymanych z API.
