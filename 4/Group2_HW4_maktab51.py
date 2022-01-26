# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:36:37 2021

@author: Group 2
"""

RUNNERS_LIST = [{'id': 0, 'name': 'Kilian Jornet', 'distance': 46, 'duration': 283},
                {'id': 1, 'name': 'Akbar Naghdi', 'distance': 120, 'duration': 720},
                {'id': 2, 'name': 'Negar sammak Nejad', 'distance': 171, 'duration': 2760},
                {'id': 3, 'name': 'Mandana Nouri', 'distance': 21.0975, 'duration': 118},
                {'id': 4, 'name': 'Eliud Kipchoge ', 'distance': 42.195, 'duration': 119},
                {'id': 5, 'name': 'Julius PASKOV', 'distance': 86.3, 'duration': 870},
                {'id': 6, 'name': 'Anabela RENDA', 'distance': 25.7, 'duration': 195},
                {'id': 7, 'name': 'Alexis SEVENNEC', 'distance': 24.1, 'duration': 140},
                {'id': 8, 'name': 'Joyciline Jepkosgei', 'distance': 10, 'duration': 28},
                {'id': 9, 'name': 'Rhonex Kipruto', 'distance': 10, 'duration': 26},
                {'id': 10, 'name': 'Vincent Kibet', 'distance': 10, 'duration': 27},
                {'id': 11, 'name': 'Senbere Teferi', 'distance': 10, 'duration': 30.2},
                {'id': 12, 'name': 'Payam Dibaj', 'distance': 30, 'duration': 152},
                {'id': 13, 'name': 'Sepideh Nouri', 'distance': 27, 'duration': 142},
                {'id': 14, 'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137}]


class Runner:
    def __init__(self, name, distance, duration):
        self.name = name
        self.distance = distance
        self.duration = duration

    def set_record(self):
        self.speed = round(self.distance / (self.duration / 60), 3)
        self.pace = round(self.duration / self.distance, 3)

    def categorize(self):
        if self.distance < 10:
            self.category = 'not finisher'
        elif 10 <= self.distance <= 20:
            self.category = '10k'
        elif 21 <= self.distance <= 41:
            self.category = 'half marathon'
        elif 42 <= self.distance <= 60:
            self.category = 'marathon'
        else:
            self.category = 'ultra'

    def __str__(self):
        return f'*{self.name}* speed: {self.speed} pace: {self.pace}' \
            f' distance: {self.distance} class: {self.category}'


# sorts the list of objects(result) by metric(speed,distance)
def ranking(members_list, metric, count=None):
    members_list = sorted(members_list, key=lambda x: x.__getattribute__(metric), reverse=True)
    return members_list[:count]


result = []
for i in range(len(RUNNERS_LIST)):
    runner = Runner(RUNNERS_LIST[i]['name'], RUNNERS_LIST[i]['distance'],
                    RUNNERS_LIST[i]['duration'])
    runner.set_record()
    runner.categorize()
    result.append(runner)

sort_byName = sorted(result, key=lambda x: x.name)
Print_byName = [print(i) for i in sort_byName]
print('--------Top 3 with the most speed--------')
Print_bySpeed = [print(i) for i in [j for j in ranking(result, 'speed', 3)]]
print("-----------------------------------------")
print("* * The Fastest * *")
Print_fastest = [print(i) for i in [j for j in ranking(result, 'speed', 1)]]
print("* * Resilient * *")
resilient = [print(i) for i in [j for j in ranking(result, 'distance', 1)]]
print("-----------------------------------------")

# {'not finisher', '10k', 'half_marathon', 'marathon', 'ultra'}
# a set of categories
categories = {x.category for x in result}
# finds runner with the most speed in each category
for group in categories:
    info = [(runner.name, runner.speed) for runner in result if runner.category == group]
    top = sorted(info, key=lambda x: x[1], reverse=True)[0]

    print(f"Fastest in {group} : {top}")
