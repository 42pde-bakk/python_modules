from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))

    print(sp.when('Amsterdam'))


if __name__ == '__main__':
    main()
