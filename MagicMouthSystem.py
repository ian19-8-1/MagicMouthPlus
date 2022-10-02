from typing import List
from MagicMouth import MagicMouth
from Trigger import Trigger
from TriggerParams import TriggerParams


class MagicMouthSystem():
    def __init__(self, id, name=None):
        self.id = id
        if name:
            self.name = name
        else:
            self.name = id

        self.mouths = {}
        self.containerMap = {}
        self.containers = []

    def get(self, id):
        return self.mouths[id]

    def add(self, mouth: MagicMouth):
        self.mouths[mouth.id] = mouth

        x, y, z = mouth.pos[0], mouth.pos[1], mouth.pos[2]
        if x not in self.containerMap:
            self.containerMap[x] = {}
        if y not in self.containerMap[x]:
            self.containerMap[x][y] = {}
        if z not in self.containerMap[x][y]:
            container = Container(pos=[x, y, z])
            self.containerMap[x][y][z] = container
            self.containers.append(container)
        self.containerMap[x][y][z].add(mouth.id)

    def remove(self, id):
        if id not in self.mouths:
            return
        else:
            self.mouths.pop(id)

    ### TRIGGER HANDLING ###
    def raise_trigger(self, trigger: Trigger):
        self.raise_triggers([trigger])

    def raise_triggers(self, triggers: List[Trigger]):
        simul_outputs = []

        for mouth in self.mouths.values():
            if mouth.try_triggers(triggers):
                out_trig, vol, dur = mouth.speak()
                simul_outputs.append(out_trig)

        if simul_outputs:
            self.raise_triggers(simul_outputs)

    ### SUMMARIZING ###
    def cost(self):
        return 10 * len(self.mouths)
    
    def cast_time(self):
        mins = 0
        for mouth in self.mouths.values():
            mins += mouth.casttime_rit

        hours = mins // 60
        mins = mins % 60

        days = hours // 24
        hours = hours % 24

        return days, hours, mins

    def print_containers(self):
        for container in self.containers:
            print(container.id, container.pos, container.mouths)

    def print_summary(self):
        print("--- " + str(self.name) + " ---")

        print("Total cost: " + str(self.cost()) + " gp")

        days, hours, mins = self.cast_time()
        cast_time_output = "Total ritual casting time: "
        if days > 0: cast_time_output += str(days) + " days "
        if hours > 0: cast_time_output += str(hours) + " hours "
        if mins > 0: cast_time_output += str(mins) + " mins"
        print(cast_time_output)


class Container:
    def __init__(self, id="", pos=None):
        self.id = id
        self.mouths = []
        self.pos = pos

    def add(self, id):
        self.mouths.append(id)