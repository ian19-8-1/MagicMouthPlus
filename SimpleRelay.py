from MagicMouth import MagicMouth
from TriggerParams import TriggerParams
from MagicMouthSystem import MagicMouthSystem
from Trigger import Trigger

class SimpleRelay(MagicMouthSystem):
    def __init__(self):
        super().__init__(self)

        def trig_fn(self, trigger: Trigger, mouth: MagicMouth):
            return self.trig_in_range(trigger.pos, mouth.pos) and trigger.atrig == self.atrig

        param1 = TriggerParams(function=trig_fn, atrig="Execute")
        param2 = TriggerParams(function=trig_fn, atrig="Hello World")

        self.add("stone1", MagicMouth(
            id="stone1",
            out_msg="Hello World", 
            pos=[0, 0, 30], 
            trig_params=[param1], 
            out_vol=1
        ))
        self.add("stone2", MagicMouth(
            id="stone2",
            out_msg="Hello World", 
            pos=[0, 0, 60], 
            trig_params=[param2], 
            out_vol=1
        ))
        self.add("stone3", MagicMouth(
            id="stone3",
            out_msg="Message Received", 
            pos=[0, 0, 90], 
            trig_params=[param2]
        ))

    def execute(self, msg):
        print("Command:", msg)

        init_trig = Trigger(
            atrig=msg, 
            pos=[0, 0, 0], 
            source="Ian", 
            source_type="human"
        )

        self.raise_trigger(init_trig)