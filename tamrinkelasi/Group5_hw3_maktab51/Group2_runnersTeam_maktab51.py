def get_info(runner):
    info = dict()
    info['name'] = runner
    print(">>>" + runner)
    distance = float(input('Enter distance in Km: '))
    duration = float(input('Enter duration time in minute: '))
    speed = distance / (duration / 60)
    info['distance'] = distance
    info['speed'] = round(speed, 2)
    return info


def calc_result(team_info):
    total_distance = sum(list(map(lambda x: x['distance'], team_info)))
    total_speed = list(map(lambda x: x['speed'], team_info))
    avg_speed = round(sum(total_speed) / len(total_speed), 2)
    max_speed = max(total_speed)
    team_leader = [info for info in team_info if info['speed'] == max_speed][0]
    return {'Total distance': total_distance, 'Average speed': avg_speed, 'Team leader': team_leader}


teams = list(map(lambda x: x.split(','), input('Enter names: ').split('*')))
teams = [tuple(name.strip() for name in t) for t in teams]
teams = [tuple(sorted(set(name for name in t))) for t in teams]
result = []
for team in teams:
    team_info = []
    for member in team:
        team_info.append(get_info(member))
    print("* * * *")
    result.append(calc_result(team_info))

for i in range(len(result)):
    print("Team", i + 1)
    print(result[i])

top3 = sorted(result, key=lambda x: x['Total distance'], reverse=True)[:3]
print("Top teams:")
for i in range(len(top3)):
    print(i+1, top3[i])
