
class Technologie:
    def __init__(self, sta):
        self.sta = sta


    @property
    def sta(self):
        return self.__sta
    
    @sta.setter
    def sta(self, value):
        self.__sta = value


