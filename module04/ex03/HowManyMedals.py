import pandas as pd


def how_many_medals(df: pd.DataFrame, name: str) -> dict:
    if not (isinstance(df, pd.DataFrame) and isinstance(name, str)):
        return {}
    selection = df.loc[(df['Name'] == name) & df['Medal']]
    medal_dict = {}
    for index, row in selection.iterrows():
        year = row['Year']
        if year not in medal_dict.keys():
            medal_dict[year] = {'G': 0, 'S': 0, 'B': 0}
        medal_dict[year][row['Medal'][0]] += 1
    return medal_dict
