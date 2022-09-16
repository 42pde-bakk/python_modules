import pandas as pd


class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def when(self, location: str) -> list[int]:
        if not (isinstance(self.df, pd.DataFrame) and isinstance(location, str)):
            return []
        return self.df[self.df['City'] == location]['Year'].unique().tolist()

    def where(self, year: int) -> list[str]:
        if not (isinstance(self.df, pd.DataFrame) and isinstance(year, int)):
            return []
        return self.df[self.df['Year'] == year]['City'].unique().tolist()
