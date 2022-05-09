import MyFantasyLeague as mfl
import FantasyFootballCalculator as ffc
import pandas as pd

aav = mfl.getAAV('2022')
adp = mfl.getADP('2022')
byes = mfl.getByeWeeks('2022')
injuries = mfl.getInjuries('2022')
players = mfl.getPlayers('2022')
ranks = mfl.getRanks('2022')