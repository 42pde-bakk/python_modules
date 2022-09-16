from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    res = proportion_by_sport(data, 2004, 'Tennis', 'F')
    print(res)


if __name__ == '__main__':
    main()
