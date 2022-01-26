def get_info(runner):
    info = dict()
    info['name'] = runner
    print(">>>" + runner)
    distance = float(input('Enter distance in Km: '))
    duration = float(input('Enter duration time in minute: '))
    speed = distance / (duration / 60)
    pace = duration / distance
    info['distance'] = distance
    info['duration'] = duration
    info['pace'] = round(pace, 2)
    info['speed'] = round(speed, 2)
    return info


def classify(finisher_info):
    if 10 <= finisher_info['distance'] <= 20:
        finisher_info['class'] = '10K'

    elif 21 <= finisher_info['distance'] <= 41:
        finisher_info['class'] = 'half marathon'

    elif 42 <= finisher_info['distance'] <= 60:
        finisher_info['class'] = 'marathon'

    else:
        finisher_info['class'] = 'ultra'
    return finisher_info


def top3(group):
    ls = sorted(group, key=lambda x: x['speed'], reverse=True)[:3]
    for runner in ls:
        print(runner['name'], "\tspeed:", runner['speed'])


runners = list(map(lambda x: x.strip(), input('Enter names: ').split(',')))
runners = sorted(set(runners))
finishers = []
for name in runners:
    info = get_info(name)
    if info['distance'] < 10:
        continue
    else:
        finishers.append(classify(info))

_10k = [x for x in finishers if x['class'] == '10K']
_halfMarathon = [x for x in finishers if x['class'] == 'half marathon']
_marathon = [x for x in finishers if x['class'] == 'marathon']
_ultra = [x for x in finishers if x['class'] == 'ultra']

print("--------Result")

print("Fastest in 10k:")
top3(_10k)
print("\nFastest in half marathon:")
top3(_halfMarathon)
print("\nFastest in marathon:")
top3(_marathon)
print("\nFastest in ultra:")
top3(_ultra)

max_speed = max(list(map(lambda x: x['speed'], finishers)))
fastest = [info['name'] for info in finishers if info['speed'] == max_speed][0]
print("\nThe fastest is {} with speed {}".format(fastest, max_speed))

max_distance = max(list(map(lambda x: x['distance'], finishers)))
resilient = [info['name'] for info in finishers if info['distance'] == max_distance][0]
print("The most resilient is {} with highest distance {}".format(resilient, max_distance))
