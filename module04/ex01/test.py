from FileLoader import FileLoader
from YoungestFellah import youngest_fellah


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(youngest_fellah(data, 2004))


if __name__ == '__main__':
    main()
