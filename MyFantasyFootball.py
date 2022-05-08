import requests
import pandas as pd

def getAAV(year, ppr='1', keeper='N'):
    """
    Go to https://api.myfantasyleague.com/2022/api_info?STATE=details# for more details.
    year:   NFL season you're requesting data for. January 2022 will be part of the 2021 season.
    ppr:    Specify if you want leagues with points-per-reception (PPR) scoring or not.
        -1 = All scoring formats
        0 = Non-PPR scoring formats
        1 = PPR Scoring formats
    keeper: Specify the type of league drafts.
        N = Redraft leagues
        K = Keeper leagues
        R = Rookie-only draft league
    """
    'https://api.myfantasyleague.com/2022/export?TYPE=aav&PERIOD=&IS_PPR=1&IS_KEEPER=N&JSON=1'
    url = 'https://api.https://api.myfantasyleague.com/' + year
    url += '/export?TYPE=aav&IS_PPR=' + ppr
    url += '&IS_KEEPER=' + keeper
    url += '&JSON=1'
    results = requests.get(url=url)
    results = results.json()
    results = results['aav']['player']
    results = pd.DataFrame.from_dict(data=results)
    return results

def getADP(year, teams='10', ppr='1', keeper='N', mock='0',cutoff='5'):
    """
    Go to https://api.myfantasyleague.com/2022/api_info?STATE=details# for more details.
    year:   NFL season you're requesting data for. January 2022 will be part of the 2021 season.
    teams:  Number of teams in the league. Valid values are 8, 10, 12, 14, and 16. If 16 is specified, it will include leagues with 16 or more teams.
    ppr:    Specify if you want leagues with points-per-reception (PPR) scoring or not.
        -1 = All scoring formats
        0 = Non-PPR scoring formats
        1 = PPR Scoring formats
    keeper: Specify the type of league drafts.
        N = Redraft leagues
        K = Keeper leagues
        R = Rookie-only draft league
    mock:   Specify whether mock drafts should be included.
        -1 = All drafts
        0 = Exclude mock drafts
        1 = Only mock drafts
    cutoff: Only returns data for players selected in at least this percentage of drafts (10 = 10%).
    """
    url = 'https://api.myfantasyleague.com/' + year
    url += '/export?TYPE=adp&FCOUNT=' + teams
    url += '&IS_PPR=' + ppr
    url += '&IS_KEEPER=' + keeper
    url += '&IS_MOCK=' + mock
    url += '&CUTOFF=' + cutoff
    url += '&JSON=1'
    results = requests.get(url=url)
    results = results.json()
    results = results['adp']['player']
    results = pd.DataFrame.from_dict(data=results)
    return results

def getPlayers(year):
    """
    Go to https://api.myfantasyleague.com/2022/api_info?STATE=details# for more details.
    year:   NFL season you're requesting data for. January 2022 will be part of the 2021 season.
    """
    url = 'https://api.myfantasyleague.com/' + year
    url += '/export?TYPE=players&DETAILS=1&JSON=1'
    results = requests.get(url=url)
    results = results.json()
    results = results['players']['player']
    results = pd.DataFrame.from_dict(data=results)
    return results

def getRanks(year, pos=''):
    """
    Go to https://api.myfantasyleague.com/2022/api_info?STATE=details# for more details.
    year:   NFL season you're requesting data for. January 2022 will be part of the 2021 season.
    pos:    Specify position of player (optional).
    """
    url = 'https://api.myfantasyleague.com/' + year
    url += '/export?TYPE=playerRanks&POS=' + pos
    url += '&JSON=1'
    results = requests.get(url=url)
    results = results.json()
    results = results['player_ranks']['player']
    results = pd.DataFrame.from_dict(data=results)
    return results