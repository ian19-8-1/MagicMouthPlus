class Trigger():
    def __init__(
        self, 
        source: str,
        atrig=None, 
        vtrig=None, 
        pos=None,
        person=None, 
        source_type=None, 
        misc=None
    ):
        self.atrig = atrig
        self.vtrig = vtrig
        self.pos = pos
        self.source = source
        self.source_type = source_type
        self.misc = misc