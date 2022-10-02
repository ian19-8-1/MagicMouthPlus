from math import sqrt
from MagicMouth import MagicMouth
from Trigger import Trigger

class TriggerParams():
    def __init__(
        self, 
        function,
        atrig=None, 
        vtrig=None, 
        min_trigrange=0, 
        max_trigrange=30, 
        source=None, 
        source_type=None, 
        misc=None
    ):
        self.function = function
        self.atrig = atrig
        self.vtrig = vtrig
        self.min_trigrange = min_trigrange
        self.max_trigrange = max_trigrange
        self.source = source
        self.source_type = source_type
        self.misc = misc

    def trig_in_range(self, trig_pos, mouth_pos):
        if not trig_pos:
            return True

        dist = sqrt(pow(mouth_pos[0] - trig_pos[0], 2) + 
                    pow(mouth_pos[1] - trig_pos[1], 2) + 
                    pow(mouth_pos[2] - trig_pos[2], 2) * 1.0)
        if dist >= self.min_trigrange and dist <= self.max_trigrange:
            return True
        else:
            return False

    def process_str(self, str):
        return str.lower()

    def try_trigger(self, trigger: Trigger, mouth: MagicMouth): 
        return self.function(self, trigger, mouth)