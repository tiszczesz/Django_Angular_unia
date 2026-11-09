from pathlib import Path
from collections import Counter


def main():
    # filename = Path(__file__).resolve().parent / "input.txt"
    words = getFromFile()
    statistics = getSatistcis(words)
    print(f"Liczba wyrazów: {len(words)}")
    print(f"Liczba unikalnych wyrazów: {len(statistics)}")
    for word, count in sorted(
        statistics.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"{word}: {count}")

    # print(Path)
    # print(filename)
    # file = open(filename,"r",encoding="utf-8")
    # content = file.read()
    # words = content.strip().split(" ")
    # print(words)
    # lines = file.readlines()
    # print(content)
    # print(lines)
    

def getFromFile():
    filename = Path("files/input.txt")
    words = []

    with filename.open("r", encoding="utf-8") as file:
        for line in file:
            # print(line.strip())
            words.extend(line.split())

    return words
    # if path.exists():
    #     print("jest")
    # else:
    #     print("Brak ścieżki")

def getSatistcis(words):
    statistics = {}
    for word in words:
        statistics[word] = statistics.get(word, 0) + 1
    return statistics

# wywołanie funkcji
if __name__ == "__main__":
    main()