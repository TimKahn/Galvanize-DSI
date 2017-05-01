import pandas as pd
import numpy as np


def get_rates(df, lst_to_rate):
    for stat in lst_to_rate:
        df[stat] = df[stat] / df['g']
    return df

def teams_preprocess(teams_df, trash=[]):
    for t in trash:
        teams_df.pop(t)
    teams_df.columns = [col.lower() for col in teams_df.columns.tolist()]
    teams_df['1b'] = teams_df['h'] - teams_df['hr'] - teams_df['2b'] - teams_df['3b']
    teams_df['ba'] = teams_df['h'] / teams_df['ab']
    teams_df['obp'] = (teams_df['h'] + teams_df['bb']) / (teams_df['ab'] + teams_df['bb']) #on base percentage
    teams_df['sp'] = (teams_df['1b'] + (teams_df['2b'] * 2) + (teams_df['3b'] * 3) + (teams_df['hr'] * 4)) / teams_df['ab']  #slugging percentage
    teams_df['ops'] = teams_df['obp'] + teams_df['sp'] #on base percentage plus slugging percentage
    teams_df['Wins'] = teams_df['w']
    teams = get_rates(teams_df, teams_to_rate)
    teams = teams[teams['yearid'] > 1980]
    teams = teams[teams['yearid'] != 1994]
    return teams

# teams_df haven't always played the same number of games each year
# convert certain stats to rates to reflect
teams_to_rate = ['r', 'ab', 'h', '1b','2b', '3b', 'hr', 'so', 'bb',
                'sb', 'cs', 'hbp', 'sf', 'ra', 'cg', 'sho', 'sv', 'ipouts',
                'ha', 'bba', 'soa', 'e', 'dp', 'w', 'l']



if __name__ == '__main__':
    teams_df = pd.read_csv('Teams.csv')
    batting = pd.read_csv('Batting.csv')
    pitching = pd.read_csv('Pitching.csv')
    fielding = pd.read_csv('Fielding.csv')
    salaries = pd.read_csv('Salaries.csv')
    teams = teams_preprocess(teams_df)
