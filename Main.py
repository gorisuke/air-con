from TemperatureControl import TemperatureControl

class Main:
    def __init__(self):
        self.tc = TemperatureControl()

    def PeriodicTask(self):
        self.tc.adjust()


if __name__ == "__main__":
    m = Main()
    m.PeriodicTask()

