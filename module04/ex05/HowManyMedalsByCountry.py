import pandas as pd


TEAM_SPORTS = (
    'Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo',
    'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball',
    'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo'
)


def how_many_medals_by_country(df: pd.DataFrame, country: str) -> dict[str, dict]:
    if not (isinstance(df, pd.DataFrame) and isinstance(country, str)):
        return {}
    medals = df.loc[(df['Team'] == country) & (df['Medal'].notna())]
    team_medals = medals.loc[medals['Sport'].isin(TEAM_SPORTS)]
    not_team_medals = medals.loc[~medals['Sport'].isin(TEAM_SPORTS)]
    men = team_medals.loc[team_medals['Sex'] == 'M'].drop_duplicates(['Year', 'Event'])
    women = team_medals.loc[team_medals['Sex'] == 'F'].drop_duplicates(['Year', 'Event'])
    medals = pd.concat([men, women, not_team_medals])
    d = {}
    for idx, row in medals.iterrows():
        year = row['Year']
        if year not in d.keys():
            d[year] = {medal: 0 for medal in ['G', 'S', 'B']}
        d[year][row['Medal'][0]] += 1
    return d
