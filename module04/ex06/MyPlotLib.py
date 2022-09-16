import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class MyPlotLib:

    @staticmethod
    def __parameters_valid(data: pd.DataFrame, features: list[str]) -> bool:
        if not isinstance(data, pd.DataFrame):
            return False
        if not isinstance(features, list) or not features or any(not isinstance(x, str) for x in features):
            return False
        return True

    @staticmethod
    def histogram(data: pd.DataFrame, features: list[str]) -> None:
        if not MyPlotLib.__parameters_valid(data, features):
            return
        data.hist(column=features)
        plt.show()

    @staticmethod
    def density(data: pd.DataFrame, features: list[str]) -> None:
        if not MyPlotLib.__parameters_valid(data, features):
            return
        data[features].plot.kde()
        plt.show()

    @staticmethod
    def pair_plot(data: pd.DataFrame, features: list[str]) -> None:
        if not MyPlotLib.__parameters_valid(data, features):
            return
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    @staticmethod
    def box_plot(data: pd.DataFrame, features: list[str]) -> None:
        if not MyPlotLib.__parameters_valid(data, features):
            return
        sns.boxplot(data=data[features])
        plt.show()
