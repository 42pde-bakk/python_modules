from FileLoader import FileLoader
from HowManyMedals import how_many_medals


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    res = how_many_medals(data, 'Kjetil Andr Aamodt')
    print(res)


if __name__ == '__main__':
    main()
