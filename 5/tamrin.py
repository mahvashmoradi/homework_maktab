class Runner():
    def __init__(self, name, distance, duration, speed=None, pace=None, category=None):
        self.name = name
        self.distance = distance
        self.duration = duration
        self.speed = speed
        self.pace = pace
        self.category = category


    def set_category(self):  # instance method
        """
        :return: set category for every object
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
        return