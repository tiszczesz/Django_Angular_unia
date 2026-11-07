def Welcome():
    print("Podaj imię",end=": ")
    firstname = input()
    #print("Podaj nazwisko: ")
    lastname = input("Podaj nazwisko: ")
    #aż będą poprawne liczby
    while True:
        try:
            age = int(input("Podaj wiek: "))
            if age>0 and age<130:
                break
            else:
                print("niepoprawny wiek!!")
        except ValueError:
            print("Wiek musi być liczbą całkowitą. Spróbuj ponownie.")
    # dwa lata później
    age = age + 2
    print(f"Witaj {firstname} {lastname}! twój wiek: {age}")

def Other(a,b):
    return a+b