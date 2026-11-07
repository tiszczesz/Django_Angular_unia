# definicja funkcji
import functions
from functions import Welcome, Other


def main():
    print("Hello python",end=" | ")
    print("inny tekst")
    print(__file__)
    print(__name__)
    functions.Welcome()
    print(round(functions.Other(5,2.56),2))
    print(Other(4,90))

# wywołanie funkcji
if __name__ == "__main__":
    main()