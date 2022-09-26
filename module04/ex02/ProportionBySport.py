import pandas as pd


def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str):
    if not (isinstance(df, pd.DataFrame) and isinstance(year, int) and isinstance(sport, str) and isinstance(gender, str)):
        return None
    total = df.loc[(df['Sex'] == gender) & (df['Year'] == year)]
    sub = total.loc[df['Sport'] == sport]
    # total = total.drop_duplicates(subset=['Name'])
    # sub = sub.drop_duplicates(subset=['Name'])
    if len(sub) == 0:
        return 0.0
    return len(sub) / len(total)
