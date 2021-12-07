import time
class TrafficLight:
    color = 0

    def running(self, color):
        self.color = color

__red_traff = TrafficLight()
__yellow_traff = TrafficLight()
__green_traff = TrafficLight()
__red_traff.running('Красный')
__yellow_traff.running('Желтый')
__green_traff.running('Зеленый')

def timer(time_sec):
    # time_sec = int(input('Время горения светофора зеленым'))
    while time_sec != 0:
        print(__red_traff.color, ' ', time_sec)
        time.sleep(1)
        time_sec -= 1

timer(7)

def timer(time_sec):
    # time_sec = int(input('Время горения светофора зеленым'))
    while time_sec != 0:
        print(__yellow_traff.color, ' ', time_sec)
        time.sleep(1)
        time_sec -= 1
timer(5)

def timer():
    time_sec = int(input('Время горения светофора зеленым - '))
    while time_sec != 0:
        print(__green_traff.color, ' ', time_sec)
        time.sleep(1)
        time_sec -= 1
timer()