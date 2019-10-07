import pandas as pd

def load_dataset():
    home = pd.read_csv('mu_home.csv')
    away = pd.read_csv('mu_away.csv')

    return home, away

home, away = load_dataset()

manchester_home_scores = home[['Home Score']].values.tolist()
manchester_away_scores = away[['Away Score']].values.tolist()
liverpool_home_scores = away[['Home Score']].values.tolist()
liverpool_away_scores = home[['Away Score']].values.tolist()

mu_win_home = 0
mu_win_away = 0
liverpool_win_home = 0
liverpool_win_away = 0
draw_mu_home = 0
draw_mu_away = 0

for i in range(len(manchester_away_scores)):
    if manchester_home_scores[i][0] > liverpool_away_scores[i][0]:
        mu_win_home += 1
    elif manchester_home_scores[i][0] < liverpool_away_scores[i][0]:
        liverpool_win_away +=1
    else:
        draw_mu_home += 1
    
    if manchester_away_scores[i][0] < liverpool_home_scores[i][0]:
        liverpool_win_home += 1
    elif manchester_away_scores[i][0] > liverpool_home_scores[i][0]:
        mu_win_away += 1
    else:
        draw_mu_away += 1

print('MU Win HOME :', mu_win_home)
print('MU Win AWAY :', mu_win_away)
print('LIV Win HOME :', liverpool_win_home)
print('LIV Win AWAY :', liverpool_win_away)
print('DRAW MU HOME:', draw_mu_home)
print('DRAW MU AWAY:', draw_mu_away)

chance_mu_win_home = (mu_win_home / (mu_win_home + liverpool_win_away + draw_mu_home)) * 100
chance_mu_win_away = (mu_win_away / (mu_win_away + liverpool_win_home + draw_mu_away)) * 100
chance_liverpool_win_home = (liverpool_win_home / (liverpool_win_home + mu_win_away + draw_mu_away)) * 100
chance_liverpool_win_away = (liverpool_win_away / (liverpool_win_away + mu_win_home + draw_mu_home)) * 100
chance_draw_mu_home = (draw_mu_home / (mu_win_home + liverpool_win_away + draw_mu_home)) * 100
chance_draw_mu_away = (draw_mu_away / (mu_win_away + liverpool_win_home + draw_mu_away)) * 100

print('MU Win HOME :', chance_mu_win_home, '%')
print('LIV Win AWAY :', chance_liverpool_win_away, '%')
print('DRAW MU HOME:', chance_draw_mu_home, '%')
print('MU Win AWAY :', chance_mu_win_away, '%')
print('LIV Win HOME :', chance_liverpool_win_home, '%')
print('DRAW MU AWAY:', chance_draw_mu_away, '%')

likely_win_home = False
likely_win_away = False

if chance_mu_win_home > chance_mu_win_away:
    likely_win_home = True
else:
    likely_win_away = True


#result = 'Manchester United has a'

#if likely_win_home:
#    result += ' higher chance of winning at Old Trafford, about ' + str(chance_mu_win_home) + '%' + ', compared to ' + str(chance_liverpool_win_away) + '%% ' + str(chance_draw_mu_home) + '%% chance the match will result in draw.' + ' chance based on previous matches with Liverpool. Therefore, Manchester United has a higher chance to win.'
#elif likely_win_away:
#    result += ' lower chance of winning Old Trafford, about ' + str(chance_mu_win_home) + '%' + ', compared to ' + str(chance_liverpool_win_away) + '%' +' chance based on previous matches with Liverpool Therefore, Liverpool has a higher chance to win.' 

#print("Because October 20th 2019 match will take place at Old Trafford, " + result)

print("October 20th 2019 match will take place at Old Trafford. Here our prediction about outcome of the match:")
print(str(chance_mu_win_home) + "%" + " Manchester United will win.")
print(str(chance_liverpool_win_away) + "%" + " Liverpool will win.")
print(str(chance_draw_mu_home) + "%" + " the match will end with draw.")