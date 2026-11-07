from random import randint
import sys
def generRandoms(howMany):
    numbers = [] # pusta lista liczb
    #todo
    for _ in range(howMany):
        numbers.append(randint(0,100)) # dodajemy kolejno nowe losowe
    return numbers

def getStatistics(data):
    # zbiór pusty
    if len(data) == 0 :
        return ("BRAK DANYCH")
    # zwracacie krotkę (suma,min,max,srednia) bez uzywania wbudowanych 
    min = sys.maxsize
    max = -sys.maxsize-1
    sum = 0
    avg = 0
    for elem in data:
        if elem > max :
            max = elem
        if elem < min:
            min = elem
        sum = sum + elem
    return (sum,min,max,round(sum/len(data),2))

def getStatInDict(data):
    pass # statystyki w słowniku