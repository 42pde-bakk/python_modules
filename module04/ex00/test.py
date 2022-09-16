from FileLoader import FileLoader


def main() -> None:
    loader = FileLoader()
    data = loader.load("../data/athlete_sevents.csv")
    loader.display(data, 12)


if __name__ == '__main__':
    main()
