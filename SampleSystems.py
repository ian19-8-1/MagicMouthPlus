from MagicMouth import MagicMouth
from TriggerParams import TriggerParams
from MagicMouthSystem import MagicMouthSystem
from Trigger import Trigger

class SimpleRelay(MagicMouthSystem):
    def __init__(self, id):
        super().__init__(id)

        def trig_fn(self, trigger: Trigger, mouth: MagicMouth):
            return self.trig_in_range(trigger.pos, mouth.pos) and trigger.atrig == self.atrig

        param1 = TriggerParams(function=trig_fn, atrig="Execute")
        param2 = TriggerParams(function=trig_fn, atrig="Hello World")

        self.add(MagicMouth(
            id="stone1",
            out_msg="Hello World", 
            pos=[0, 0, 30], 
            trig_params=[param1], 
            out_vol=5
        ))
        self.add(MagicMouth(
            id="stone2",
            out_msg="Hello World", 
            pos=[0, 0, 60], 
            trig_params=[param2], 
            out_vol=5
        ))
        self.add(MagicMouth(
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

class TwoMessages(SimpleRelay):
    def __init__(self, id):
        super().__init__(id)

        def trig_fn(self, trigger: Trigger, mouth: MagicMouth):
            return self.trig_in_range(trigger.pos, mouth.pos) and trigger.atrig == self.atrig

        param1 = TriggerParams(function=trig_fn, atrig="Start")
        param2 = TriggerParams(function=trig_fn, atrig="Howdy Earth")

        self.add(MagicMouth(
            id="stone4",
            out_msg="Howdy Earth", 
            pos=[0, 0, 30], 
            trig_params=[param1], 
            out_vol=5
        ))
        self.add(MagicMouth(
            id="stone5",
            out_msg="Howdy Earth", 
            pos=[0, 0, 60], 
            trig_params=[param2], 
            out_vol=5
        ))
        self.add(MagicMouth(
            id="stone6",
            out_msg="Telegram Acquired", 
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