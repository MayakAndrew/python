incom = {'wage': 10, 'bonus': 20}
a = incom['wage']
b = incom['bonus']
inc = a + b
# print(inc)

class Worker:

    def __init__(self, name, surname, position, inc):
        self.name = name
        self.surname = surname
        self.position = position
        self._inc = inc

pod_1 = Worker('Andrew', 'Mayak', 'manager', inc)
# print(pod_1.name, pod_1.surname, pod_1._inc)

class Position(Worker):

    def get_full_name(self, worker):
        self.name = worker
pod_2 = Position(Worker)
pod_2.get_full_name(Worker.name)
print(pod_2.name)

        # print(worker.name)


