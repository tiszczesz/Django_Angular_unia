from pathlib import Path


def main():
    # filename = Path(__file__).resolve().parent / "input.txt"
    filename =Path("files/input.txt")
    with open(filename,"r",encoding="utf-8") as file:
        words = []
        for line in file:
            print(line.strip())
            words.extend([*line.split()])
    print(words)

    # print(Path)
    # print(filename)
    # file = open(filename,"r",encoding="utf-8")
    # content = file.read()
    # words = content.strip().split(" ")
    # print(words)
    # lines = file.readlines()
    # print(content)
    # print(lines)
    file.close()
    # if path.exists():
    #     print("jest")
    # else:
    #     print("Brak ścieżki")

# wywołanie funkcji
if __name__ == "__main__":
    main()