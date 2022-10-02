from MagicMouth import MagicMouth
from TriggerParams import TriggerParams
from MagicMouthSystem import MagicMouthSystem
from Trigger import Trigger
from TriggerTestFunctions import match_audio, match_audio_oneway, match_visual
import LogicGates

class SimpleRelay(MagicMouthSystem):
    def __init__(self, id):
        super().__init__(id)

        param1 = TriggerParams(function=match_audio, atrig="Execute")
        param2 = TriggerParams(function=match_audio_oneway, atrig="Hello World", source="stone1")
        param3 = TriggerParams(function=match_audio_oneway, atrig="Hello World", source="stone2")

        self.add(MagicMouth(
            id="stone1",
            out_msg="Hello World", 
            pos=[0, 0, 30], 
            trig_params=[param1], 
            out_vol=5, 
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
            trig_params=[param3]
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

        param1 = TriggerParams(function=match_audio, atrig="Start")
        param2 = TriggerParams(function=match_audio, atrig="Howdy Earth")

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

class FeedbackLoop(MagicMouthSystem):
    def __init__(self, id):
        super().__init__(id)

        param1 = TriggerParams(function=match_audio, atrig="Execute")
        param2 = TriggerParams(function=match_audio, atrig="Feedback")

        self.add(MagicMouth(
            id="stone1", 
            out_msg="Feedback", 
            pos=[0, 0, 30], 
            trig_params=[param1]
        ))

        ids = ["stone2", "stone3"]
        poss = [[0, 0, 60], [0, 0, 90]] 
        for i in range(2):
            self.add(MagicMouth(
                id=ids[i], 
                out_msg="Feedback", 
                pos=poss[i], 
                trig_params=[param2]
            ))
        
    def execute(self):
        print("Command: Execute")

        init_trig = Trigger(
            atrig="Execute", 
            pos=[0, 0, 0], 
            source="Ian", 
            source_type="human"
        )

        self.raise_trigger(init_trig)

class Repeater(MagicMouthSystem):
    def __init__(self, id):
        super().__init__(id)

        param = TriggerParams(function=match_visual, vtrig="move", source_type="grass")
        self.add(MagicMouth(
            id="pebble", 
            out_msg="AH", 
            trig_params=[param]
        ))

    def execute(self, num_loops, debug=False):
        print("Time start")

        init_trig = Trigger(
            vtrig="move", 
            source="grass", 
            source_type="grass"
        )

        for i in range(num_loops):
            self.raise_trigger(init_trig, debug)

        print("Time stop")

class AndGateTest(MagicMouthSystem):
    def __init__(self, id, name=None):
        super().__init__(id, name)

        self.add(LogicGates.And(
            id="and", 
            trig1="Execute", 
            trig2="Start",
            input_source1="s1", 
            input_source2="s2"
        ))

    def execute(self, input1, input2, source1, source2, debug):
        trig1 = Trigger(atrig=input1, source=source1)
        trig2 = Trigger(atrig=input2, source=source2)

        self.raise_triggers([trig1, trig2], debug)

class OrGateTest(MagicMouthSystem):
    def __init__(self, id, name=None):
        super().__init__(id, name)

        self.add(LogicGates.Or(
            id="or", 
            trig1="Execute", 
            trig2="Start", 
            input_source1="s1", 
            input_source2="s2"
        ))

    def execute(self, input1, input2, source1, source2):
        trig1 = Trigger(atrig=input1, source=source1)
        trig2 = Trigger(atrig=input2, source=source2)

        self.raise_triggers([trig1, trig2])

class XorGateTest(MagicMouthSystem):
    def __init__(self, id, name=None):
        super().__init__(id, name)

        self.add(LogicGates.Xor(
            id="or", 
            trig1="Execute", 
            trig2="Start", 
            input_source1="s1", 
            input_source2="s2"
        ))

    def execute(self, input1, input2, source1, source2):
        trig1 = Trigger(atrig=input1, source=source1)
        trig2 = Trigger(atrig=input2, source=source2)

        self.raise_triggers([trig1, trig2])