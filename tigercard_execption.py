class InvalidZone(Exception):
    def __init__(self, zone):
        self.zone = zone
        self.msg = f"Zone {zone} not in operation"
        super().__init__(self.msg)
