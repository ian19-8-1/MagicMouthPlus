from typing import List

from Trigger import Trigger


class MagicMouth():
    def __init__(
        self, 
        out_msg, 
        id, 
        pos=None,
        out_vol=5, 
        out_dur=1, 
        trig_params=[]
    ):

        # METADATA
        self.id = id                # simple descriptor/id of the object that the mouth is attached to

        self.pos = pos                      # x, y, z coordinates of this magic mouth in feet (relative)

        self.cost = 10                      # casting cost in gp
        self.casttime_rit = 11              # ritual casting time in minutes
        self.casttime = 1

        # TRIGGERS
        self.trig_params = trig_params      # assign one or more trigger conditions

        # OUTPUT
        if len(out_msg.split(" ")) > 25:
            print("ERROR: messages must be 25 words or less")
            return
        self.out_msg = out_msg              # the output message
        self.out_vol = out_vol              # the output message's volume (1 for near-inaudible whisper, 10 for screaming)
        self.out_dur = out_dur              # the output's duration in seconds

    def speak(self):
        if self.out_vol >= 3:
            print(self.out_msg, "(" + self.id + ")")
        return Trigger(atrig=self.out_msg, pos=self.pos, source=self.id), self.out_vol, self.out_dur

    def try_triggers(self, triggers: List[Trigger]):        # can be overriden for special cases
        num_satis = 0

        for trigger in triggers:
            if trigger.source == self.id:
                break
            for param in self.trig_params:
                if param.try_trigger(trigger, self): num_satis += 1

        if num_satis == len(self.trig_params):              # if all conditions are satisfied, trigger
            return True
        else:
            return False