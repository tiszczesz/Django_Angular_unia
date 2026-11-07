import functions
def main():
  size = int(input("Podaj ile chcesz liczb losowych: "))
  numbers = functions.generRandoms(size)
  print(numbers)
  print(sorted(numbers))
  print(f"statystyki: {functions.getStatistics(numbers)}")
  print(f"statystyki: {functions.getStatInDict(numbers)}")

if __name__ == "__main__":
    main()