# a lambda function for categorizing runners based on the distance they ran
category = lambda x: "not finisher" if x < 10 \
    else "10k" if 10 <= x < 21.0975 \
    else "halfMarathon" if 21.0975 <= x < 42.195 \
    else "marathon" if 42.195 <= x < 60 \
    else "ultra"


class Runner:
    id = 0  # this class attribute is used to give every runner a unique id

    def __init__(self, name, distance, duration):
        self.name = name  # name of the runner
        self.distance = distance  # distance he/she ran
        self.duration = duration  # the amount of time taken to run the distance
        self.id = Runner.id  # runner's unique id
        Runner.id += 1
        self.speed = (self.distance / self.duration) / 60  # speed of the runner(km/h)
        self.pace = self.duration / self.distance  # pace of the runner(min/km)
        self.category = category(
            self.distance)  # one of "not finisher","10k","halfMarathon","marathon","ultra" categories based on distance

    def __str__(self):
        return f"{self.name, self.id, self.speed, self.pace, self.category}"


runners_list = [{'name': 'Kilian Jornet', 'distance': 46, 'duration': 283},
                {'name': 'Akbar Naghdi', 'distance': 120, 'duration': 720},
                {'name': 'Negar sammak Nejad', 'distance': 171, 'duration': 2760},
                {'name': 'Mandana Nouri', 'distance': 21.0975, 'duration': 118},
                {'name': 'Eliud Kipchoge ', 'distance': 42.195, 'duration': 119},
                {'name': 'Julius PASKOV', 'distance': 86.3, 'duration': 870},
                {'name': 'Anabela RENDA', 'distance': 25.7, 'duration': 195},
                {'name': 'Alexis SEVENNEC', 'distance': 24.1, 'duration': 140},
                {'name': 'Joyciline Jepkosgei', 'distance': 10, 'duration': 180},
                {'name': 'Rhonex Kipruto', 'distance': 10, 'duration': 26},
                {'name': 'Vincent Kibet', 'distance': 10, 'duration': 27},
                {'name': 'Senbere Teferi', 'distance': 10, 'duration': 30.2},
                {'name': 'Payam Dibaj', 'distance': 30, 'duration': 152},
                {'name': 'Sepideh Nouri', 'distance': 27, 'duration': 142},
                {'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137}]

lst = []  # used to create a list of runner objects
names = []  # used to omit repeated names
for runner in runners_list:
    if runner['name'] not in names:
        names.append(runner['name'])
        x = (Runner(runner["name"], runner['distance'], runner['duration']))
        lst.append(x)

# shows the list of all runners
print("list of runners:")
for i in lst:
    print(i)
print("#####################################################")

# shows the sorted list of all runners based on their names
print("sorted list of runners based on their names:")
members_list = sorted(lst, key=lambda x: x.name)
for i in members_list:
    print(i)
print("#####################################################")

# shows three fastest runners
print("list of three fastest runners:")
members_list = sorted(lst, key=lambda x: x.speed, reverse=True)[:3]
for i in members_list:
    print(i)
print("#####################################################")


# show the fastest runner in each category
category = ['10k', 'halfMarathon', 'marathon', 'ultra']
categorized_runners = dict()
for group in category:
    categorized_runners[group] = [info for info in lst if info.category == group]
print("list of fastest runner in each category:")
for i in categorized_runners:
    x = sorted(categorized_runners[i], key=lambda x: x.speed, reverse=True)[:1][0]
    print(x)
print("#####################################################")

# show the fastest runner
print("fastest runner:")
x = sorted(lst, key=lambda x: x.speed, reverse=True)[:1][0]
print(x)
print("#####################################################")

# show runner with largest distance
print("runner with the largest distance:")
x = sorted(lst, key=lambda x: x.distance, reverse=True)[:1][0]
print(x)
print("#####################################################")

