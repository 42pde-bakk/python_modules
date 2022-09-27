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
    team_medals = medals.loc[medals['Sport'].isin(TEAM_SPORTS)].drop_duplicates(['Year', 'Event', 'Sport', 'Medal', 'Team'])
    not_team_medals = medals.loc[~medals['Sport'].isin(TEAM_SPORTS)]
    medals = pd.concat([team_medals, not_team_medals])
    d = {}
    for idx, row in medals.iterrows():
        year = row['Year']
        if year not in d.keys():
            d[year] = {medal: 0 for medal in ['G', 'S', 'B']}
        d[year][row['Medal'][0]] += 1
    return d
