"""
This code suggest by Parisa Etemadinejad for HW4 at maktab51
in this code we use base sample for list of runner
"""


class Runner:
    def __init__(self, id_runner, name, distance, duration, speed=None, pace=None, category=None):
        """
        :param id_runner: id of runner - This is unique for every runner
        :param name: name of runner
        :param distance: distance of runner
        :param duration: duration of runner
        :param speed:speed of runner
        :param pace:pace of runner
        :param category: category of runner
        """
        self.id_runner = id_runner
        self.name = name
        self.distance = distance
        self.duration = duration
        self.speed = speed
        self.pace = pace
        self.category = category

    def set_category(self):
        """
            this function set category for every object
        """
        if self.distance < 10:
            self.category = "not finisher"
        elif 10 <= self.distance <= 20:
            self.category = "10k"
        elif 21 <= self.distance <= 41:
            self.category = "half marathon"
        elif 42 <= self.distance <= 60:
            self.category = "marathon"
        else:
            self.category = "ultra"

    def set_speed(self):
        """
            This function set speed for every runner
        """
        self.speed = round(self.distance / (self.duration / 60), 3)

    def set_pace(self):
        """
            This function set pace for every runner
        """
        self.pace = round(self.duration / self.distance, 3)

    def __str__(self):
        return f"{self.name} run {self.distance} in {self.duration} and has {self.speed} speed and {self.pace} pace and {self.category} category."


def top_runners(list_input, metric, count, reverse):
    """
        This function get count argument for show count of top runners base on metric
    """
    members_list = sorted(list_input, key=lambda x:
    x.__getattribute__(metric), reverse=reverse)
    for _ in members_list[:count]:
        print(_.name)


def grouping_object(list_input):
    """
        this function get list of object and grouping them base on metric
    """
    group_list = {x.category for x in list_runner}
    # print(group_list)
    for group in group_list:
        list_runner_grouping = [(_.name, _.speed) for _ in list_input if _.category == group]
        fastest = sorted(list_runner_grouping, key=lambda x: x[1], reverse=True)[0]
        print(f"Fastest runner in {group} is : {fastest}")


NO_runner = int(input('please input number of runner:'))
list_name_runner = []
list_runner = []
for i in range(1, NO_runner + 1):
    while True:
        """
            this while handle unique name and empty name
        """
        name_runner = input('please input name of runner: ')
        if name_runner in list_name_runner:
            print("ERROR:your input name already exist")
        elif name_runner == "":
            print("ERROR:your input name is blank")
        else:
            list_name_runner.append(name_runner)
            break
    distance_runner = int(input('please input distance of runner: '))
    duration_runner = int(input('please input duration of runner: '))
    member = Runner(i, name_runner, distance_runner, duration_runner)
    member.set_category()
    member.set_speed()
    member.set_pace()
    list_runner.append(member)
print('-------------------------------------show all runners----------------- ------------------------------')
print("NO", "      ", "name", "       ", "distance", "      ", "duration", "      ",
      "speed", "      ", "pace", "      ", "category")
for runner in list_runner:
    print(runner.id_runner, "       ", runner.name, "            ", runner.distance, "            ", runner.duration,
          "          ",
          runner.speed, "      ", runner.pace, "      ", runner.category)

print('\n')
print('-------------------------------------show sorted runners---------------------------------------------')
top_runners(list_runner, 'name', len(list_runner), False)
print('\n')
print('-------------------------------------show top_3 runners----------------------------------------------')
top_runners(list_runner, 'speed', 3, True)
print('\n')
print('-------------------------------------show fastest runners--------------------------------------------')
top_runners(list_runner, 'speed', 1, True)
print('\n')
print('-----------------------------show runner that run max distance---------------------------------------')
top_runners(list_runner, 'distance', 1, True)
print('\n')
print('---------------------------show fastest runner in each category--------------------------------------')
grouping_object(list_runner)
