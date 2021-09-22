class TigerCardException(Exception):
    pass


class InvalidZone(Exception):
    def __init__(self, zone):
        self.zone = zone
        self.msg = "Zone not in operation"
        super().__init__(self.msg)
