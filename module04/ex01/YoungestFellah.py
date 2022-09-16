import pandas as pd


def youngest_fellah(df: pd.DataFrame, year: int) -> dict[str, float] | None:
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int) or year % 4 != 0:
        print('ERROR')
        return
    men = df.loc[(df['Sex'] == 'M') & (df['Year'] == year)]
    women = df.loc[(df['Sex'] == 'F') & (df['Year'] == year)]
    return {
        'm': men['Age'].min(),
        'f': women['Age'].min()
    }
