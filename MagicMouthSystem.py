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

        self.system = {}

    def get(self, id):
        return self.system[id]

    def add(self, id, mouth: MagicMouth):
        self.system[id] = mouth

    def remove(self, id):
        if id not in self.system:
            return
        else:
            self.system.pop(id)

    def get_mouths(self):
        return self.system.values()

    def cost(self):
        return 10 * len(self.system)
    
    def cast_time(self):
        mins = 0
        for mouth in self.system.values():
            mins += mouth.casttime_rit

        hours = mins // 60
        mins = mins % 60

        days = hours // 24
        hours = hours % 24

        return days, hours, mins

    def print_summary(self):
        print("--- " + self.name + " ---")

        print("Total cost: " + str(self.cost()) + " gp")

        days, hours, mins = self.cast_time()
        cast_time_output = "Total ritual casting time: "
        if days > 0: cast_time_output += str(days) + " days "
        if hours > 0: cast_time_output += str(hours) + " hours "
        if mins > 0: cast_time_output += str(mins) + " mins"
        print(cast_time_output)

    def raise_trigger(self, trigger: Trigger):
        self.raise_triggers([trigger])

    def raise_triggers(self, triggers: List[Trigger]):
        simul_outputs = []

        for mouth in self.system.values():
            if mouth.try_triggers(triggers):
                out_trig, vol, dur = mouth.speak()
                simul_outputs.append(out_trig)

        if simul_outputs:
            self.raise_triggers(simul_outputs)