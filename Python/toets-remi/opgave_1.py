import eredivisie

# Matches is the result from Opgave a
matches = {}

for row in eredivisie.eredivisie:
    splitted = row.split(": ")
    team_names = tuple(splitted[0].split(" - "))
    scores = splitted[1].split(" - ")
    diff = int(scores[0]) - int(scores[1])
    if diff < 0:
        # 'Verschil' has to be positive, right?
        diff *= -1

    matches[team_names] = diff

print(matches)

# ---

print("\n---\n")

# opgave_wants_us_to_use_a_list_though is the result from Opgave b
opgave_wants_us_to_use_a_list_though = []

# (But a dict is nice to check if a Team object has been created yet)
teams = {}

for row in eredivisie.eredivisie:
    splitted = row.split(": ")
    team_names = tuple(splitted[0].split(" - "))
    goals = splitted[1].split(" - ")
    goal0 = int(goals[0])
    goal1 = int(goals[1])

    # Create Team object if not yet created.
    if team_names[0] not in teams:
        teams[team_names[0]] = eredivisie.Team(team_names[0])
    if team_names[1] not in teams:
        teams[team_names[1]] = eredivisie.Team(team_names[1])

    # Update goal_difference
    teams[team_names[0]].goal_difference += goal0 - goal1
    teams[team_names[1]].goal_difference += goal1 - goal0

    # Reward points
    reward_points0 = 0
    reward_points1 = 0
    if goal0 is goal1:
        reward_points0 = 1
        reward_points1 = 1
    elif goal0 < goal1:
        reward_points0 = 0
        reward_points1 = 3
    else:
        reward_points0 = 3
        reward_points1 = 0
    teams[team_names[0]].points += reward_points0
    teams[team_names[1]].points += reward_points1


for t in teams:
    opgave_wants_us_to_use_a_list_though.append(teams[t])

for t in opgave_wants_us_to_use_a_list_though:
    print(t)

# ---

print("\n---\n")

winner = max(opgave_wants_us_to_use_a_list_though,
        key=lambda x: (x.points, x.goal_difference))
print("The winner is:\n", winner)
