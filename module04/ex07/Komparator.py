import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("How hard is it to supply a Dataframe when asked?")
        self.df = df

    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        if not isinstance(categorical_var, str):
            return
        if isinstance(numerical_var, str):
            sns.boxenplot(data=self.df, x=numerical_var, y=categorical_var)
            plt.show()
        elif isinstance(numerical_var, (list, tuple)):
            _ = [self.compare_box_plots(categorical_var, numerical) for numerical in numerical_var]

    def density(self, categorical_var: str, numerical_var: str):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return
        new_data = self.df.groupby(categorical_var)[numerical_var]
        new_data.plot.kde(legend=True)
        plt.show()

    def compare_histograms(self, categorical_var: str, numerical_var: str):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return
        data = self.df.groupby(categorical_var)[numerical_var]
        data.plot.hist(legend=True, alpha=0.3)
        plt.show()
