from eredivisie import *

# OPGAVE 1 a
wedstrijden = dict()
for wedstrijd in eredivisie:
    spel = wedstrijd.split(":")[0]
    team1_str = spel.split("-")[0][0:-1]
    team2_str = spel.split("-")[1][1:]
    wedstrijden[(team1_str, team2_str)] = eval(wedstrijd.split(":")[1])

print(wedstrijden)




# OPGAVE 1 b
teams = dict()
for wedstrijd in eredivisie:
    spel = wedstrijd.split(":")[0]

    team1_str = spel.split("-")[0][0:-1]
    if team1_str not in teams:
        teams[team1_str] = Team(team1_str)

    team2_str = spel.split("-")[1][1:]
    if team2_str not in teams:
        teams[team2_str] = Team(team2_str)
    
    wedstrijd_score = eval(wedstrijd.split(":")[1])
    if wedstrijd_score < 0:
        teams[team2_str].points += 3
    elif wedstrijd_score > 0:
        teams[team1_str].points += 3
    else:
        teams[team1_str].points += 1
        teams[team2_str].points += 1
    
    teams[team1_str].goal_difference += int(wedstrijd.split(":")[1][1])
    teams[team1_str].goal_difference -= int(wedstrijd.split(":")[1][-1])
    teams[team2_str].goal_difference += int(wedstrijd.split(":")[1][-1])
    teams[team2_str].goal_difference -= int(wedstrijd.split(":")[1][1])
    

print(teams)




# OPGAVE 1 c
winningteam = list(teams.values())[0]
for team in teams.values():
    if team.points > winningteam.points:
        winningteam = team
    elif team.points == winningteam.points  and  team.goal_difference > winningteam.goal_difference:
        winningteam = team

print(winningteam)
