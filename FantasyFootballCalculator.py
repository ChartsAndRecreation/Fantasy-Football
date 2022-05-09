from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame

def parse_row(row):
    """
    Take in a tr tag and get the data out of it in the form of a list of strings.
    """
    return [str(x.string) for x in row.find_all('td')]

def getADP(year, scoring='half-ppr', teams='10'):
    url = 'https://fantasyfootballcalculator.com/adp/' + scoring
    url += '/' + teams
    url += '-team/all/' + year
    results = requests.get(url=url)
    results = Soup(results.text)
    results = results.find_all('table')
    results = results[0]
    results = results.find_all('tr')
    results = [parse_row(result) for result in results[1:]]
    results = DataFrame(results)
    results.columns = ['ovr','pick','name','pos','team','bye','adp','std_dev',
        'high','low','drafted','graph']
    results[['adp','std_dev']] = results[['adp','std_dev']].astype(float)
    results[['ovr','drafted']] = results[['ovr','drafted']].astype(int)
    results.drop(labels='graph',axis='columns',inplace=True)
    return results