from Komparator import Komparator
from FileLoader import FileLoader


def main() -> None:
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    komp = Komparator(data)
    komp.compare_box_plots('Sex', 'Height')
    komp.compare_box_plots('Sex', 'Weight')

    komp.density('Sex', 'Height')
    komp.compare_histograms('Sex', 'Height')


if __name__ == '__main__':
    main()
