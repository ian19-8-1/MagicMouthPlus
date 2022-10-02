from Trigger import Trigger
from MagicMouth import MagicMouth

def match_audio(self, trigger: Trigger, mouth: MagicMouth):
    in_range = True
    if trigger.pos and mouth.pos:
        in_range = self.trig_in_range(trigger.pos, mouth.pos)
    trig_match = (trigger.atrig == self.atrig)
    
    return in_range and trig_match

def match_audio_oneway(self, trigger, mouth):
    in_range = True
    if trigger.pos and mouth.pos:
        in_range = self.trig_in_range(trigger.pos, mouth.pos)
    trig_match = (trigger.atrig == self.atrig)
    source_match = (trigger.source == self.source)
    
    return in_range and trig_match and source_match

def match_visual(self, trigger, mouth):
    in_range = True
    if trigger.pos and mouth.pos:
        in_range = self.trig_in_range(trigger.pos, mouth.pos)
    trig_match = (trigger.vtrig == self.vtrig)
    source_type_match = (trigger.source_type == self.source_type)

    return in_range and trig_match and source_type_match