from FileLoader import FileLoader
from MyPlotLib import MyPlotLib


def main() -> None:
    loader = FileLoader()
    mpl = MyPlotLib()
    data = loader.load('../data/athlete_events.csv')
    mpl.histogram(data, ['Height', 'Weight'])
    mpl.density(data, ['Weight', 'Height'])
    mpl.pair_plot(data, ['Weight', 'Height'])
    mpl.box_plot(data, ['Weight', 'Height'])


if __name__ == '__main__':
    main()
