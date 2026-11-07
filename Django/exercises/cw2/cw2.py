import functions
def main():
  size = int(input("Podaj ile chcesz liczb losowych: "))
  numbers = functions.generRandoms(size)
  print(numbers)
  print(sorted(numbers))
  print(f"statystyki: {functions.getStatistics(numbers)}")
  print(f"statystyki: {functions.getStatInDict(numbers)}")
  print(f"bez powtórzeń: {functions.distinc(numbers)}")
  print(f"ilość wystąpień: {functions.counter(numbers)}")
  print("Ilość wystąpień:")
  counts = functions.counter(numbers)
#   for key, value in sorted(
#      counts.items(), 
#      key=lambda item: 
#      abs(item[0])):
#       print(f"liczba: {key}\tilość wystąpień: {value}")
  for key, value in sorted(counts.items()):    
      print(f"----liczba: {key}\tilość wystąpień: {value}")
  for key, value in sorted(counts.items(),key=lambda elem: elem[1]):    
      print(f"liczba: {key}\tilość wystąpień: {value}")
if __name__ == "__main__":
    main()