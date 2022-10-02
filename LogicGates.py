from MagicMouth import MagicMouth
from TriggerParams import TriggerParams
import TriggerTestFunctions


class Binary(MagicMouth):
    def __init__(self, id, trig_msg, pos=None, out_vol=5, out_dur=1):
        super().__init__(
            id, 
            "1",
            pos, 
            out_vol, 
            out_dur, 
            trig_params=[TriggerParams(function=TriggerTestFunctions.match_audio, atrig=trig_msg)], 
        )


class And(MagicMouth):
    def __init__(self, id, trig1, trig2, input_source1, input_source2, pos=None, out_vol=5, out_dur=1):

        param1 = TriggerParams(function=TriggerTestFunctions.match_audio_oneway, atrig=trig1, source=input_source1)
        param2 = TriggerParams(function=TriggerTestFunctions.match_audio_oneway, atrig=trig2, source=input_source2)

        super().__init__(id, "1", pos, out_vol, out_dur, trig_params=[param1, param2])

class Or(MagicMouth):
    def __init__(self, id, trig1, trig2, input_source1, input_source2, pos=None, out_vol=5, out_dur=1):

        param1 = TriggerParams(function=TriggerTestFunctions.match_audio_oneway, atrig=trig1, source=input_source1)
        param2 = TriggerParams(function=TriggerTestFunctions.match_audio_oneway, atrig=trig2, source=input_source2)

        super().__init__(id, "1", pos, out_vol, out_dur, trig_params=[param1, param2])

    def try_triggers(self, triggers):
        for trigger in triggers:
            if trigger.source == self.id:
                break
            for param in self.trig_params:
                if param.try_trigger(trigger, self): return True

        return False

class Xor(MagicMouth):
    def __init__(self, id, trig1, trig2, input_source1, input_source2, pos=None, out_vol=5, out_dur=1):

        param1 = TriggerParams(function=TriggerTestFunctions.match_audio_oneway, atrig=trig1, source=input_source1)
        param2 = TriggerParams(function=TriggerTestFunctions.match_audio_oneway, atrig=trig2, source=input_source2)

        super().__init__(id, "1", pos, out_vol, out_dur, trig_params=[param1, param2])

    def try_triggers(self, triggers):
        num_satis = 0

        for trigger in triggers:
            if trigger.source == self.id:
                break
            for param in self.trig_params:
                if param.try_trigger(trigger, self): num_satis += 1

        if num_satis == 1:             
            return True
        else:
            return False